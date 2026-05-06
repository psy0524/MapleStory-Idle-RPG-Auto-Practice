import pytest
from appium.webdriver.common.appiumby import AppiumBy
import time

def test_app_launch(driver):
    """메이플 키우기 앱이 정상적으로 실행되는지 확인"""
    time.sleep(3)  # 앱 로딩 대기
    
    # 현재 앱 패키지 확인
    current_package = driver.current_package
    print(f"\n현재 실행 중인 앱: {current_package}")
    
    # 메이플 키우기 앱이 맞는지 검증
    assert current_package == "com.nexon.ma", \
        f"앱 실행 실패! 현재 패키지: {current_package}"
    
    print("✅ 앱 정상 실행 확인!")

def test_screenshot(driver):
    """앱 화면 스크린샷 저장"""
    time.sleep(2)
    driver.save_screenshot("screenshots/launch_screen.png")
    print("✅ 스크린샷 저장 완료: screenshots/launch_screen.png")