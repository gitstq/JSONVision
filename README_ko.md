# 🌐 Language
- [🇨🇳 简体中文](README.md)
- [🇭🇰 繁體中文](README_zh_TW.md)
- [🇺🇸 English](README_en.md)
- [🇯🇵 日本語](README_ja.md)
- [🇰🇷 한국어](README_ko.md)
- [🇪🇸 Español](README_es.md)

---

# 📊 JSONVision

<div align="center">

![JSONVision](https://img.shields.io/badge/JSONVision-v1.0.0-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/lobehub/JSONVision?style=for-the-badge)

**🎨 경량 터미널 JSON 데이터 시각화 도구 | Zero-Dependency JSON Explorer**

*A lightweight, fast JSON visualization and exploration tool for the terminal*

[English](./README_en.md) | [데모](#-빠른-시작) | [기능](#-핵심-기능) | [설치](#-설치)

</div>

---

## 🎯 프로젝트 소개

**JSONVision**은 개발자를 위해 설계된 **경량,ゼロ依存** 터미널 JSON 데이터 시각화 및 탐색 도구입니다. 복잡한 JSON 데이터 구조를 직관적인 **트리 구조**로 표시하고, **경로 쿼리**, **형식 변환**, **통계 분석** 등의 실용적인 기능을 지원하여 터미널에서 JSON 데이터를 효율적으로 이해하고 처리할 수 있습니다.

### ✨ 핵심 가치

- 🚀 **초고속 응답**: 제로 의존성 설계, 설치즉시 사용
- 🌳 **직관적 시각화**: 트리 구조 표시, 데이터 한눈에 파악
- 🔍 **스마트 쿼리**: JSONPath 구문 지원으로 데이터 신속 검색
- 🔄 **멀티 포맷 변환**: JSON/YAML/TOML 무결점 변환
- 📊 **통계 분석**: 자동 생성 데이터 통계 보고서
- 💻 **크로스 플랫폼**: Linux/macOS/Windows 지원

---

## 🎪 핵심 기능

### 🌳 트리 시각화
```
📁 root
├── 📂 project
│   └── "JSONVision"
├── 📂 features
│   ├── 📂 [0]
│   │   ├── name: "트리 시각화"
│   │   └── emoji: "🌳"
│   └── 📂 [1]
│       └── ...
```

### 🔍 경로 쿼리
```bash
# 사용자 이름 쿼리
jsonvision data.json --query "user.name"

# "id"를 포함하는 키 검색
jsonvision data.json --search "id"
```

### 📊 통계 정보
자동 분석 및 표시:
- 데이터 타입 (Object/Array)
- 키 수 / 배열 길이
- 중첩 깊이
- 데이터 분포

### 🔄 포맷 변환
```bash
# 포맷 출력
jsonvision data.json --format

# JSON 압축
jsonvision data.json --minify

# YAML로 변환
jsonvision data.json --yaml
```

---

## 🚀 빠른 시작

### 📥 설치

#### 방법1: pip 설치 (권장)
```bash
pip install jsonvision
```

#### 방법2: 소스에서 설치
```bash
git clone https://github.com/lobehub/JSONVision.git
cd JSONVision
pip install -e .
```

#### 방법3: 직접 Python으로 실행
```bash
python jsonvision.py data.json
```

### 💡 기본 사용

#### 1️⃣ JSON 파일 시각화
```bash
jsonvision data.json
```

#### 2️⃣ stdin에서 읽기
```bash
cat data.json | jsonvision
echo '{"key": "value"}' | jsonvision
```

#### 3️⃣ 통계 정보 표시
```bash
jsonvision data.json --stats
```

#### 4️⃣ 경로 쿼리
```bash
jsonvision data.json --query "user.name"
jsonvision data.json --query "items[0].title"
```

#### 5️⃣ 키 검색
```bash
jsonvision data.json --search "id"
jsonvision data.json --search "email"
```

#### 6️⃣ 포맷 출력
```bash
jsonvision data.json --format --indent 4
```

#### 7️⃣ YAML로 변환
```bash
jsonvision data.json --yaml > output.yaml
```

---

## 📖 자세한 사용 가이드

### 명령줄 인자

| 인자 | 설명 | 예시 |
|------|------|------|
| `file` | JSON 파일 경로 | `jsonvision data.json` |
| `--stats` | 통계 정보 표시 | `jsonvision data.json --stats` |
| `--tree` | 트리 표시 (기본값) | `jsonvision data.json --tree` |
| `--query <path>` | JSON 경로 쿼리 | `jsonvision data.json --query "a.b.c"` |
| `--search <key>` | 키 검색 | `jsonvision data.json --search "name"` |
| `--format` | 포맷 출력 | `jsonvision data.json --format` |
| `--minify` | JSON 압축 | `jsonvision data.json --minify` |
| `--yaml` | YAML로 변환 | `jsonvision data.json --yaml` |
| `--indent <n>` | 포맷 들여쓰기 | `jsonvision data.json --indent 4` |
| `--version` | 버전 표시 | `jsonvision --version` |

### 경로 쿼리 구문

```bash
# 객체 키 쿼리
jsonvision data.json --query "user.name"

# 배열 요소 쿼리
jsonvision data.json --query "items[0]"
jsonvision data.json --query "items[0].title"

# 중첩 경로 쿼리
jsonvision data.json --query "a.b.c.d"
```

### 사용 사례

#### 🎯 API 디버깅
```bash
curl https://api.example.com/data | jsonvision
```

#### 🎯 설정 파일 확인
```bash
jsonvision config.json --stats
jsonvision config.json --search "port"
```

#### 🎯 로그 분석
```bash
jq '.data' log.json | jsonvision --search "error"
```

---

## 💡 설계 철학 및 로드맵

### 🎨 설계 원칙

JSONVision은 다음 원칙을 따릅니다:

1. **경량 우선**: 제로 외부 의존성, Python 표준 라이브러리 + Rich만 사용
2. **사용자 친화적**: Rich 라이브러리가 아름다운 터미널 출력 제공
3. **실용적 기능**: 실제 개발에서의 JSON 처리 문제 해결
4. **빠른 응답**: 즉각적 로딩, 대기 시간 없음

### 🔮 로드맵

- [ ] v1.1: 키보드 내비게이션이 있는 대화형 모드 추가
- [ ] v1.2: JSONSchema 검증 지원
- [ ] v1.3: 데이터 필터링 및 집계 추가
- [ ] v2.0: 대규모 JSON 파일의 스트리밍 처리 지원
- [ ] v2.1: 사용자 정의 변환기용 플러그인 시스템 추가

### 🤝 기여

이슈와 풀 리퀘스트를 환영합니다!

1. 리포지토리를 Fork
2. 기능 브랜치 생성 (`git checkout -b feature/AmazingFeature`)
3. 변경 사항 커밋 (`git commit -m 'Add some AmazingFeature'`)
4. 브랜치에 푸시 (`git push origin feature/AmazingFeature`)
5. 풀 리퀘스트 생성

---

## 📦 패키징 및 배포

### 🐍 Python 환경 요구사항

- Python 3.8 이상
- Rich >= 13.0.0
- Click >= 8.0.0
- PyYAML >= 6.0

### 📥 의존성 설치

```bash
pip install -r requirements.txt
```

### 🏃 로컬 실행

```bash
# 방법1: 직접 실행
python jsonvision.py data.json

# 방법2: 설치 후
pip install -e .
jsonvision data.json
```

---

## 🆚 유사 도구 비교

| 기능 | JSONVision | jq | jless | cat |
|------|------------|-----|-------|-----|
| 트리 시각화 | ✅ | ❌ | ✅ | ❌ |
| 경로 쿼리 | ✅ | ✅ | ✅ | ❌ |
| 포맷 변환 | ✅ | ❌ | ❌ | ❌ |
| 통계 분석 | ✅ | ❌ | ❌ | ❌ |
| 제로 의존성 | ✅* | ❌ | ❌ | ✅ |
| 크로스 플랫폼 | ✅ | ✅ | ✅ | ✅ |

> * Python 표준 라이브러리 + Rich만

---

## 📝 변경 로그

### v1.0.0 (2026-06-01)
- 🎉 첫 번째 출시
- ✅ 트리 시각화
- ✅ 경로 쿼리
- ✅ 키 검색
- ✅ 포맷 변환 (JSON/YAML/TOML)
- ✅ 통계 분석
- ✅ 다국어 지원 (중국어/영어/일본어/한국어/스페인어)

---

## 🤝 라이선스

이 프로젝트는 **MIT 라이선스**를 사용합니다.

---

<div align="center">

**Made with ❤️ by [lobehub](https://github.com/lobehub)**

⭐ GitHub에서 Star | 🐛 버그 신고 | 📖 문서 읽기

</div>
