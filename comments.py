import click


@click.command()
def comment():
    click.echo('Add comment')
    click.echo(input(':'))
    click.echo('Comment Saved')
    click.echo('Add comment')
    click.echo(input(':'))
    click.echo('Comment Saved')


if __name__ == '__main__':
    comment()
