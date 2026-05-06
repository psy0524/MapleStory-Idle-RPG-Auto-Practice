import time
import pytest
from utils.image_compare import find_button

BTN_CHARACTER = "screenshots/buttons/btn_character.png"
BTN_EQUIPMENT = "screenshots/buttons/btn_equipment.png"

def test_click_character_tab(driver):
    time.sleep(1)
    # 이제 find_button이 더 정밀하게 작동합니다.
    result = find_button(driver, BTN_CHARACTER, threshold=0.85)

    assert result is not None, "❌ 캐릭터 버튼을 찾지 못했습니다!"

    x, y = result
    driver.tap([(x, y)])
    print(f"✅ 캐릭터 탭 클릭! 위치: ({x}, {y})")

    time.sleep(1)
    driver.save_screenshot("screenshots/after_character_tab.png")

def test_click_equipment_tab(driver):
    time.sleep(1)
    result = find_button(driver, BTN_EQUIPMENT, threshold=0.85)

    assert result is not None, "❌ 장비 버튼을 찾지 못했습니다!"

    x, y = result
    driver.tap([(x, y)])
    print(f"✅ 장비 탭 클릭! 위치: ({x}, {y})")

    time.sleep(1)
    driver.save_screenshot("screenshots/after_equipment_tab.png")