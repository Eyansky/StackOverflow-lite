from api.server import APP

CONNECT_CREDS = {
    "host": APP.config.get('DATABASE_HOST'),
    "database": APP.config.get('DATABASE_NAME'),
    "user": APP.config.get('DATABASE_USER'),
    "password": APP.config.get('DATABASE_PASS')
}
