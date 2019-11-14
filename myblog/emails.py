from threading import Thread

from flask import url_for, current_app
from flask_mail import Message

from myblog.extensions import mail


def _send_async_mail(app, message):
    with app.app_context():
        mail.send(message)


def send_mail(subject, to, html):
    app = current_app._get_current_object()
    message = Message(subject,recipients=[to], html=html)
    thr = Thread(target=_send_async_mail, args=[app, message])
    thr.start()
    return thr


def send_new_comment_email(post):
    post_url = url_for('blog.show_post', post_id=post.id, _external=True) + '#comments'
    send_mail(subject='新的评论', to=current_app.config['MYBLOG_EMAIL'],
              html='<p>你的文章： <i>%s</i>有新的评论, 点击下方链接查看:</p>'
                   '<p><a href="%s">%s</a></P>'
                   '<p><small style="color: #868e96">请不要回复此条邮件.</small></p>'
                   % (post.title, post_url, post_url))


def send_new_reply_email(comment):
    post_url = url_for('blog.show_post', post_id=comment.post_id, _external=True) + '#comments'
    send_mail(subject='新的回复', to=comment.email,
              html='<p>你在文章 <i>%s</i>中的留言有了新的回复, 点击下方链接查看: </p>'
                   '<p><a href="%s">%s</a></p>'
                   '<p><small style="color: #868e96">请不要回复此条邮件.</small></p>'
                   % (comment.post.title, post_url, post_url))
