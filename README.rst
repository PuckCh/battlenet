battlenet
=====================

Python Library for Blizzard's Community Platform API

Major features
----------------------

* Pythonic
* Unicode normalization
* Lazyloading and eagerloading
* Support locales (en, fr, de, ...)
* Support client_id/client_secret OAuth2 login

Making a connection
----------------------

Global connection settings can be setup so that objects can make connections implicitly.

::

    from battlenet import Connection

    Connection.setup(
        client_id='your client id',
        client_secret='your client secret',
        locale='fr')

You can also create connections explicitly.

::

    from battlenet import Connection

    connection = Connection(
        client_id='your client id',
        client_secret='your client secret',
        locale='fr')

Using the api
-------------

You can define your client_id/client_secret via environment variables. For
example using a bash shell:

::

    $ export BNET_CLIENT_ID=your-client-id-here
    $ export BNET_CLIENT_SECRET=your-client-secret-here

More details on the official Blizzard Battle.net Developer Portal https://develop.battle.net/.

Fetching a specific realm
-------------------------

::

    from battlenet import Realm

    # If a global connection was setup
    realm = Realm(battlenet.UNITED_STATES, 'Nazjatar')

    # Using a specific connection
    realm = connection.get_realm(battlenet.UNITED_STATES, 'Nazjatar')

    print realm.name
    # => Nazjatar

    print realm.is_online()
    # => true

    print realm.type
    # => PVP


Fetching all realms
-------------------------

::

    for realm in connection.get_all_realms(battlenet.UNITED_STATES):
        print realm

Fetching a character
----------------------

::

    from battlenet import Character

    # If a global connection was setup
    character = Character(battlenet.UNITED_STATES, 'Nazjatar', 'Vishnevskiy', fields=[Character.GUILD])

    # Using a specific connection
    character = connection.get_character(battlenet.UNITED_STATES, 'Nazjatar', 'Vishnevskiy', fields=[Character.GUILD])

    print character.name
    # => Vishnevskiy

    print character.guild.name
    # => Excellence


Fetching a guild
----------------------

::

    from battlenet import Guild

    # If a global connection was setup
    guild = Guild(battlenet.UNITED_STATES, 'Nazjatar', 'Excellence')

    # Using a specific connection
    guild = connection.get_guild(battlenet.UNITED_STATES, 'Nazjatar', 'Excellence')

    print guild.name
    # => Excellence

    leader = guild.get_leader()
    print leader.name
    # => Clí

More Examples
----------------------

Read the unit tests inside the tests directory.
