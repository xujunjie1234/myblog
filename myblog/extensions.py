
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor 
from flask_login import LoginManager, AnonymousUserMixin
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_whooshee import Whooshee
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
import datetime

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
ckeditor = CKEditor()
mail = Mail()
moment = Moment()
whooshee = Whooshee()
toolbar = DebugToolbarExtension()
migrate = Migrate()

@login_manager.user_loader
def load_user(user_id):
    from myblog.models import Admin
    user = Admin.query.get(int(user_id))
    return user

login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'warning'

# class Guest(AnonymousUserMixin):
#     def __init__(self):
#         self.time1 = datetime.datetime(2019, 10, 31, 10, 51, 0)

#     def can(self):
#         # self.time1 = datetime.datetime(2019, 10, 31, 10, 51, 0)
#         if not self.time1:
#             self.time1 = datetime.datetime(2001, 1, 31, 10, 51, 0)
#         return self.time1

#     @property
#     def is_admin(self):
#         return False


# login_manager.anonymous_user = Guest