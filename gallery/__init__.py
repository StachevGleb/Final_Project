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

db_info = {'host': 'dpg-ch7aj2o2qv26p1buenvg-a.oregon-postgres.render.com',
           'database': 'gallery_2nft',
           'psw': '1YupNaos78oExe5rlkQrvYRyTfhVE38X',
           'user': 'gleb',
           'port': '5432'}

# app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://gleb:1YupNaos78oExe5rlkQrvYRyTfhVE38X@dpg-ch7aj2o2qv26p1buenvg-a.oregon-postgres.render.com/gallery_2nft"

# postgres://gleb:1YupNaos78oExe5rlkQrvYRyTfhVE38X@dpg-ch7aj2o2qv26p1buenvg-a.oregon-postgres.render.com/gallery_2nft

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