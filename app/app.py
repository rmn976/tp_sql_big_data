from sqlalchemy import create_engine

config = {
    'host': 'db',
    'port': 3306,
    'user': 'rmn',
    'password': 'rmn',
    'database': 'classicmodels'
}

db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'

engine = create_engine(connection_str)
connection = engine.connect()

print('---MySQL Docker Container Python connection ok---\n')