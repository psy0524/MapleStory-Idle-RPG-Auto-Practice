import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일 자동으로 읽어옴

DEVICE_CONFIG = {
    "platformName": "Android",
    "platformVersion": os.getenv("PLATFORM_VERSION", "16"),
    "deviceName": os.getenv("DEVICE_NAME", "YOUR_DEVICE_ID"),
    "appPackage": "com.nexon.ma",
    "appActivity": "com.nexon.ma.MainActivity",
    "noReset": True,
    "autoGrantPermissions": True,
}

APPIUM_SERVER = "http://127.0.0.1:4723"