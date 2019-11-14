
import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'



class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')
    #测试
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    #数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    #CKEDITOR编辑器设置
    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_FILE_UPLOADER = 'admin.upload_image'
    CKEDITOR_ENABLE_CODESNIPPET = True
    CKEDITOR_CODE_THEME = 'docco'
    # CKEDITOR_PKG_TYPE = 'full'
    CKEDITOR_WIDTH = 900
    CKEDITOR_HEIGHT = 400
    # CKEDITOR_EXTRA_PLUGINS = []
    CKEDITOR_SERVE_LOCAL = True

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

    MYBLOG_EMAIL = MAIL_USERNAME
    MYBLOG_POST_PER_PAGE = 6
    MYBLOG_MANAGE_POST_PER_PAGE = 15
    MYBLOG_COMMENT_PER_PAGE = 5
    
    #文件上传路径
    MYBLOG_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    #允许图片格式
    MYBLOG_ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
    #邮件主题
    MYBLOG_MAIL_SUBJECT_PREFIX = '[发狂的桔子]'     

    WHOOSHEE_MIN_STRING_LEN = 1
    MYBLOG_SEARCH_RESULT_PER_PAGE = 6

    MYBLOG_SLOW_QUERY_THRESHOLD = 280


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data-dev.db')


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # in-memory database


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))



class Operations:
    CONFIRM = 'confirm'
    RESET_PASSWORD = 'reset-password'
    CHANGE_EMAIL = 'change-email'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
