'''
Notification Module for LinkedIn AI Bot
Supports:
1. ntfy.sh (Instant zero-setup push notifications to Android & iOS)
2. Telegram Bot
3. Discord Webhook
'''

import os
import sys
import datetime
import base64
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from urllib.parse import quote_plus

# Try loading settings safely
try:
    from config.settings import (
        enable_phone_notifications,
        ntfy_topic,
        telegram_bot_token,
        telegram_chat_id,
        discord_webhook_url,
        enable_email_job_notifications,
        enable_whatsapp_job_notifications
    )
except ImportError:
    enable_phone_notifications = True
    ntfy_topic = "omkar_linkedin_bot_alerts"
    telegram_bot_token = ""
    telegram_chat_id = ""
    discord_webhook_url = ""
    enable_email_job_notifications = True
    enable_whatsapp_job_notifications = False

try:
    from config.secrets import (
        email_sender,
        email_app_password,
        email_recipient,
        whatsapp_phone,
        whatsapp_callmebot_apikey
    )
except ImportError:
    email_sender = "omkarjadhav095@gmail.com"
    email_app_password = "wijbspufmqnotflh"
    email_recipient = "omkarjadhav095@gmail.com"
    whatsapp_phone = ""
    whatsapp_callmebot_apikey = ""


def _encode_rfc2047(text: str) -> str:
    '''
    Encode header value using RFC 2047 standard to safely support emojis and unicode.
    '''
    try:
        text.encode('ascii')
        return text
    except UnicodeEncodeError:
        b64 = base64.b64encode(text.encode('utf-8')).decode('ascii')
        return f"=?utf-8?b?{b64}?="


def send_ntfy(topic: str, title: str, message: str, priority: str = "default", tags: str = "robot") -> bool:
    '''
    Send push notification via ntfy.sh to your phone.
    No account or API key required. Just install the 'ntfy' app on Android or iOS
    and subscribe to the topic name.
    '''
    if not topic or topic == "YOUR_UNIQUE_NTFY_TOPIC_HERE":
        return False
    
    url = f"https://ntfy.sh/{topic}"
    headers = {
        "Title": _encode_rfc2047(title),
        "Priority": priority,  # min, low, default, high, urgent
        "Tags": tags
    }
    try:
        response = requests.post(url, data=message.encode("utf-8"), headers=headers, timeout=10)
        return response.status_code == 200
    except Exception as e:
        print(f"[Notifier] Failed to send ntfy notification: {e}")
        return False


def send_telegram(token: str, chat_id: str, message: str) -> bool:
    '''
    Send message via Telegram Bot API.
    '''
    if not token or not chat_id:
        return False
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        return response.status_code == 200
    except Exception as e:
        print(f"[Notifier] Failed to send Telegram message: {e}")
        return False


def send_discord(webhook_url: str, title: str, message: str, color: int = 3447003) -> bool:
    '''
    Send message via Discord Webhook.
    '''
    if not webhook_url:
        return False
    
    payload = {
        "embeds": [
            {
                "title": title,
                "description": message,
                "color": color,
                "timestamp": datetime.datetime.utcnow().isoformat()
            }
        ]
    }
    try:
        response = requests.post(webhook_url, json=payload, timeout=10)
        return response.status_code in (200, 204)
    except Exception as e:
        print(f"[Notifier] Failed to send Discord webhook: {e}")
        return False


def send_email(subject: str, html_body: str, text_body: str = None) -> bool:
    '''
    Send HTML email notification via Gmail SMTP.
    '''
    sender = globals().get("email_sender", "")
    pwd = globals().get("email_app_password", "")
    recipient = globals().get("email_recipient", "") or sender

    if not sender or not pwd or not recipient:
        return False

    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = f"LinkedIn AI Bot <{sender}>"
        msg["To"] = recipient

        if text_body:
            msg.attach(MIMEText(text_body, "plain", "utf-8"))
        msg.attach(MIMEText(html_body, "html", "utf-8"))

        with smtplib.SMTP("smtp.gmail.com", 587, timeout=15) as server:
            server.starttls()
            server.login(sender, pwd)
            server.sendmail(sender, recipient, msg.as_string())
        print(f"[Notifier] Email notification sent to {recipient}!")
        return True
    except Exception as e:
        print(f"[Notifier] Failed to send email: {e}")
        return False


def send_whatsapp(phone: str, apikey: str, message: str) -> bool:
    '''
    Send WhatsApp message via CallMeBot API.
    '''
    if not phone or not apikey:
        return False

    phone = phone.strip().replace(" ", "").replace("-", "")
    url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={quote_plus(message)}&apikey={apikey}"
    try:
        res = requests.get(url, timeout=15)
        if res.status_code == 200:
            print(f"[Notifier] WhatsApp message sent to {phone}!")
            return True
        else:
            print(f"[Notifier] CallMeBot returned status {res.status_code}: {res.text}")
            return False
    except Exception as e:
        print(f"[Notifier] Failed to send WhatsApp message: {e}")
        return False


