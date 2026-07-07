import requests

# ==========================
# تنظیمات
# ==========================
BOT_TOKEN = "8916345954:AAFafkj0CbiXga827gET2qSfUry_iAqpeyE"
CHAT_ID = "-1004226652444"


def get_weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=32.6546"
        "&longitude=51.6680"
        "&hourly=temperature_2m,wind_speed_10m,precipitation_probability"
        "&forecast_days=1"
        "&timezone=auto"
    )

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    data = response.json()

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

    return f"""
🏸 SMASH ZONE

🌤 وضعیت هوای فردا صبح | ناژوان

🌡 دما: {temp}°C
💨 باد: {wind} km/h ({wind_text})
🌧 احتمال بارش: {rain}%

🎯 شرایط بازی: {emoji} {status}

🔥 آماده‌ی بازی باشید!
"""


def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": text,
        },
        timeout=15,
    )

    print("========== DEBUG ==========")
    print("Status:", response.status_code)
    print("Response:", response.text)
    print("===========================")

    response.raise_for_status()


if __name__ == "__main__":
    print("Bot started...")

    try:
        message = get_weather()
        print("Weather received.")

        send_message(message)

        print("Done.")
    except Exception as e:
        print("ERROR:")
        print(e)
