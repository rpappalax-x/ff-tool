#!/usr/bin/env python

import os
import platform
import re
import sys
import ConfigParser as configparser  # Python 2
from outlawg import Outlawg

Log = Outlawg()


class FirefoxEnvHandler():
    def __init__(self):
        pass

    @staticmethod
    def get_os():
        """
        Do our best to determine the user's current operating system.
        """
        system = platform.system().lower()
        system = re.split('[-_]', system, maxsplit=1).pop(0)

        if system == "cygwin":
            return "windows"

        return system

    @classmethod
    def is_linux(cls):
        """
        Am I running on Linux?
        """
        return cls.get_os() == "linux"

    @classmethod
    def is_mac(cls):
        """
        Am I running on Mac/Darwin?
        """
        return cls.get_os() == "darwin"

    @classmethod
    def is_other(cls):
        """
        I 'literally' have no idea who you are.
        """
        return not (cls.is_linux() or cls.is_mac() or cls.is_windows())

    @classmethod
    def is_windows(cls):
        """
        Am I running on Windows/Cygwin?
        """
        return cls.get_os() == "windows"


class IniHandler(FirefoxEnvHandler):
    def __init__(self, ini_path=None):
        """
        Creates a new config parser object, and optionally loads a config file
        if `ini_path` was specified.
        """
        self.config = configparser.SafeConfigParser(os.environ)

        if ini_path is not None:
            self.load_config(ini_path)

    def load_config(self, ini_path):
        """
        Load an INI config based on the specified `ini_path`.
        """
        Log.header('LOADING {0}'.format(ini_path))

        # Make sure the specified config file exists, fail hard if missing.
        if not os.path.isfile(ini_path):
            sys.exit('Config file not found: {0}'.format(ini_path))

        self.config.read(ini_path)

    def load_os_config(self, config_path):
        """
        Load an INI file based on the current operating system. This method
        will attempt to load a "darwin.ini", "cygwin.ini", or "linux-gnu.ini"
        file from the specified `config_path` based on the current OS.
        """
        os_config = os.path.join(config_path, IniHandler.get_os() + '.ini')
        self.load_config(os_config)

    def create_env_file(self, out_file='.env'):
        """
        Generate and save the output environment file so we can source it from
        something like .bashrc or .bashprofile.
        """
        Log.header('CREATING ENV FILE ({0})'.format(out_file))

        env_fmt = "export %s=\'%s\'"
        env_vars = []

        # Generic paths to Sikuli and Firefox profile directories.
        for key in ['PATH_SIKULIX_BIN', 'PATH_FIREFOX_PROFILES']:
            env_key = self.get_default(key + '_ENV')
            env_vars.append(env_fmt % (key, env_key))

        # Channel specific Firefox binary paths.
        for channel in self.sections():
            export_name = 'PATH_FIREFOX_APP_' + channel.upper()
            firefox_bin = self.get(channel, 'PATH_FIREFOX_BIN_ENV')
            env_vars.append(env_fmt % (export_name, firefox_bin))

        output = '\n'.join(env_vars) + '\n'
        print(output)

        with open(out_file, 'w') as env_file:
            env_file.write(output)
            env_file.close()

    def sections(self):
        """
        Shortcut for getting a config's `sections()` array without needing to
        do the visually horrifying `self.config.config.sections()`.
        """
        return self.config.sections()

    def get(self, section, option):
        """
        Shortcut for calling a config's `get()` method without needing to
        do the visually horrifying `self.config.config.get()`.
        """
        return self.config.get(section, option)

    def set(self, section, option, value):
        """
        Shortcut for calling a config's `set()` method without needing to
        do the visually horrifying `self.config.config.set()`.
        """
        return self.config.set(section, option, str(value))

    def get_default(self, option):
        """
        Shortcut to get a value from the "DEFAULTS" section of a ConfigParser
        INI file. Doesn't save much time, but reads a bit easier.
        """
        return self.get('DEFAULT', option)


if __name__ == '__main__':

    i = IniHandler()
    i.load_os_config('configs')
    i.create_env_file()
