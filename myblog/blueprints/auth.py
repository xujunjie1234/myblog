
from flask import url_for,redirect,render_template,flash,request,current_app,Blueprint
from flask_login import login_user,logout_user,login_required,current_user

from myblog.forms import LoginForm

from myblog.settings import Operations
from myblog.extensions import db
from myblog.utils import redirect_back
from myblog.models import Admin


auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        admin = Admin.query.first()
        if admin:
            if username == admin.username and admin.validate_password(password):
                login_user(admin, remember)
                # flash('欢迎回来.', 'info')
                return redirect_back()
            flash('无效用户名或密码.', 'warning')
        else:
            flash('账号不存在.', 'warning')
    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    # flash('Logout success.', 'info')
    return redirect_back()

