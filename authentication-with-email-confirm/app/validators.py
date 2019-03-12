# -*- coding: utf-8 -*-
from wtforms.validators import ValidationError

class Unique(object):

    def __init__(self, model, field, message):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        if self.model.query.filter(self.field==field.data).first():
            raise ValidationError(self.message)

