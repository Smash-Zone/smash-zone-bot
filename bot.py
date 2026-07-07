import requests
import traceback


# ==========================
# تنظیمات ربات
# ==========================

BOT_TOKEN = "8916345954:AAFafkj0CbiXga827gET2qSfUry_iAqpeyE"
CHAT_ID = "-1004226652444"


# ==========================
# تست ارتباط با تلگرام
# ==========================

def test_bot():

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"

    r = requests.get(url, timeout=15)

    print("=== Telegram Bot Test ===")
    print("Status:", r.status_code)
    print("Response:", r.text)


# ==========================
# گرفتن وضعیت هوا
# ==========================

def get_weather():

    print("Getting weather...")

    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=32.6546"
        "&longitude=51.6680"
        "&hourly=temperature_2m,wind_speed_10m,precipitation_probability"
        "&forecast_days=1"
        "&timezone=auto"
    )

    r = requests.get(url, timeout=15)
    r.raise_for_status()

    data = r.json()

    temp = data["hourly"]["temperature_2m"][6]
    wind = data["hourly"]["wind_speed_10m"][6]
    rain = data["hourly"]["precipitation_probability"][6]


    if wind < 5:
        wind_text = "ساکن"
        status = "عالی"
        emoji = "✅"

    elif wind < 15:
        wind_text = "نسیم ملایم"
        status = "مناسب"
        emoji = "👍"

    elif wind < 30:
        wind_text = "باد نسبتاً شدید"
        status = "متوسط"
        emoji = "⚠️"

    else:
        wind_text = "باد شدید"
        status = "نامناسب"
        emoji = "❌"


    message = f"""
🏸 SMASH ZONE

🌤 وضعیت هوای فردا صبح | ناژوان

🌡 دما: {temp}°C
💨 باد: {wind} km/h ({wind_text})
🌧 احتمال بارش: {rain}%

🎯 شرایط بازی: {emoji} {status}

🔥 آماده‌ی بازی باشید!
"""

    return message



# ==========================
# ارسال پیام
# ==========================

def send_message(text):

    print("Sending message...")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


    r = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": text
        },
        timeout=15
    )


    print("=== Send Message Result ===")
    print("Status:", r.status_code)
    print("Response:", r.text)



# ==========================
# شروع برنامه
# ==========================

if __name__ == "__main__":

    print("BOT STARTED")

    try:

        test_bot()

        msg = get_weather()

        print(msg)

        send_message(msg)

        print("FINISHED")


    except Exception:

        print("ERROR FOUND")
        traceback.print_exc()
