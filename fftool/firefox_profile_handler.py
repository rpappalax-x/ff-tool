#!/usr/bin/env python

from firefox_env_handler import FirefoxEnvHandler, IniHandler

import sys


class FirefoxProfileHandler(object):

    def __init__(self, config):
        # Do some basic type checking on the `config` attribute.
        if isinstance(config, IniHandler):
            self.config = config

        elif isinstance(config, str):
            self.config = IniHandler()
            self.config.load_os_config(config)

        else:
            sys.exit('FirefoxProfileHandler: Unexpected config data type')

        self.profile_dir = self.config.get_default('PATH_FIREFOX_PROFILES_ENV')

    def switch_prefs(self, profile_name, user_prefs, channel='nightly'):
        channel_firefox_bin = self.config.get(channel, 'PATH_FIREFOX_BIN_ENV')
        print(('{0} -CreateProfile {1}'.format(channel_firefox_bin, profile_name)))  # NOQA
        print('copy prefs.js to <new profile name> dir')

    def delete_all_profiles(self):
        FirefoxEnvHandler.clean_folder(self.profile_dir)


def main():
    config_path = './configs/'
    FirefoxProfileHandler(config_path)


if __name__ == '__main__':
    main()
