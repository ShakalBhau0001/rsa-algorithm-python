from math import gcd
from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt
from rich.table import Table

console = Console()

# Header
console.print(
    Panel.fit(
        "[bold cyan]RSA Encryption & Decryption[/bold cyan]",
        border_style="green"
    )
)

# Input Prime Numbers
p = IntPrompt.ask("[yellow]Enter 1st Prime Number[/yellow]")
q = IntPrompt.ask("[yellow]Enter 2nd Prime Number[/yellow]")

# Computation of modulus and Euler's Totient
n = p * q
phi = (p - 1) * (q - 1)

# Selecting public exponent [e]
e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1

# Computation of private exponent [d]
d = pow(e, -1, phi)

# Key Display Table
key_table = Table(title="Generated RSA Keys", header_style="bold magenta")
key_table.add_column("Key Type", justify="center")
key_table.add_column("Value", justify="center")
key_table.add_row("Public Key (e, n)", str((e, n)))
key_table.add_row("Private Key (d, n)", str((d, n)))
console.print()
console.print(key_table)

# Message Input
msg = IntPrompt.ask(f"\n[cyan]Enter message (number < {n})[/cyan]")

# Encryption
cipher = pow(msg, e, n)

console.print(
    Panel(
        f"[bold green]{cipher}[/bold green]",
        title="Encrypted Message",
        border_style="green"
    )
)

# Decryption
plain = pow(cipher, d, n)

console.print(
    Panel(
        f"[bold bright_white]{plain}[/bold bright_white]",
        title="Decrypted Message",
        border_style="blue"
    )
)
