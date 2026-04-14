  GNU nano 8.4                                                           alert_button.py
import time
import RPi.GPIO as GPIO
import requests

BOT_TOKEN = "8776704562:AAFdFv0q8NsoGIUQ2WiFoIY7cmGnkfcymFM"
CHAT_ID = "8783877386"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot8776704562:AAFdFv0q8NsoGIUQ2WiFoIY7cmGnkfcymFM/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, data=payload)
        print(response.json())
    except Exception as e:
        print("Error:", e)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False

while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        print("Someone pressed the alert button!")
        send_telegram_message("🚨 Alert! Button pressed!")
        button_pressed = True

    elif GPIO.input(7) == GPIO.LOW:
        button_pressed = False

    time.sleep(0.1)
