#!/usr/bin/env python3
"""
JSONVision 安装配置文件
"""

from setuptools import setup, find_packages
from pathlib import Path

# 读取README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="jsonvision",
    version="1.0.0",
    author="lobehub",
    author_email="",
    description="轻量级终端JSON数据可视化与探索工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lobehub/JSONVision",
    project_urls={
        "Bug Tracker": "https://github.com/lobehub/JSONVision/issues",
        "Source Code": "https://github.com/lobehub/JSONVision",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Terminals",
        "Topic :: Text Editors",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "rich>=13.0.0",
        "click>=8.0.0",
        "pyyaml>=6.0",
        "toml>=0.10.0",
    ],
    entry_points={
        "console_scripts": [
            "jsonvision=jsonvision:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
