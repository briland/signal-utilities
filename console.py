#!/usr/bin/env python

import sys

from .pinstall import install as install_package

try:
  from rich.console import Console
  from rich.live import Live
  from rich.progress import Progress
except ImportError:
  install_package('rich')
  from rich.console import Console
  from rich.live import Live
  from rich.progress import Progress


stdout = Console()
stderr = Console(file=sys.stderr)


def new_live_display(console: Console, screen: bool = False, auto_refresh: bool = False) -> Live:
  return Live(console=console, screen=screen, auto_refresh=auto_refresh)

def new_progress_display(console: Console) -> Progress:
  return Progress(console=console)

if __name__ == "__main__":
  pass
