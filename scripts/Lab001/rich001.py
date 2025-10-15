import rich
from rich.progress import track
import rich.traceback
import time
import random

rich.traceback.install()

1 / 0

rich.get_console().clear()
rich.get_console().rule('[bold pink]Rich[/bold pink] Progress Bar Example', style='bold red')
rich.get_console().print('Hello:pile_of_poo: [bold magenta]Rich[/bold magenta]!', style='italic red')

for i in track(range(100), description='[bold green]Processing...[/bold green]'):
    time.sleep(random.random())