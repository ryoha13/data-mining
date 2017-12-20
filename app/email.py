#! -*- coding:utf-8 -*-

from flask_mail import Message
from flask import current_app, render_template
from . import mail
from threading import Thread


def async_mail_send(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(subject, sender=app.config['MAIL_ADMIN'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=async_mail_send, args=[app, msg])
    thr.start()
    return thr
