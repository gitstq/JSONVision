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

**🎨 Herramienta de Visualización y Exploración de Datos JSON Ligera para Terminal | Zero-Dependency JSON Explorer**

*A lightweight, fast JSON visualization and exploration tool for the terminal*

[English](./README_en.md) | [Demo](#-inicio-rápido) | [Características](#-características-principales) | [Instalación](#-instalación)

</div>

---

## 🎯 Introducción del Proyecto

**JSONVision** es una herramienta de visualización y exploración de datos JSON **ligera, sin dependencias** diseñada para desarrolladores. Transforma estructuras de datos JSON complejas en **vistas de árbol** intuitivas, soporta **consultas de ruta**, **conversión de formato** y **análisis estadístico**, permitiéndote entender y procesar datos JSON eficientemente en la terminal.

### ✨ Valor Central

- 🚀 **Ultra Rápido**: Diseño sin dependencias, instálalo y úsalo al instante
- 🌳 **Visualización Intuitiva**: Estructura de árbol, datos de un vistazo
- 🔍 **Consulta Inteligente**: Soporte de sintaxis JSONPath para localización rápida
- 🔄 **Conversión Multi-Formato**: Conversión perfecta JSON/YAML/TOML
- 📊 **Análisis Estadístico**: Informes de estadísticas de datos generados automáticamente
- 💻 **Multiplataforma**: Soporta Linux/macOS/Windows

---

## 🎪 Características Principales

### 🌳 Visualización de Árbol
```
📁 root
├── 📂 project
│   └── "JSONVision"
├── 📂 features
│   ├── 📂 [0]
│   │   ├── name: "Visualización de Árbol"
│   │   └── emoji: "🌳"
│   └── 📂 [1]
│       └── ...
```

### 🔍 Consulta de Ruta
```bash
# Consultar nombre de usuario
jsonvision data.json --query "user.name"

# Buscar claves que contengan "id"
jsonvision data.json --search "id"
```

### 📊 Estadísticas
Análisis automático y visualización:
- Tipo de dato (Object/Array)
- Cantidad de claves / Longitud del array
- Profundidad de anidamiento
- Distribución de datos

### 🔄 Conversión de Formato
```bash
# Formatear salida
jsonvision data.json --format

# Minificar JSON
jsonvision data.json --minify

# Convertir a YAML
jsonvision data.json --yaml
```

---

## 🚀 Inicio Rápido

### 📥 Instalación

#### Método 1: Instalación pip (Recomendado)
```bash
pip install jsonvision
```

#### Método 2: Desde código fuente
```bash
git clone https://github.com/lobehub/JSONVision.git
cd JSONVision
pip install -e .
```

#### Método 3: Ejecución Python directa
```bash
python jsonvision.py data.json
```

### 💡 Uso Básico

#### 1️⃣ Visualizar archivo JSON
```bash
jsonvision data.json
```

#### 2️⃣ Leer desde stdin
```bash
cat data.json | jsonvision
echo '{"key": "value"}' | jsonvision
```

#### 3️⃣ Mostrar estadísticas
```bash
jsonvision data.json --stats
```

#### 4️⃣ Consultar ruta
```bash
jsonvision data.json --query "user.name"
jsonvision data.json --query "items[0].title"
```

#### 5️⃣ Buscar claves
```bash
jsonvision data.json --search "id"
jsonvision data.json --search "email"
```

#### 6️⃣ Formatear salida
```bash
jsonvision data.json --format --indent 4
```

#### 7️⃣ Convertir a YAML
```bash
jsonvision data.json --yaml > output.yaml
```

---

## 📖 Guía Detallada de Uso

### Argumentos de Línea de Comando

| Argumento | Descripción | Ejemplo |
|-----------|-------------|---------|
| `file` | Ruta del archivo JSON | `jsonvision data.json` |
| `--stats` | Mostrar estadísticas | `jsonvision data.json --stats` |
| `--tree` | Mostrar árbol (por defecto) | `jsonvision data.json --tree` |
| `--query <path>` | Consultar ruta JSON | `jsonvision data.json --query "a.b.c"` |
| `--search <key>` | Buscar claves | `jsonvision data.json --search "name"` |
| `--format` | Formatear salida | `jsonvision data.json --format` |
| `--minify` | Minificar JSON | `jsonvision data.json --minify` |
| `--yaml` | Convertir a YAML | `jsonvision data.json --yaml` |
| `--indent <n>` | Indentación de formato | `jsonvision data.json --indent 4` |
| `--version` | Mostrar versión | `jsonvision --version` |

### Sintaxis de Consulta de Ruta

```bash
# Consultar clave de objeto
jsonvision data.json --query "user.name"

# Consultar elemento de array
jsonvision data.json --query "items[0]"
jsonvision data.json --query "items[0].title"

# Consultar ruta anidada
jsonvision data.json --query "a.b.c.d"
```

### Casos de Uso

#### 🎯 Depuración de API
```bash
curl https://api.example.com/data | jsonvision
```

#### 🎯 Inspección de Archivo de Configuración
```bash
jsonvision config.json --stats
jsonvision config.json --search "port"
```

#### 🎯 Análisis de Logs
```bash
jq '.data' log.json | jsonvision --search "error"
```

---

## 💡 Filosofía de Diseño y Hoja de Ruta

### 🎨 Principios de Diseño

JSONVision sigue estos principios:

1. **Ligero Primero**: Sin dependencias externas, solo biblioteca estándar Python + Rich
2. **Amigable para el Usuario**: La biblioteca Rich proporciona salida de terminal hermosa
3. **Características Prácticas**: Resuelve problemas reales de procesamiento JSON en desarrollo
4. **Respuesta Rápida**: Carga instantánea, sin esperas

### 🔮 Hoja de Ruta

- [ ] v1.1: Agregar modo interactivo con navegación por teclado
- [ ] v1.2: Soporte de validación JSONSchema
- [ ] v1.3: Agregar filtrado y agregación de datos
- [ ] v2.0: Soporte de procesamiento de transmisión para archivos JSON grandes
- [ ] v2.1: Sistema de plugins para convertidores personalizados

### 🤝 Contribuir

¡Damos la bienvenida a Issues y Pull Requests!

1. Fork del repositorio
2. Crear rama de característica (`git checkout -b feature/AmazingFeature`)
3. Confirmar cambios (`git commit -m 'Add some AmazingFeature'`)
4. Empujar a rama (`git push origin feature/AmazingFeature`)
5. Crear Pull Request

---

## 📦 Empaquetado y Despliegue

### 🐍 Requisitos de Entorno Python

- Python 3.8 o superior
- Rich >= 13.0.0
- Click >= 8.0.0
- PyYAML >= 6.0

### 📥 Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 🏃 Ejecución Local

```bash
# Método 1: Ejecución directa
python jsonvision.py data.json

# Método 2: Después de instalar
pip install -e .
jsonvision data.json
```

---

## 🆚 Comparación con Herramientas Similares

| Característica | JSONVision | jq | jless | cat |
|----------------|------------|-----|-------|-----|
| Visualización de Árbol | ✅ | ❌ | ✅ | ❌ |
| Consulta de Ruta | ✅ | ✅ | ✅ | ❌ |
| Conversión de Formato | ✅ | ❌ | ❌ | ❌ |
| Análisis Estadístico | ✅ | ❌ | ❌ | ❌ |
| Sin Dependencias | ✅* | ❌ | ❌ | ✅ |
| Multiplataforma | ✅ | ✅ | ✅ | ✅ |

> * Solo biblioteca estándar Python + Rich

---

## 📝 Registro de Cambios

### v1.0.0 (2026-06-01)
- 🎉 Lanzamiento inicial
- ✅ Visualización de árbol
- ✅ Consulta de ruta
- ✅ Búsqueda de claves
- ✅ Conversión de formato (JSON/YAML/TOML)
- ✅ Análisis estadístico
- ✅ Soporte multilingüe (Chino/Inglés/Japonés/Coreano/Español)

---

## 🤝 Licencia

Este proyecto está bajo la licencia **MIT**.

---

<div align="center">

**Made with ❤️ by [lobehub](https://github.com/lobehub)**

⭐ Star en GitHub | 🐛 Reportar Bug | 📖 Leer Documentación

</div>
