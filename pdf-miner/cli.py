"""
pdf-miner

Usage:
  pdf-miner grab <URL>
  pdf-miner grab --input=FILE
  pdf-miner parse [<path/to/dir>] [-o OUTPUT_DIR | --output OUTPUT_DIR]
  pdf-miner join [<path/to/dir>] [-o OUTPUT_DIR | --output OUTPUT_DIR]
  pdf-miner -h | --help
  pdf-miner -v | --version

Help:
  For help using this tool, please open an issue on GitHub. 
  The link for GitHub repository is: 
  https://github.com/reesepathak/pdf-mining
"""

from inspect import getmembers, isclass
from docopt import docopt
from . import __version__ as VERSION

def main():
    """ Main CLI entrypoint."""
    import commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll dynamically match the command the user
    # is attempting to call with a pre-defined command class
    # that we've created.
    
    for k, v in options.iteritems():
        if hasattr(commands, k):
            module = getattr(commands, k)
            commands = getmembers(module, isclass)
            command = [command[1] for command in commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
