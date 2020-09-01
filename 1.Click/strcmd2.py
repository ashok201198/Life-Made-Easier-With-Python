import click


class config(object):
    def __init__(self):
        self.removedigits=False

pass_config=click.make_pass_decorator(config,ensure=True)

@click.group()
@click.option('--removedigits/--no-removedigits', is_flag=True, help="to remove digits from input")
@pass_config
def cli(config,removedigits):
    """support some string commands from strings"""
    config.removedigits=removedigits


@cli.command("concat",help="concatenates passsed in strings with delimiter")
@click.option('-d','--delimiter',default=":",help="joined")
@click.argument('statement',nargs=-1)
@pass_config
def concat(config,delimiter,statement):
    args=list(statement)
    st=delimiter.join(args)
    s=""
    if config.removedigits:
        l=list(map(str,range(10)))
        for i in st:
            if i not in l:
                s+=i
        print(s)
    else:
        print(st)

@cli.command("upper",help="converts the word to upper case")
@click.argument('statement')
@pass_config
def upper(config,statement):
    st=statement.upper()
    s = ""
    if config.removedigits:
        l = list(map(str, range(10)))
        for i in st:
            if i not in l:
                s += i
        print(s)
    else:
        print(st)

@cli.command("lower",help="converst the word to lower case")
@click.argument('statement')
@pass_config
def lower(config,statement):
    st=statement.lower()
    s = ""
    if config.removedigits:
        l = list(map(str, range(10)))
        for i in st:
            if i not in l:
                s += i
        print(s)
    else:
        print(st)


cli()