def notify_external_job(
    title: str,
    company: str,
    work_location: str,
    work_style: str,
    job_link: str,
    application_link: str,
    experience_required: str = "Unknown",
    skills: str = ""
) -> None:
    '''
    Send rich notification (Email + WhatsApp + ntfy/phone) when a relevant non-Easy Apply job is found.
    '''
    now_str = datetime.datetime.now().strftime("%d %b %Y, %I:%M %p")
    clean_app_link = application_link if application_link and application_link != "Easy Applied" else job_link
    skills_text = ", ".join(skills) if isinstance(skills, (list, set)) else str(skills or "Not specified")

    # 1. Dispatch Email (if enabled)
    if globals().get("enable_email_job_notifications", True):
        subject = f"💼 [Job Lead] {title} at {company} ({work_location})"
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 20px; background-color: #f4f6f8; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <div style="max-width: 600px; margin: 0 auto; background: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.08); border: 1px solid #e1e4e8;">
    
    <!-- Header -->
    <div style="background: linear-gradient(135deg, #0a66c2 0%, #004182 100%); padding: 24px 28px; color: #ffffff;">
      <span style="background: rgba(255,255,255,0.22); color: #ffffff; font-size: 11px; font-weight: 700; text-transform: uppercase; padding: 4px 10px; border-radius: 20px; letter-spacing: 0.5px;">External Apply Opportunity</span>
      <h1 style="margin: 12px 0 6px 0; font-size: 22px; font-weight: 700; color: #ffffff; line-height: 1.3;">{title}</h1>
      <p style="margin: 0; font-size: 16px; opacity: 0.95; font-weight: 500;">🏢 {company}</p>
    </div>

    <!-- Body Info -->
    <div style="padding: 24px 28px;">
      <table style="width: 100%; border-collapse: collapse; margin-bottom: 24px;">
        <tr style="border-bottom: 1px solid #f0f2f5;">
          <td style="padding: 10px 0; color: #65676b; font-size: 14px; width: 130px;">📍 <b>Location:</b></td>
          <td style="padding: 10px 0; color: #1c1e21; font-size: 14px; font-weight: 600;">{work_location} ({work_style})</td>
        </tr>
        <tr style="border-bottom: 1px solid #f0f2f5;">
          <td style="padding: 10px 0; color: #65676b; font-size: 14px;">🎯 <b>Experience:</b></td>
          <td style="padding: 10px 0; color: #1c1e21; font-size: 14px; font-weight: 600;">{experience_required}</td>
        </tr>
        <tr style="border-bottom: 1px solid #f0f2f5;">
          <td style="padding: 10px 0; color: #65676b; font-size: 14px;">💡 <b>Key Skills:</b></td>
          <td style="padding: 10px 0; color: #1c1e21; font-size: 14px;">{skills_text}</td>
        </tr>
      </table>

      <!-- Action Buttons -->
      <div style="text-align: center; margin-top: 25px; margin-bottom: 10px;">
        <a href="{clean_app_link}" target="_blank" style="display: inline-block; background-color: #0a66c2; color: #ffffff; text-decoration: none; font-weight: 700; padding: 14px 28px; border-radius: 8px; font-size: 15px; margin: 6px; box-shadow: 0 4px 10px rgba(10,102,194,0.3);">🚀 Apply on Company Website</a>
        <a href="{job_link}" target="_blank" style="display: inline-block; background-color: #f0f2f5; color: #0a66c2; text-decoration: none; font-weight: 600; padding: 14px 22px; border-radius: 8px; font-size: 14px; margin: 6px; border: 1px solid #d0d7de;">View on LinkedIn</a>
      </div>
    </div>

    <!-- Footer -->
    <div style="background: #f8fafc; padding: 14px 28px; font-size: 12px; color: #8c9ba5; text-align: center; border-top: 1px solid #eef2f6;">
      Filtered & matched by your LinkedIn AI Bot · {now_str}
    </div>
  </div>
