# -*- coding: utf-8 -*-

__all__ = ['MAIN_ROUTE', 'LOGS', 'ENVIRONMENT']


MAIN_ROUTE = ["Main", "initialize"]

LOGS = {
    "log": "",
    "error": "",
    "debug": ""
}

#0 for production, 1 for develop, 2 for debug
ENVIRONMENT = 1

DATABASE = {
    #The user name used to authenticate with the MySQL server.
    "user": "",

    #The password to authenticate the user with the MySQL server.
    "password": "",

    #The database name to use when connecting with the MySQL server.
    "database": "",

    #The host name or IP address of the MySQL server.
    "host": "localhost",

    #The TCP/IP port of the MySQL server. Must be an integer.
    "port": 3306,

    #The location of the Unix socket file.
    "unix_socket": "",

    #Authentication plugin to use.
    "auth_plugin": "",

    #Whether to use Unicode.
    "use_unicode": True,

    #Which MySQL character set to use.
    "charset": "utf8",

    #Which MySQL collation to use.
    "collation": "utf8_general_ci",

    #Whether to autocommit transactions.
    "autocommit": False,

    #Set the time_zone session variable at connection time.
    "time_zone": "",

    #Set the sql_mode session variable at connection time.
    "sql_mode": "",

    #Whether to fetch warnings.
    "get_warnings": False,

    #Whether to raise an exception on warnings.
    "raise_on_warnings": False,

    #Timeout for the TCP and Unix socket connections.
    "connection_timeout": "",

    #MySQL client flags.
    "client_flags": "",

    #Whether cursor objects fetch the results immediately after executing queries.
    "buffered": False,

    #Whether MySQL results are returned as is, rather than converted to Python types.
    "raw": False,

    #Whether to automatically read result sets.
    "consume_results": False,

    #File containing the SSL certificate authority.
    "ssl_ca": "",

    #File containing the SSL certificate file.
    "ssl_cert": "",

    #File containing the SSL key.
    "ssl_key": "",

    #When set to True, checks the server certificate against the certificate file specified by the ssl_ca option. Any mismatch causes a ValueError exception.
    "ssl_verify_cert": False,

    #When set to True, uses IPv6 when an address resolves to both IPv4 and IPv6. By default, IPv4 is used in such cases.
    "force_ipv6": False,

    #Not supported (raises NotSupportedError when used).
    "dsn": "",

    #Connection pool name.
    "pool_name": "",

    #Connection pool size.
    "pool_size": 5,

    #Whether to reset session variables when connection is returned to pool.
    "pool_reset_session": True,

    #Whether to use compressed client/server protocol.
    "compress": False,

    #Converter class to use.
    "converter_class": "",

    #MySQL Fabric connection arguments.
    "fabric": "",

    #Server failover sequence.
    "failover": "",

    #Which option files to read.
    "option_files": "",

    #Which groups to read from option files.
    "option_groups": ['client', 'connector_python'],

    #Whether to enable LOAD DATA LOCAL INFILE.
    "allow_local_infile": True,

    #Whether to use pure Python or C Extension.
    "use_pure": True,
}
