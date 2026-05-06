# 🍁 메이플 키우기 QA 자동화 포트폴리오

넥슨 모바일 게임 **메이플 키우기**를 대상으로 한 Android QA 자동화 프로젝트입니다.  
실제 출시된 앱을 대상으로 Appium 기반 UI 자동화, 화면 검증, 성능 측정을 구현합니다.

---

## 📌 프로젝트 목적

- 실제 출시된 게임 앱을 대상으로 QA 자동화 실습
- Appium 기반 모바일 UI 자동화 구현
- 게임 QA 엔지니어 취업을 위한 포트폴리오 제작

---

## 🛠️ 기술 스택

| 목적 | 도구 |
|------|------|
| 모바일 UI 자동화 | Appium 2.x + Python |
| 화면 이미지 검증 | OpenCV |
| 성능 측정 | Android adb |
| 테스트 프레임워크 | pytest |
| 리포트 | Allure Report |
| 환경변수 관리 | python-dotenv |

---

## 📱 테스트 환경

| 항목 | 내용 |
|------|------|
| 기기 | Samsung Galaxy S23 (SM-S911N) |
| Android 버전 | 16 |
| 대상 앱 | 메이플 키우기 (com.nexon.ma) |
| OS | Windows 11 |

---

## 🧪 테스트 시나리오

| 단계 | 파일 | 내용 | 상태 |
|------|------|------|------|
| 1단계 | `test_01_launch.py` | 앱 정상 실행 및 스크린샷 저장 | ✅ 완료 |
| 2단계 | `test_02_ui_navigation.py` | UI 버튼 클릭 및 화면 이동 | 🔜 예정 |
| 3단계 | `test_03_farming_loop.py` | 반복 파밍 동작 자동화 | 🔜 예정 |
| 4단계 | `test_04_performance.py` | FPS / 메모리 성능 측정 | 🔜 예정 |

---

## 📁 프로젝트 구조

```
maple-qa/
├── config/
│   └── device_config.py        ← 기기 설정 (.env에서 읽어옴)
├── tests/
│   ├── test_01_launch.py       ← 앱 실행 검증 ✅
│   ├── test_02_ui_navigation.py ← UI 클릭/화면 이동 (예정)
│   ├── test_03_farming_loop.py  ← 반복 파밍 자동화 (예정)
│   └── test_04_performance.py   ← 성능 측정 (예정)
├── utils/
│   ├── adb_helper.py           ← adb 명령어 유틸
│   └── image_compare.py        ← 이미지 비교 유틸
├── screenshots/                ← 자동 저장 스크린샷
├── reports/                    ← Allure 리포트
├── .env.example                ← 환경변수 샘플
├── conftest.py                 ← pytest 공통 설정
├── requirements.txt            ← 패키지 목록
└── README.md
```

---

## ▶️ 실행 방법

### 1. 패키지 설치
```bash
pip install -r requirements.txt
```

### 2. 환경변수 설정
`.env.example` 을 복사해서 `.env` 파일 생성 후 본인 기기 정보 입력:
```bash
DEVICE_NAME=YOUR_DEVICE_ID       # adb devices 로 확인
PLATFORM_VERSION=YOUR_ANDROID_VERSION
```

### 3. Appium 서버 실행
```bash
appium
```

### 4. 테스트 실행
```bash
# 전체 실행
python -m pytest tests/ -v

# 특정 테스트만
python -m pytest tests/test_01_launch.py -v
```

---

## ✅ 1단계 테스트 결과

```
PASSED tests/test_01_launch.py::test_app_launch
PASSED tests/test_01_launch.py::test_screenshot
```

앱 정상 실행 확인 및 스크린샷 자동 저장까지 완료했습니다.

---

## 🐛 발견한 버그

| ID | 증상 | 재현 조건 | 심각도 |
|----|------|-----------|--------|
| - | 작성 예정 | - | - |