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

# Try loading settings safely
try:
    from config.settings import (
        enable_phone_notifications,
        ntfy_topic,
        telegram_bot_token,
        telegram_chat_id,
        discord_webhook_url
    )
except ImportError:
    enable_phone_notifications = True
    ntfy_topic = "omkar_linkedin_bot_alerts"
    telegram_bot_token = ""
    telegram_chat_id = ""
    discord_webhook_url = ""


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