</body>
</html>
"""
        plain_text = (
            f"New External Job Lead:\n\n"
            f"Title: {title}\n"
            f"Company: {company}\n"
            f"Location: {work_location} ({work_style})\n"
            f"Experience: {experience_required}\n"
            f"Skills: {skills_text}\n\n"
            f"Direct Apply Link:\n{clean_app_link}\n\n"
            f"LinkedIn Job Link:\n{job_link}\n"
        )
        send_email(subject, html_content, plain_text)

    # 2. Dispatch WhatsApp (if enabled)
    if globals().get("enable_whatsapp_job_notifications", False):
        w_phone = globals().get("whatsapp_phone", "")
        w_key = globals().get("whatsapp_callmebot_apikey", "")
        if w_phone and w_key:
            wa_message = (
                f"💼 *New External Job Lead!*\n\n"
                f"📌 *Role:* {title}\n"
                f"🏢 *Company:* {company}\n"
                f"📍 *Location:* {work_location} ({work_style})\n"
                f"🎯 *Experience:* {experience_required}\n\n"
                f"🌐 *Direct Apply:*\n{clean_app_link}\n\n"
                f"🔗 *LinkedIn:*\n{job_link}"
            )
            send_whatsapp(w_phone, w_key, wa_message)

    # 3. Direct 1-tap push notification to phone via ntfy
    topic = globals().get("ntfy_topic", "")
    if topic:
        url = f"https://ntfy.sh/{topic}"
        headers = {
            "Title": _encode_rfc2047(f"💼 External Job: {title}"),
            "Priority": "high",
            "Tags": "briefcase,globe_with_meridians",
            "Click": clean_app_link
        }
        ntfy_msg = f"{company} · {work_location}\nTap to open external application link directly!"
        try:
            requests.post(url, data=ntfy_msg.encode("utf-8"), headers=headers, timeout=10)
        except Exception:
            pass


def notify(title: str, message: str, priority: str = "default", tags: str = "robot", color: int = 3447003):
    '''
    Dispatch notification across all enabled channels (ntfy, Telegram, Discord).
    '''
    if not globals().get("enable_phone_notifications", True):
        return

    # 1. ntfy.sh (Push notification to phone)
    topic = globals().get("ntfy_topic", "")
    if topic:
        send_ntfy(topic, title, message, priority=priority, tags=tags)

    # 2. Telegram Bot
    t_token = globals().get("telegram_bot_token", "")
    t_chat = globals().get("telegram_chat_id", "")
    if t_token and t_chat:
        tg_text = f"<b>{title}</b>\n\n{message}"
        send_telegram(t_token, t_chat, tg_text)

    # 3. Discord
    d_webhook = globals().get("discord_webhook_url", "")
    if d_webhook:
        send_discord(d_webhook, title, message, color=color)


def notify_run_start(mode: str = "LinkedIn AI Bot"):
    '''
    Send notification when bot execution begins.
    '''
    now = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    title = "🚀 LinkedIn Bot Started"
    message = (
        f"Bot has started running on your machine!\n"
        f"• Mode: {mode}\n"
        f"• Time: {now}\n"
        f"• Status: Searching & Applying..."
    )
    print(f"\n[Notifier] Sending run start notification to phone...")
    notify(title, message, priority="default", tags="rocket,briefcase", color=3447003)


def notify_run_complete(easy_applied: int = 0, external: int = 0, failed: int = 0, skipped: int = 0, time_saved_secs: int = 0):
    '''
    Send notification when bot finishes applying.
    '''
    now = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    time_saved_mins = round(time_saved_secs / 60) if time_saved_secs else 0
    total_processed = easy_applied + external

    title = "✅ LinkedIn Bot Run Completed"
    message = (
        f"Job application run has finished!\n\n"
        f"📊 Summary:\n"
        f"• Easy Applied: {easy_applied}\n"
        f"• External Links: {external}\n"
        f"• Total Processed: {total_processed}\n"
        f"• Jobs Skipped: {skipped}\n"
        f"• Failed Jobs: {failed}\n"
        f"• Approx Time Saved: ~{time_saved_mins} mins\n"
        f"• Completed At: {now}"
    )
    print(f"\n[Notifier] Sending run complete notification to phone...")
    notify(title, message, priority="default", tags="white_check_mark,partying_face", color=3066993)


def notify_error(error_details: str):
    '''
    Send notification when an unhandled error or crash occurs.
    '''
    now = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    title = "⚠️ LinkedIn Bot Error"
    message = (
        f"An error occurred during bot execution!\n\n"
        f"• Time: {now}\n"
        f"• Details: {error_details[:500]}"
    )
    print(f"\n[Notifier] Sending error notification to phone...")
    notify(title, message, priority="high", tags="warning,x", color=15158332)


if __name__ == "__main__":
    print("Testing Notification System...")
    test_title = "🔔 Test Notification"
    test_msg = "This is a test notification from your LinkedIn AI Bot! If you see this on your phone, your notification system is working perfectly. 🚀"
    notify(test_title, test_msg, priority="high", tags="bell,test_tube", color=3447003)
    print("Test notification sent! Check your phone.")
