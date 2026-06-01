#!/usr/bin/env python3
"""
JSONVision - 轻量级终端JSON数据可视化与探索工具
JSONVision - Lightweight Terminal JSON Data Visualization & Exploration Tool

Author: lobehub
License: MIT
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
from rich.console import Console
from rich.tree import Tree
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax
from rich.json import JSON as RichJSON

__version__ = "1.0.0"
__author__ = "lobehub"

# 初始化控制台
console = Console()

class JSONExplorer:
    """JSON数据探索器"""
    
    def __init__(self, data: Any, max_depth: int = 10):
        self.data = data
        self.max_depth = max_depth
        self.console = Console()
    
    def explore(self) -> None:
        """交互式探索JSON数据"""
        self._display_tree(self.data)
        self._display_stats()
    
    def _display_tree(self, data: Any, tree: Optional[Tree] = None, key: str = "root", depth: int = 0) -> None:
        """递归显示JSON树形结构"""
        if tree is None:
            tree = Tree(f"📁 [bold cyan]root[/bold cyan]", guide_style="dim")
        
        if depth >= self.max_depth:
            tree.add(f"[yellow]... (max depth reached)[/yellow]")
            self.console.print(tree)
            return
        
        if isinstance(data, dict):
            for k, v in data.items():
                if isinstance(v, (dict, list)):
                    branch = tree.add(f"📂 [bold]{k}[/bold]")
                    self._display_tree(v, branch, k, depth + 1)
                else:
                    value_repr = self._format_value(v)
                    tree.add(f"📄 [cyan]{k}[/cyan]: {value_repr}")
        elif isinstance(data, list):
            for i, item in enumerate(data[:20]):  # 限制显示20个元素
                if isinstance(item, (dict, list)):
                    branch = tree.add(f"📋 [bold][{i}][/bold]")
                    self._display_tree(item, branch, str(i), depth + 1)
                else:
                    value_repr = self._format_value(item)
                    tree.add(f"📄 [{i}]: {value_repr}")
            if len(data) > 20:
                tree.add(f"[dim]... and {len(data) - 20} more items[/dim]")
        
        self.console.print(tree)
    
    def _format_value(self, value: Any) -> str:
        """格式化值显示"""
        if value is None:
            return "[dim]null[/dim]"
        elif isinstance(value, bool):
            return f"[yellow]{value}[/yellow]"
        elif isinstance(value, (int, float)):
            return f"[green]{value}[/green]"
        elif isinstance(value, str):
            display = value[:50] + "..." if len(value) > 50 else value
            return f"[magenta]'{display}'[/magenta]"
        else:
            return f"[red]{type(value).__name__}[/red]"
    
    def _display_stats(self) -> None:
        """显示统计信息"""
        table = Table(title="📊 JSON Statistics", show_header=True, header_style="bold magenta")
        table.add_column("Metric", style="cyan", width=20)
        table.add_column("Value", style="green")
        
        if isinstance(self.data, dict):
            table.add_row("Type", "Object (Dict)")
            table.add_row("Keys", str(len(self.data)))
            table.add_row("Values", str(sum(1 for v in self.data.values())))
        elif isinstance(self.data, list):
            table.add_row("Type", "Array (List)")
            table.add_row("Length", str(len(self.data)))
        
        self.console.print(table)

class JSONFormatter:
    """JSON格式化器"""
    
    @staticmethod
    def format_json(data: Any, indent: int = 2) -> str:
        """格式化JSON"""
        return json.dumps(data, indent=indent, ensure_ascii=False, sort_keys=False)
    
    @staticmethod
    def minify_json(data: Any) -> str:
        """压缩JSON"""
        return json.dumps(data, separators=(',', ':'), ensure_ascii=False)
    
    @staticmethod
    def convert_to_yaml(data: Any, level: int = 0) -> str:
        """JSON转YAML"""
        import yaml
        return yaml.dump(data, allow_unicode=True, sort_keys=False)
    
    @staticmethod
    def convert_to_toml(data: Any) -> str:
        """JSON转TOML"""
        try:
            import toml
            return toml.dumps(data)
        except ImportError:
            return "[toml] pip install toml required"
        except Exception as e:
            return f"[error] {str(e)}"

class JSONQuery:
    """JSON路径查询器"""
    
    def __init__(self, data: Any):
        self.data = data
    
    def get(self, path: str) -> Optional[Any]:
        """通过路径获取值"""
        try:
            parts = path.replace('[', '.').replace(']', '').split('.')
            current = self.data
            for part in parts:
                if part:
                    if isinstance(current, dict):
                        current = current[part]
                    elif isinstance(current, list):
                        current = current[int(part)]
            return current
        except (KeyError, IndexError, ValueError):
            return None
    
    def search(self, key: str) -> List[tuple]:
        """搜索包含特定键的路径"""
        results = []
        
        def _search(data: Any, path: str = ""):
            if isinstance(data, dict):
                for k, v in data.items():
                    new_path = f"{path}.{k}" if path else k
                    if key.lower() in k.lower():
                        results.append((new_path, v))
                    _search(v, new_path)
            elif isinstance(data, list):
                for i, item in enumerate(data):
                    new_path = f"{path}[{i}]"
                    _search(item, new_path)
        
        _search(self.data)
        return results

def display_help():
    """显示帮助信息"""
    help_text = """
