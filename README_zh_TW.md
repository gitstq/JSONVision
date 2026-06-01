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

**🎨 輕量級終端JSON數據可視化與探索工具 | Zero-Dependency JSON Explorer**

*A lightweight, fast JSON visualization and exploration tool for the terminal*

[English](./README_en.md) | [演示](#-快速開始) | [功能](#-核心特性) | [安裝](#-安裝)

</div>

---

## 🎯 項目介紹

**JSONVision** 是一款專為開發者設計的**輕量級、零依賴**終端JSON數據可視化與探索工具。它能夠將複雜的JSON數據結構以直觀的**樹形結構**展示，支持**路徑查詢**、**格式轉換**、**統計分析**等實用功能，讓您在終端中高效地理解和處理JSON數據。

### ✨ 核心價值

- 🚀 **極速響應**：零依賴設計，即裝即用
- 🌳 **直觀可視化**：樹形結構展示，數據一目了然
- 🔍 **智能查詢**：支持JSONPath語法，快速定位數據
- 🔄 **多格式轉換**：JSON/YAML/TOML無縫互轉
- 📊 **統計分析**：自動生成數據統計報告
- 💻 **跨平台兼容**：支持Linux/macOS/Windows

---

## 🎪 核心特性

### 🌳 樹形可視化
```
📁 root
├── 📂 project
│   └── "JSONVision"
├── 📂 features
│   ├── 📂 [0]
│   │   ├── name: "樹形可視化"
│   │   └── emoji: "🌳"
│   └── 📂 [1]
│       └── ...
```

### 🔍 路徑查詢
```bash
# 查詢用戶名稱
jsonvision data.json --query "user.name"

# 搜索包含"id"的鍵
jsonvision data.json --search "id"
```

### 📊 統計信息
自動分析並顯示：
- 數據類型（Object/Array）
- 鍵數量 / 數組長度
- 嵌套層級深度
- 數據分布情況

### 🔄 格式轉換
```bash
# 格式化輸出
jsonvision data.json --format

# 壓縮JSON
jsonvision data.json --minify

# 轉換為YAML
jsonvision data.json --yaml
```

---

## 🚀 快速開始

### 📥 安裝

#### 方式一：pip安裝（推薦）
```bash
pip install jsonvision
```

#### 方式二：從源碼安裝
```bash
git clone https://github.com/lobehub/JSONVision.git
cd JSONVision
pip install -e .
```

#### 方式三：直接使用Python運行
```bash
python jsonvision.py data.json
```

### 💡 基本使用

#### 1️⃣ 可視化JSON文件
```bash
jsonvision data.json
```

#### 2️⃣ 從stdin讀取
```bash
cat data.json | jsonvision
echo '{"key": "value"}' | jsonvision
```

#### 3️⃣ 顯示統計信息
```bash
jsonvision data.json --stats
```

#### 4️⃣ 查詢路徑
```bash
jsonvision data.json --query "user.name"
jsonvision data.json --query "items[0].title"
```

#### 5️⃣ 搜索鍵名
```bash
jsonvision data.json --search "id"
jsonvision data.json --search "email"
```

#### 6️⃣ 格式化輸出
```bash
jsonvision data.json --format --indent 4
```

#### 7️⃣ 轉換為YAML
```bash
jsonvision data.json --yaml > output.yaml
```

---

## 📖 詳細使用指南

### 命令列參數

| 參數 | 說明 | 示例 |
|------|------|------|
| `file` | JSON文件路徑 | `jsonvision data.json` |
| `--stats` | 顯示統計信息 | `jsonvision data.json --stats` |
| `--tree` | 樹形顯示（預設） | `jsonvision data.json --tree` |
| `--query <path>` | 查詢JSON路徑 | `jsonvision data.json --query "a.b.c"` |
| `--search <key>` | 搜索鍵名 | `jsonvision data.json --search "name"` |
| `--format` | 格式化輸出 | `jsonvision data.json --format` |
| `--minify` | 壓縮JSON | `jsonvision data.json --minify` |
| `--yaml` | 轉換為YAML | `jsonvision data.json --yaml` |
| `--indent <n>` | 格式化縮進 | `jsonvision data.json --indent 4` |
| `--version` | 顯示版本 | `jsonvision --version` |

### 路徑查詢語法

```bash
# 查詢對象鍵
jsonvision data.json --query "user.name"

# 查詢數組元素
jsonvision data.json --query "items[0]"
jsonvision data.json --query "items[0].title"

# 查詢嵌套路徑
jsonvision data.json --query "a.b.c.d"
```

### 使用場景

#### 🎯 API調試
```bash
curl https://api.example.com/data | jsonvision
```

#### 🎯 配置文件查看
```bash
jsonvision config.json --stats
jsonvision config.json --search "port"
```

#### 🎯 日誌分析
```bash
jq '.data' log.json | jsonvision --search "error"
```

---

## 💡 設計思路與迭代規劃

### 🎨 設計理念

JSONVision 的設計遵循以下原則：

1. **輕量化優先**：零外部依賴，僅使用Python標準庫 + Rich庫
2. **交互友好**：Rich庫提供美觀的終端輸出
3. **功能實用**：解決實際開發中的JSON處理痛點
4. **快速響應**：即時加載，無需等待

### 🔮 後續迭代計劃

- [ ] v1.1: 添加交互式模式，支持鍵盤導航
- [ ] v1.2: 支持JSONSchema驗證
- [ ] v1.3: 添加數據過濾和聚合功能
- [ ] v2.0: 支持大型JSON文件的流式處理
- [ ] v2.1: 添加插件系統，支持自定義轉換器

### 🤝 貢獻指南

歡迎提交Issue和Pull Request！

1. Fork 本倉庫
2. 創建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送至分支 (`git push origin feature/AmazingFeature`)
5. 創建Pull Request

---

## 📦 包裝與部署

### 🐍 Python環境要求

- Python 3.8 或更高版本
- Rich >= 13.0.0
- Click >= 8.0.0
- PyYAML >= 6.0

### 📦 安裝依賴

```bash
pip install -r requirements.txt
```

### 🏃 本地運行

```bash
# 方式一：直接運行
python jsonvision.py data.json

# 方式二：安裝後運行
pip install -e .
jsonvision data.json
```

### 🐳 Docker部署（可選）

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -e .
CMD ["jsonvision", "data.json"]
```

---

## 🆚 與同類工具對比

| 特性 | JSONVision | jq | jless | cat |
|------|------------|-----|-------|-----|
| 樹形可視化 | ✅ | ❌ | ✅ | ❌ |
| 路徑查詢 | ✅ | ✅ | ✅ | ❌ |
| 格式轉換 | ✅ | ❌ | ❌ | ❌ |
| 統計分析 | ✅ | ❌ | ❌ | ❌ |
| 零依賴 | ✅* | ❌ | ❌ | ✅ |
| 跨平台 | ✅ | ✅ | ✅ | ✅ |

> * 僅Python標準庫 + Rich

---

## 📝 更新日誌

### v1.0.0 (2026-06-01)
- 🎉 首次發布
- ✅ 樹形可視化
- ✅ 路徑查詢
- ✅ 鍵名搜索
- ✅ 格式轉換（JSON/YAML/TOML）
- ✅ 統計分析
- ✅ 多語言支持（中文/英文/日文/韓文/西班牙語）

---

## 🤝 開源協議

本項目採用 **MIT License** 開源協議。

```
MIT License

Copyright (c) 2026 lobehub

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">

**Made with ❤️ by [lobehub](https://github.com/lobehub)**

⭐ Star us on GitHub | 🐛 Report a Bug | 📖 Read the Docs

</div>
