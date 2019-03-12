# -*- coding: utf-8 -*-
from flask import render_template, render_template_string
from flask_mail import Mail, Message
import os

mail = Mail()

def send_mail(subject, recipients, context, body_template=None, html_template=None):
    message = Message(
        subject=subject,
        sender=os.environ.get("MAIL_USERNAME"),
        recipients=recipients)
    if body_template:
        message.body = render_template_string(body_template, **context)
    if html_template:
        message.html = render_template(html_template, **context)
    mail.send(message)

