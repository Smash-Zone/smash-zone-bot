import requests
from datetime import datetime

BOT_TOKEN = "8916345954:AAFLOPXI4Yp97RYoZZInQ8SciQ0-EDjgJEA"
CHAT_ID = "6888066102"

def get_weather():
    # اصفهان (Isfahan) - Open-Meteo API
    url = "https://api.open-meteo.com/v1/forecast?latitude=32.6546&longitude=51.6680&hourly=temperature_2m,wind_speed_10m,precipitation_probability,weathercode&forecast_days=1&timezone=auto"
    data = requests.get(url).json()

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

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

if __name__ == "__main__":
    msg = get_weather()
    send_message(msg)
