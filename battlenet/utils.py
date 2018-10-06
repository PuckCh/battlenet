import os

def client_id():
    return os.environ.get('BNET_CLIENT_ID')


def client_secret():
    return os.environ.get('BNET_CLIENT_SECRET')


def normalize(name):
    return name.replace("'", '')


def make_icon_url(region, icon, size='large'):
    if not icon:
        return ''

    if size == 'small':
        size = 18
    else:
        size = 56

    return 'http://%s.media.blizzard.com/wow/icons/%d/%s.jpg' % (region, size, icon)


def make_connection():
    if not hasattr(make_connection, 'Connection'):
        from .connection import Connection
        make_connection.Connection = Connection

    return make_connection.Connection(client_id=client_id(), client_secret=client_secret())
