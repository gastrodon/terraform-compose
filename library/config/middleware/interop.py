from library.config.middleware.parser import parser
from library.types.parser import Order


@parser.middleware(Order.PRE_LOAD)
def bash_yaml(args, config):
    """Interop $[bash] expressions into literal YAML"""
    return config  # TODO


@parser.middleware(Order.PRE_LOAD)
def bash_values(args, config):
    """Interop $(bash) expressions into values for keys"""
    return config  # TODO
