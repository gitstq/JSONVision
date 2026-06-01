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

**🎨 轻量级终端JSON数据可视化与探索工具 | Zero-Dependency JSON Explorer**

*A lightweight, fast JSON visualization and exploration tool for the terminal*

[English](./README_en.md) | [演示](#-快速开始) | [功能](#-核心特性) | [安装](#-安装)

</div>

---

## 🎯 项目介绍

**JSONVision** 是一款专为开发者设计的**轻量级、零依赖**终端JSON数据可视化与探索工具。它能够将复杂的JSON数据结构以直观的**树形结构**展示，支持**路径查询**、**格式转换**、**统计分析**等实用功能，让您在终端中高效地理解和处理JSON数据。

### ✨ 核心价值

- 🚀 **极速响应**：零依赖设计，即装即用
- 🌳 **直观可视化**：树形结构展示，数据一目了然
- 🔍 **智能查询**：支持JSONPath语法，快速定位数据
- 🔄 **多格式转换**：JSON/YAML/TOML无缝互转
- 📊 **统计分析**：自动生成数据统计报告
- 💻 **跨平台兼容**：支持Linux/macOS/Windows

---

## 🎪 核心特性

### 🌳 树形可视化
```
📁 root
├── 📂 project
│   └── "JSONVision"
├── 📂 features
│   ├── 📂 [0]
│   │   ├── name: "树形可视化"
│   │   └── emoji: "🌳"
│   └── 📂 [1]
│       └── ...
```

### 🔍 路径查询
```bash
# 查询用户名称
jsonvision data.json --query "user.name"

# 搜索包含"id"的键
jsonvision data.json --search "id"
```

### 📊 统计信息
自动分析并显示：
- 数据类型（Object/Array）
- 键数量 / 数组长度
- 嵌套层级深度
- 数据分布情况

### 🔄 格式转换
```bash
# 格式化输出
jsonvision data.json --format

# 压缩JSON
jsonvision data.json --minify

# 转换为YAML
jsonvision data.json --yaml
```

---

## 🚀 快速开始

### 📥 安装

####方式一：pip安装（推荐）
```bash
pip install jsonvision
```

#### 方式二：从源码安装
```bash
git clone https://github.com/lobehub/JSONVision.git
cd JSONVision
pip install -e .
```

#### 方式三：直接使用Python运行
```bash
python jsonvision.py data.json
```

### 💡 基本使用

#### 1️⃣ 可视化JSON文件
```bash
jsonvision data.json
```

#### 2️⃣ 从stdin读取
```bash
cat data.json | jsonvision
echo '{"key": "value"}' | jsonvision
```

#### 3️⃣ 显示统计信息
```bash
jsonvision data.json --stats
```

#### 4️⃣ 查询路径
```bash
jsonvision data.json --query "user.name"
jsonvision data.json --query "items[0].title"
```

#### 5️⃣ 搜索键名
```bash
jsonvision data.json --search "id"
jsonvision data.json --search "email"
```

#### 6️⃣ 格式化输出
```bash
jsonvision data.json --format --indent 4
```

#### 7️⃣ 转换为YAML
```bash
jsonvision data.json --yaml > output.yaml
```

---

## 📖 详细使用指南

### 命令行参数

| 参数 | 说明 | 示例 |
|------|------|------|
| `file` | JSON文件路径 | `jsonvision data.json` |
| `--stats` | 显示统计信息 | `jsonvision data.json --stats` |
| `--tree` | 树形显示（默认） | `jsonvision data.json --tree` |
| `--query <path>` | 查询JSON路径 | `jsonvision data.json --query "a.b.c"` |
| `--search <key>` | 搜索键名 | `jsonvision data.json --search "name"` |
| `--format` | 格式化输出 | `jsonvision data.json --format` |
| `--minify` | 压缩JSON | `jsonvision data.json --minify` |
| `--yaml` | 转换为YAML | `jsonvision data.json --yaml` |
| `--indent <n>` | 格式化缩进 | `jsonvision data.json --indent 4` |
| `--version` | 显示版本 | `jsonvision --version` |

### 路径查询语法

```bash
# 查询对象键
jsonvision data.json --query "user.name"

# 查询数组元素
jsonvision data.json --query "items[0]"
jsonvision data.json --query "items[0].title"

# 查询嵌套路径
jsonvision data.json --query "a.b.c.d"
```

### 使用场景

#### 🎯 API调试
```bash
curl https://api.example.com/data | jsonvision
```

#### 🎯 配置文件查看
```bash
jsonvision config.json --stats
jsonvision config.json --search "port"
```

#### 🎯 日志分析
```bash
jq '.data' log.json | jsonvision --search "error"
```

---

## 💡 设计思路与迭代规划

### 🎨 设计理念

JSONVision 的设计遵循以下原则：

1. **轻量化优先**：零外部依赖，仅使用Python标准库 + Rich库
2. **交互友好**：Rich库提供美观的终端输出
3. **功能实用**：解决实际开发中的JSON处理痛点
4. **快速响应**：即时加载，无需等待

### 🔮 后续迭代计划

- [ ] v1.1: 添加交互式模式，支持键盘导航
- [ ] v1.2: 支持JSONSchema验证
- [ ] v1.3: 添加数据过滤和聚合功能
- [ ] v2.0: 支持大型JSON文件的流式处理
- [ ] v2.1: 添加插件系统，支持自定义转换器

### 🤝 贡献指南

欢迎提交Issue和Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建Pull Request

---

## 📦 打包与部署

### 🐍 Python环境要求

- Python 3.8 或更高版本
- Rich >= 13.0.0
- Click >= 8.0.0
- PyYAML >= 6.0

### 📦 安装依赖

```bash
pip install -r requirements.txt
```

### 🏃 本地运行

```bash
# 方式一：直接运行
python jsonvision.py data.json

# 方式二：安装后运行
pip install -e .
jsonvision data.json
```

### 🐳 Docker部署（可选）

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -e .
CMD ["jsonvision", "data.json"]
```

---

## 🆚 与同类工具对比

| 特性 | JSONVision | jq | jless | cat |
|------|------------|-----|-------|-----|
| 树形可视化 | ✅ | ❌ | ✅ | ❌ |
| 路径查询 | ✅ | ✅ | ✅ | ❌ |
| 格式转换 | ✅ | ❌ | ❌ | ❌ |
| 统计分析 | ✅ | ❌ | ❌ | ❌ |
| 零依赖 | ✅* | ❌ | ❌ | ✅ |
| 跨平台 | ✅ | ✅ | ✅ | ✅ |

> * 仅Python标准库 + Rich

---

## 📝 更新日志

### v1.0.0 (2026-06-01)
- 🎉 首次发布
- ✅ 树形可视化
- ✅ 路径查询
- ✅ 键名搜索
- ✅ 格式转换（JSON/YAML/TOML）
- ✅ 统计分析
- ✅ 多语言支持（中文/英文/日文/韩文/西班牙语）

---

## 🤝 开源协议

本项目采用 **MIT License** 开源协议。

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
