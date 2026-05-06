import cv2
import numpy as np

def find_button(driver, button_img_path, threshold=0.8):
    """
    현재 화면에서 버튼 이미지를 찾아 좌표 반환
    """
    # 1. 화면 캡처 및 전처리
    screenshot = driver.get_screenshot_as_png()
    screen_np = np.frombuffer(screenshot, np.uint8)
    screen_img = cv2.imdecode(screen_np, cv2.IMREAD_COLOR)

    # 2. 버튼 이미지 로드 (투명도 정보 유지)
    button_img = cv2.imread(button_img_path, cv2.IMREAD_UNCHANGED)
    if button_img is None:
        raise FileNotFoundError(f"버튼 이미지를 찾을 수 없습니다: {button_img_path}")

    # 투명 채널이 있다면 제거 (3채널 BGR로 변환)
    if button_img.shape[2] == 4:
        button_img = cv2.cvtColor(button_img, cv2.COLOR_BGRA2BGR)

    # 3. 크기 검증 (템플릿이 화면보다 크면 에러 발생 방지)
    if button_img.shape[0] > screen_img.shape[0] or button_img.shape[1] > screen_img.shape[1]:
        print(f"⚠️ 경고: 버튼 이미지가 화면보다 큽니다! ({button_img_path})")
        return None

    # 4. 템플릿 매칭 수행
    result = cv2.matchTemplate(screen_img, button_img, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    print(f"🔍 버튼 검색 결과: {button_img_path} | 유사도: {max_val:.2%}")

    if max_val >= threshold:
        # 버튼 중앙 좌표 계산
        h, w = button_img.shape[:2]
        center_x = max_loc[0] + w // 2
        center_y = max_loc[1] + h // 2
        return (center_x, center_y)
    
    return None