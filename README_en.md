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

**🎨 Lightweight Terminal JSON Data Visualization & Exploration Tool | Zero-Dependency JSON Explorer**

*A powerful yet lightweight tool for visualizing and exploring JSON data in your terminal*

[English](./README_en.md) | [Demo](#-quick-start) | [Features](#-features) | [Install](#-installation)

</div>

---

## 🎯 Project Introduction

**JSONVision** is a **lightweight, zero-dependency** terminal-based JSON data visualization and exploration tool designed for developers. It transforms complex JSON data structures into intuitive **tree views**, supports **path queries**, **format conversion**, and **statistical analysis**, enabling you to efficiently understand and process JSON data in the terminal.

### ✨ Core Value

- 🚀 **Lightning Fast**: Zero-dependency design, install and use instantly
- 🌳 **Intuitive Visualization**: Tree structure display, data at a glance
- 🔍 **Smart Query**: JSONPath syntax support for quick data location
- 🔄 **Multi-Format Conversion**: Seamless JSON/YAML/TOML conversion
- 📊 **Statistical Analysis**: Auto-generate data statistics reports
- 💻 **Cross-Platform**: Supports Linux/macOS/Windows

---

## 🎪 Core Features

### 🌳 Tree Visualization
```
📁 root
├── 📂 project
│   └── "JSONVision"
├── 📂 features
│   ├── 📂 [0]
│   │   ├── name: "Tree Visualization"
│   │   └── emoji: "🌳"
│   └── 📂 [1]
│       └── ...
```

### 🔍 Path Query
```bash
# Query username
jsonvision data.json --query "user.name"

# Search keys containing "id"
jsonvision data.json --search "id"
```

### 📊 Statistics
Auto-analyze and display:
- Data type (Object/Array)
- Key count / Array length
- Nesting depth
- Data distribution

### 🔄 Format Conversion
```bash
# Format output
jsonvision data.json --format

# Minify JSON
jsonvision data.json --minify

# Convert to YAML
jsonvision data.json --yaml
```

---

## 🚀 Quick Start

### 📥 Installation

#### Method 1: pip install (Recommended)
```bash
pip install jsonvision
```

#### Method 2: From source
```bash
git clone https://github.com/lobehub/JSONVision.git
cd JSONVision
pip install -e .
```

#### Method 3: Direct Python execution
```bash
python jsonvision.py data.json
```

### 💡 Basic Usage

#### 1️⃣ Visualize JSON file
```bash
jsonvision data.json
```

#### 2️⃣ Read from stdin
```bash
cat data.json | jsonvision
echo '{"key": "value"}' | jsonvision
```

#### 3️⃣ Show statistics
```bash
jsonvision data.json --stats
```

#### 4️⃣ Query path
```bash
jsonvision data.json --query "user.name"
jsonvision data.json --query "items[0].title"
```

#### 5️⃣ Search keys
```bash
jsonvision data.json --search "id"
jsonvision data.json --search "email"
```

#### 6️⃣ Format output
```bash
jsonvision data.json --format --indent 4
```

#### 7️⃣ Convert to YAML
```bash
jsonvision data.json --yaml > output.yaml
```

---

## 📖 Detailed Usage Guide

### Command Line Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `file` | JSON file path | `jsonvision data.json` |
| `--stats` | Show statistics | `jsonvision data.json --stats` |
| `--tree` | Tree display (default) | `jsonvision data.json --tree` |
| `--query <path>` | Query JSON path | `jsonvision data.json --query "a.b.c"` |
| `--search <key>` | Search keys | `jsonvision data.json --search "name"` |
| `--format` | Format output | `jsonvision data.json --format` |
| `--minify` | Minify JSON | `jsonvision data.json --minify` |
| `--yaml` | Convert to YAML | `jsonvision data.json --yaml` |
| `--indent <n>` | Format indent | `jsonvision data.json --indent 4` |
| `--version` | Show version | `jsonvision --version` |

### Path Query Syntax

```bash
# Query object key
jsonvision data.json --query "user.name"

# Query array element
jsonvision data.json --query "items[0]"
jsonvision data.json --query "items[0].title"

# Query nested path
jsonvision data.json --query "a.b.c.d"
```

### Use Cases

#### 🎯 API Debugging
```bash
curl https://api.example.com/data | jsonvision
```

#### 🎯 Config File Inspection
```bash
jsonvision config.json --stats
jsonvision config.json --search "port"
```

#### 🎯 Log Analysis
```bash
jq '.data' log.json | jsonvision --search "error"
```

---

## 💡 Design Philosophy & Roadmap

### 🎨 Design Principles

JSONVision follows these principles:

1. **Lightweight First**: Zero external dependencies, only Python stdlib + Rich
2. **User-Friendly**: Rich library provides beautiful terminal output
3. **Practical Features**: Solve real JSON processing pain points
4. **Fast Response**: Instant loading, no waiting

### 🔮 Roadmap

- [ ] v1.1: Add interactive mode with keyboard navigation
- [ ] v1.2: JSONSchema validation support
- [ ] v1.3: Data filtering and aggregation
- [ ] v2.0: Streaming processing for large JSON files
- [ ] v2.1: Plugin system for custom converters

### 🤝 Contributing

We welcome Issues and Pull Requests!

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Create Pull Request

---

## 📦 Packaging & Deployment

### 🐍 Python Requirements

- Python 3.8 or higher
- Rich >= 13.0.0
- Click >= 8.0.0
- PyYAML >= 6.0

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 🏃 Local Run

```bash
# Method 1: Direct run
python jsonvision.py data.json

# Method 2: After install
pip install -e .
jsonvision data.json
```

### 🐳 Docker Deployment (Optional)

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -e .
CMD ["jsonvision", "data.json"]
```

---

## 🆚 Comparison with Similar Tools

| Feature | JSONVision | jq | jless | cat |
|---------|------------|-----|-------|-----|
| Tree Visualization | ✅ | ❌ | ✅ | ❌ |
| Path Query | ✅ | ✅ | ✅ | ❌ |
| Format Conversion | ✅ | ❌ | ❌ | ❌ |
| Statistics | ✅ | ❌ | ❌ | ❌ |
| Zero Dependency | ✅* | ❌ | ❌ | ✅ |
| Cross-Platform | ✅ | ✅ | ✅ | ✅ |

> * Python stdlib + Rich only

---

## 📝 Changelog

### v1.0.0 (2026-06-01)
- 🎉 Initial release
- ✅ Tree visualization
- ✅ Path query
- ✅ Key search
- ✅ Format conversion (JSON/YAML/TOML)
- ✅ Statistical analysis
- ✅ Multi-language support (CN/TW/EN/JA/KO/ES)

---

## 🤝 License

This project is licensed under the **MIT License**.

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
