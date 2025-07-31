import click

@click.group()
def cli():
    pass
@click.command()
def createDB():
    print("Created Database")

@click.command()
def deleteDB():
    print("Deleted Database")

@click.command()
@click.option('--count',default=1,help='Number of greetings')
@click.argument('name')
def hello(count,name):
    for x in range(count):
        print(f"Hello! {name}")


cli.add_command(createDB)
cli.add_command(deleteDB)
cli.add_command(hello)

if __name__=='__main__':
    cli()

#Output with help
"""
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  createdb
  deletedb
  hello
"""  
