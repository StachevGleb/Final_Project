db_info = {'host': 'dpg-ch78k702qv26p1bk0dug-a.oregon-postgres.render.com',
           'database': 'bookstore_n9bb',
           'psw': 'j6lgsrQU1I6WV2rFYfCiRyLmIaLzFD7E',
           'user': 'admin',
           'port': ''}


class Config:
    SECRET_KEY = "qwertyuiop"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"