[bold cyan]JSONVision - 轻量级终端JSON数据可视化工具[/bold cyan]

[yellow]使用方法:[/yellow]
    jsonvision <file.json>                    # 可视化JSON文件
    jsonvision <file.json> --stats           # 显示统计信息
    jsonvision <file.json> --query <path>    # 查询特定路径
    jsonvision <file.json> --search <key>    # 搜索键名
    jsonvision <file.json> --format          # 格式化输出
    jsonvision <file.json> --minify         # 压缩JSON
    jsonvision <file.json> --yaml           # 转换为YAML
    cat file.json | jsonvision               # 从stdin读取

[yellow]示例:[/yellow]
    jsonvision data.json
    jsonvision data.json --query "user.name"
    jsonvision data.json --search "id"
    jsonvision data.json --format --indent 4
    """
    console.print(Panel(help_text, title="📖 Help", border_style="blue"))

def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="JSONVision - 轻量级终端JSON数据可视化工具",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('file', nargs='?', help='JSON文件路径')
    parser.add_argument('--stats', action='store_true', help='显示统计信息')
    parser.add_argument('--query', type=str, help='查询JSON路径')
    parser.add_argument('--search', type=str, help='搜索键名')
    parser.add_argument('--format', action='store_true', help='格式化输出')
    parser.add_argument('--minify', action='store_true', help='压缩JSON')
    parser.add_argument('--yaml', action='store_true', help='转换为YAML')
    parser.add_argument('--indent', type=int, default=2, help='格式化缩进')
    parser.add_argument('--tree', action='store_true', help='树形显示')
    parser.add_argument('--no-color', action='store_true', help='禁用颜色')
    parser.add_argument('--version', action='version', version=f'JSONVision {__version__}')
    
    args = parser.parse_args()
    
    # 如果没有参数，显示帮助
    if len(sys.argv) == 1:
        display_help()
        return
    
    # 读取JSON数据
    try:
        if args.file:
            file_path = Path(args.file)
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            else:
                data = json.loads(args.file)
        else:
            # 从stdin读取
            stdin_data = sys.stdin.read()
            if stdin_data.strip():
                data = json.loads(stdin_data)
            else:
                console.print("[red]Error: No input data provided[/red]")
                return
    except json.JSONDecodeError as e:
        console.print(f"[red]Error: Invalid JSON - {str(e)}[/red]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)
    
    # 创建探索器
    explorer = JSONExplorer(data)
    
    # 执行操作
    if args.tree or args.stats:
        explorer.explore()
    
    if args.format:
        formatted = JSONFormatter.format_json(data, args.indent)
        syntax = Syntax(formatted, "json", theme="monokai", line_numbers=True)
        console.print(syntax)
    
    if args.minify:
        minified = JSONFormatter.minify_json(data)
        console.print(minified)
    
    if args.yaml:
        yaml_output = JSONFormatter.convert_to_yaml(data)
        console.print(yaml_output)
    
    if args.query:
        query = JSONQuery(data)
        result = query.get(args.query)
        if result is not None:
            console.print(f"[green]Found:[/green] {result}")
        else:
            console.print(f"[red]Path '{args.query}' not found[/red]")
    
    if args.search:
        query = JSONQuery(data)
        results = query.search(args.search)
        if results:
            table = Table(title=f"🔍 Search Results for '{args.search}'")
            table.add_column("Path", style="cyan")
            table.add_column("Value", style="green")
            for path, value in results[:10]:
                table.add_row(path, str(value)[:50])
            console.print(table)
        else:
            console.print(f"[yellow]No results found for '{args.search}'[/yellow]")
    
    # 默认显示
    if not any([args.tree, args.stats, args.format, args.minify, args.yaml, args.query, args.search]):
        explorer.explore()

if __name__ == "__main__":
    main()
