import flask_migrate
import flask_sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13mbjhv887vge280ba245'


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


# db_info = {'host': 'localhost',
#            'database': 'gallery',
#            'psw': 'Lena091165',
#            'user': 'postgres',
#            'port': '5432'}

# db_info = {'host': 'dpg-chohar67avjb90hnel50-a.oregon-postgres.render.com',
#            'database': 'gallery_0ol7',
#            'psw': 'U6ezg9aq9oBVI9lF0c61ARRtll6HVtEu',
#            'user': 'gleb',
#            'port': '5432'}

db_info = {'host': 'dpg-cm2v1q5a73kc73enittg-a.frankfurt-postgres.render.com',
           'database': 'gallery_lp7s',
           'psw': 'i4YY3kwpqkjHfHlo07xFEBsi9b47j3l3',
           'user': 'stachev',
           'port': '5432'}

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://stachev:6aXU7uHGaPqNrLkpufSM6OhuIpFxjcqf@dpg-cjs6055v2qks738556rg-a.frankfurt-postgres.render.com/gallery_yiwm"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://stachev:i4YY3kwpqkjHfHlo07xFEBsi9b47j3l3@dpg-cm2v1q5a73kc73enittg-a.frankfurt-postgres.render.com/gallery_lp7s"





# app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"

#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://gleb:U6ezg9aq9oBVI9lF0c61ARRtll6HVtEu@dpg-chohar67avjb90hnel50-a.oregon-postgres.render.com/gallery_0ol7"


db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)
# db = SQLAlchemy(app)

os.environ["EMAIL_USER"] = "paintings.gallery.blog@gmail.com"
os.environ["EMAIL_PASS"] = "tQc3RFfmhz4pCw0N"

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'
app.config['MAIL_SERVER'] = 'smtp-relay.sendinblue.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)


from gallery import routes, models