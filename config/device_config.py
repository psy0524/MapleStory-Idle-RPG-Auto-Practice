import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일을 읽어들임

DEVICE_CONFIG = {
    "platformName": "Android",
    "platformVersion": os.getenv("PLATFORM_VERSION", "16"), # .env에서 가져옴
    "deviceName": os.getenv("DEVICE_NAME"),       # .env에서 가져옴
    "appPackage": os.getenv("APP_PACKAGE"),       # .env에서 가져옴
    "appActivity": os.getenv("APP_ACTIVITY"),     # .env에서 가져옴
    "noReset": True,
    "autoGrantPermissions": True,
}

APPIUM_SERVER = "http://127.0.0.1:4723"