from rich.console import Console
from rich.panel import Panel
from rich.align import Align

def show_welcome_banner():
    console = Console()

    message = """
[bold cyan]🛸 Wokie has awakened...[/bold cyan]
[bold white]Welcome, Young Padawan![/bold white]

⚔️  Your mission is to master the commands of the Force.

💡  Type [bold yellow]help[/bold yellow] to see the list of commands.

[italic]May the Code be with you.[/italic]
"""
    banner = Panel.fit(
        Align.center(message, vertical="middle"),
        title="[bold bright_blue]Wokie Assistant[/bold bright_blue]",
        border_style="magenta"
    )

    console.print(banner, justify="center")