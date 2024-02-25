import os
from flask_admin.contrib.sqla import ModelView

class UsersView(ModelView):
    column_display_pk = True
    column_labels = {
        'id': 'Код',
        'role':'Роль',
        'username': 'Имя пользователя',
        'password': 'Пароль',
    }
    form_columns = ['id','role', 'username', 'password']
    column_list = ['id', 'role','username', 'password']
    def on_form_prefill(self, form, model):
        form.id.render_kw = {'readonly': True}

    AVAILABLE_USER_TYPES = [
        (u'Администратор', u'Админ'),
        (u'Пользователь', u'Пользователь'),
    ]

    form_choices = {
        'role': AVAILABLE_USER_TYPES,
    }