"""Allows to read from config file."""
import configparser

from os.path import expandvars
from os.path import join


class Configparser(object):
    """Utility for read a config file."""

    def get(self):
        """Return the config object."""
        if(self.firsttime):
            self.firsttime = False
            self.config.read(join(self.path, self.fname))
        return self.config

    def is_loaded(self):
        """Return if is loaded."""
        if (self.get() and self.get().sections()):
            return True
        else:
            return False

    def where_is(self):
        """Return absolute path of config filename."""
        return join(self.path, self.fname)

    def __get_default_filename():
        """Config file. Used when not specified a config filename.

        This is a private method.
        """
        return 'conf.ini'

    def __init__(self, path='$HOME', fname=__get_default_filename()):
        """Initialize method."""
        self.path = expandvars(path or '')
        self.fname = expandvars(fname or self.__get_default_filename())
        self.config = configparser.ConfigParser()
        self.firsttime = True
