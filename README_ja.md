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

**🎨 軽量ターミナルJSONデータ可視化ツール | Zero-Dependency JSON Explorer**

*A lightweight, fast JSON visualization and exploration tool for the terminal*

[English](./README_en.md) | [デモ](#-クイックスタート) | [機能](#-コア機能) | [インストール](#-インストール)

</div>

---

## 🎯 プロジェクト紹介

**JSONVision** は開発者向けに設計された**軽量、ゼロ依存**ターミナルJSONデータ可視化ツールです。複雑なJSONデータ構造を直感的な**ツリー構造**で表示し、**パス查询**、**フォーマット変換**、**統計分析**などの実用的な機能をサポートし、ターミナルでJSONデータを効率的に理解和処理できます。

### ✨ コアバリュー

- 🚀 **超高速応答**：ゼロ依存設計、インストールしてすぐ使用可能
- 🌳 **直感的な可視化**：ツリー構造表示、データが一目でわかる
- 🔍 **スマートクエリ**：JSONPath構文サポートでデータを迅速に検索
- 🔄 **マルチフォーマット変換**：JSON/YAML/TOML的无缝変換
- 📊 **統計分析**：自動生成データ統計レポート
- 💻 **クロスプラットフォーム対応**：Linux/macOS/Windowsをサポート

---

## 🎪 コア機能

### 🌳 ツリー可視化
```
📁 root
├── 📂 project
│   └── "JSONVision"
├── 📂 features
│   ├── 📂 [0]
│   │   ├── name: "ツリー可視化"
│   │   └── emoji: "🌳"
│   └── 📂 [1]
│       └── ...
```

### 🔍 パスクエリ
```bash
# ユーザー名を查询
jsonvision data.json --query "user.name"

# "id"を含むキーを検索
jsonvision data.json --search "id"
```

### 📊 統計情報
自動分析と表示：
- データタイプ（Object/Array）
- キー数 / 配列長さ
- ネスト深度
- データ分布

### 🔄 フォーマット変換
```bash
# フォーマット出力
jsonvision data.json --format

# JSON圧縮
jsonvision data.json --minify

# YAMLに変換
jsonvision data.json --yaml
```

---

## 🚀 クイックスタート

### 📥 インストール

#### 方法1：pipインストール（推奨）
```bash
pip install jsonvision
```

#### 方法2：ソースからインストール
```bash
git clone https://github.com/lobehub/JSONVision.git
cd JSONVision
pip install -e .
```

#### 方法3：直接Pythonで実行
```bash
python jsonvision.py data.json
```

### 💡 基本使用

#### 1️⃣ JSONファイルを可視化
```bash
jsonvision data.json
```

#### 2️⃣ stdinから読み込み
```bash
cat data.json | jsonvision
echo '{"key": "value"}' | jsonvision
```

#### 3️⃣ 統計情報を表示
```bash
jsonvision data.json --stats
```

#### 4️⃣ パスを查询
```bash
jsonvision data.json --query "user.name"
jsonvision data.json --query "items[0].title"
```

#### 5️⃣ キーを検索
```bash
jsonvision data.json --search "id"
jsonvision data.json --search "email"
```

#### 6️⃣ フォーマット出力
```bash
jsonvision data.json --format --indent 4
```

#### 7️⃣ YAMLに変換
```bash
jsonvision data.json --yaml > output.yaml
```

---

## 📖 詳細な使い方ガイド

### コマンドライン引数

| 引数 | 説明 | 例 |
|------|------|------|
| `file` | JSONファイルパス | `jsonvision data.json` |
| `--stats` | 統計情報を表示 | `jsonvision data.json --stats` |
| `--tree` | ツリー表示（デフォルト） | `jsonvision data.json --tree` |
| `--query <path>` | JSONパスを查询 | `jsonvision data.json --query "a.b.c"` |
| `--search <key>` | キーを検索 | `jsonvision data.json --search "name"` |
| `--format` | フォーマット出力 | `jsonvision data.json --format` |
| `--minify` | JSONを圧縮 | `jsonvision data.json --minify` |
| `--yaml` | YAMLに変換 | `jsonvision data.json --yaml` |
| `--indent <n>` | フォーマットインデント | `jsonvision data.json --indent 4` |
| `--version` | バージョンを表示 | `jsonvision --version` |

### パスクエリ構文

```bash
# オブジェクトキーを查询
jsonvision data.json --query "user.name"

# 配列要素を查询
jsonvision data.json --query "items[0]"
jsonvision data.json --query "items[0].title"

# ネストされたパスを查询
jsonvision data.json --query "a.b.c.d"
```

### ユースケース

#### 🎯 APIデバッグ
```bash
curl https://api.example.com/data | jsonvision
```

#### 🎯 設定ファイル確認
```bash
jsonvision config.json --stats
jsonvision config.json --search "port"
```

#### 🎯 ログ分析
```bash
jq '.data' log.json | jsonvision --search "error"
```

---

## 💡 設計思想とロードマップ

### 🎨 設計原則

JSONVisionは次の原則に従います：

1. **軽量設計優先**：ゼロ外部依存、Python標準ライブラリ + Richのみ
2. **ユーザーフレンドリー**：Richライブラリが美しいターミナル出力を提供
3. **実用的な機能**：実際の開発におけるJSON処理の問題を解決
4. **高速応答**：インスタントロード、待ち時間なし

### 🔮 ロードマップ

- [ ] v1.1: キーボードナビゲーション付きインタラクティブモードを追加
- [ ] v1.2: JSONSchema検証サポート
- [ ] v1.3: データフィルタリングと集計を追加
- [ ] v2.0: 大規模JSONファイルのストリーミング処理をサポート
- [ ] v2.1: カスタムコンバーター用プラグインシステムを追加

### 🤝 コントリビュート

IssueとPull Requestを歓迎します！

1. リポジトリをFork
2. フィーチャーブランチを作成 (`git checkout -b feature/AmazingFeature`)
3. 変更をコミット (`git commit -m 'Add some AmazingFeature'`)
4. ブランチにプッシュ (`git push origin feature/AmazingFeature`)
5. Pull Requestを作成

---

## 📦 パッケージングとデプロイ

### 🐍 Python環境要件

- Python 3.8 以上
- Rich >= 13.0.0
- Click >= 8.0.0
- PyYAML >= 6.0

### 📥 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 🏃 ローカル実行

```bash
# 方法1：直接実行
python jsonvision.py data.json

# 方法2：インストール後
pip install -e .
jsonvision data.json
```

---

## 🆚 同類ツールとの比較

| 機能 | JSONVision | jq | jless | cat |
|------|------------|-----|-------|-----|
| ツリー可視化 | ✅ | ❌ | ✅ | ❌ |
| パスクエリ | ✅ | ✅ | ✅ | ❌ |
| フォーマット変換 | ✅ | ❌ | ❌ | ❌ |
| 統計分析 | ✅ | ❌ | ❌ | ❌ |
| ゼロ依存 | ✅* | ❌ | ❌ | ✅ |
| クロスプラットフォーム | ✅ | ✅ | ✅ | ✅ |

> * Python標準ライブラリ + Richのみ

---

## 📝 変更履歴

### v1.0.0 (2026-06-01)
- 🎉 初回リリース
- ✅ ツリー可視化
- ✅ パスクエリ
- ✅ キー検索
- ✅ フォーマット変換（JSON/YAML/TOML）
- ✅ 統計分析
- ✅ マルチ言語サポート（中国語/英語/日本語/韓国語/スペイン語）

---

## 🤝 ライセンス

このプロジェクトは **MIT License** のライセンスを使用しています。

---

<div align="center">

**Made with ❤️ by [lobehub](https://github.com/lobehub)**

⭐ GitHubでStar | 🐛 バグを報告 | 📖 ドキュメントを読む

</div>
