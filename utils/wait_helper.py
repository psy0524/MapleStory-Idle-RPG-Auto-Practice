import time
import cv2
import numpy as np

def wait_for_screen_stable(driver, timeout=60, interval=2, threshold=500000):
    """
    화면이 안정화(로딩 완료)될 때까지 대기

    timeout  : 최대 대기 시간 (초)
    interval : 화면 비교 간격 (초)
    threshold: 변화량 기준값 (낮을수록 민감)
    """
    prev_screenshot = None
    start_time = time.time()

    while time.time() - start_time < timeout:
        current = driver.get_screenshot_as_png()
        current_np = np.frombuffer(current, np.uint8)
        current_img = cv2.imdecode(current_np, cv2.IMREAD_GRAYSCALE)

        if prev_screenshot is not None:
            diff = cv2.absdiff(prev_screenshot, current_img)
            diff_score = np.sum(diff)
            print(f"화면 변화량: {diff_score}")

            if diff_score < threshold:
                print("✅ 화면 안정화 완료!")
                return True

        prev_screenshot = current_img
        time.sleep(interval)

    print("⚠️ 타임아웃: 최대 대기시간 초과")
    return False