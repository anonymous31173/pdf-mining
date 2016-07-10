# pdf-miner/commands/base.py
""" This file describes the base command """

# TODO: switch from base class to ABCMeta...


class Base(object):
    """ A base command object """

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs

    def run(self):
        raise NotImplementedError("You must implement the run() method")
