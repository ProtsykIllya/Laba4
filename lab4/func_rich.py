from rich.console import Console
from rich.table import Table
def show_table(df):
    table = Table(title="Люди")
    for column in df.columns:
        table.add_column(str(column))
    for _, row in df.iterrows():
        table.add_row(*[str(value) for value in row])
    Console().print(table)