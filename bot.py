import requests
import traceback

print("HELLO FROM BOT.PY")


BOT_TOKEN = "8916345954:AAFafkj0CbiXga827gET2qSfUry_iAqpeyE"
CHAT_ID = "-1004226652444"


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

    response = requests.get(url, timeout=20)
    print("Weather status:", response.status_code)

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



def send_message(message):

    print("Sending message...")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        },
        timeout=20
    )

    print("Telegram status:", response.status_code)
    print("Telegram response:", response.text)



if __name__ == "__main__":

    print("BOT STARTED")

    try:
        text = get_weather()

        print(text)

        send_message(text)

        print("DONE")

    except Exception:
        print("ERROR")
        traceback.print_exc()
