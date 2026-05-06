import time

def test_app_is_running(driver):
    """앱이 현재 실행 중인지 확인 (실행 중 아니면 실패)"""
    current_package = driver.current_package
    print(f"\n현재 실행 중인 앱: {current_package}")

    assert current_package == "com.nexon.ma", \
        f"❌ 앱이 실행 중이 아닙니다! (현재 앱: {current_package})\n" \
        f"👉 안드로이드 스마트폰에서 앱을 먼저 실행해주세요."

    print("✅ 앱 실행 중 확인!")

def test_screenshot(driver):
    """현재 화면 스크린샷 저장"""
    # 앱 실행 중인지 먼저 체크
    current_package = driver.current_package
    assert current_package == "com.nexon.ma", \
        f"❌ 앱이 실행 중이 아닙니다!"

    time.sleep(2)
    driver.save_screenshot("screenshots/launch_screen.png")
    print("✅ 스크린샷 저장 완료")