import click


def func(st):
    s = ""
    l = list(map(str, range(10)))
    for i in st:
        if i not in l:
            s += i
    return s


@click.group()
@click.option('--removedigits /--no-removedigits', is_flag=True,default=False, help="remove digits from input", )
@click.pass_context
def cli(context,removedigits):
    """Supports some string commands from command line"""
    context.obj={'removedigits':removedigits}
    #print(type(context))
    #setattr(context,'removedigits',removedigits)


@cli.command("concat",short_help="concatenates passsed in strings with delimiter")
@click.option('-d','--delimiter',default=":",help="defaults to:")
@click.argument('tokens',nargs=-1)
@click.pass_context
def concat(context,delimiter,tokens):
    """pass one or more strings, concat them with delimiter and print them out"""
    args=list(tokens)
    st=delimiter.join(args)
    if context.obj['removedigits']:
    #if context.removedigits:
        click.echo(func(st))
    else:
        click.echo(st)

@cli.command("upper",help="converts the word to upper case")
@click.argument('statement')
@click.pass_context
def upper(context,statement):
    st=statement.upper()
    if context.obj['removedigits']:
    #if context.removedigits:
        click.echo(func(st))
    else:
        click.echo(st)

@cli.command("lower",help="converts the word to lower case")
@click.argument('statement')
@click.pass_context
def lower(context,statement):
    st=statement.lower()
    #if context.obj['removedigits']:
    if context.removedigits:
        click.echo(func(st))
    else:
        click.echo(st)


cli()