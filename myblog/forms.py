
from flask_wtf import FlaskForm
from wtforms import SelectField,StringField,TextAreaField,PasswordField,\
    SelectField,BooleanField,ValidationError,HiddenField ,SubmitField
from wtforms.validators import DataRequired, Email, URL, Length, Optional
from flask_ckeditor import CKEditorField
from myblog.models import Category

class LoginForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired(),Length(1,20)])
    password = PasswordField("Password",validators=[DataRequired(),Length(6,128)])
    remember = BooleanField("记住我")
    submit = SubmitField("登录")

class SettingForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired(),Length(1,20)])
    blog_title = StringField("Title",validators=[DataRequired(),Length(1,20)])
    submit = SubmitField()

class PostForm(FlaskForm):
    title = StringField("Title",validators=[DataRequired(),Length(1,20)])
    category = SelectField("Category",coerce=int,default=1)
    body = CKEditorField("body",validators=[DataRequired()])
    submit = SubmitField()

    def __init__(self,*args,**kwargs):
        super(PostForm,self).__init__(*args,**kwargs)
        self.category.choices = [(category.id,category.name) for category in Category.query.order_by(Category.name).all()]

class CategoryForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired(),Length(1,10)])
    submit = SubmitField()

    def validate_name(self,Field):
        if Category.query.filter_by(name=Field.data).first():
            raise ValidationError("名称已存在")

class CommentForm(FlaskForm):
    author = StringField("评论者",validators=[DataRequired(),Length(1,20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 254)])
    body = TextAreaField("评论内容:",validators=[DataRequired(),Length(1,800)])
    submit = SubmitField('提交')

class AdminCommentForm(CommentForm):
    author = HiddenField()
    email = HiddenField()

