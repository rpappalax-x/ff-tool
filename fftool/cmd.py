"""module providing ff-tool command menus"""

from firefox_download import download

class CMDDownload():

    def __init__(self, subparsers, CHANNELS, DEFAULT_CHANNEL):
        download = subparsers.add_parser('download', help='<download> command help')
        download.add_argument(
            '-c',
            '--channel',
            choices=CHANNELS,
            default=DEFAULT_CHANNEL,
            type=str,
            help='Download a specific Firefox channel via mozdownload.'
        )
        download.set_defaults(func=self.cmd)

    def cmd(self, args):
        print('Downloading Firefox... [channel: {0}]'.format(args.channel))

        download(args.channel)


class CMDProfile():

    def __init__(self, subparsers):
        profile = subparsers.add_parser('profile', help='<profile> command help')
        profile.add_argument(
            '-c',
            '--create',
            type=str,
            help='Create a new Firefox profile with the specified name.'
        )
        profile.add_argument(
            '-d',
            '--delete',
            type=str,
            help='Delete the specified Firefox profile.'
        )
        profile.set_defaults(func=self.cmd)

    def cmd(self, args):
        if args.create:
            print('Creating Firefox profile... [name: {0}]'.format(args.create))

        if args.delete:
            print('Deleting Firefox profile... [name: {0}]'.format(args.delete))


class CMDInstall():

    def __init__(self, subparsers, CHANNELS, DEFAULT_CHANNEL):
        install = subparsers.add_parser('install', help='<install> command help')
        install.add_argument(
            '-c',
            '--channel',
            choices=CHANNELS,
            default=DEFAULT_CHANNEL,
            type=str,
            help='Install a specific Firefox channel.'
        )
        install.set_defaults(func=self.cmd)


    def cmd(self, args):
        print('Installing Firefox... [channel: {0}]'.format(args.channel))



class CMDUninstall():

    def __init__(self, subparsers, CHANNELS, DEFAULT_CHANNEL):
        uninstall = subparsers.add_parser('uninstall', help='<uninstall> command help')
        uninstall.add_argument(
            '-c',
            '--channel',
            choices=CHANNELS,
            default=DEFAULT_CHANNEL,
            type=str,
            help='Uninstall a specific Firefox channel.'
        )
        uninstall.set_defaults(func=self.cmd)


    def cmd(self, args):
        print('Uninstalling Firefox... [channel: {0}]'.format(args.channel))