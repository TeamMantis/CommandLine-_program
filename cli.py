import click

@click.command()
def login():
    click.echo(input('Insert Role:'))
    click.echo(input('Insert Username:'))
    click.echo(input('Insert Password:'))
    click.echo('You have been succesfully logged in!!!')
if __name__ == '__main__':
    login()