import os
from flask_admin.contrib.sqla import ModelView

class CategoryView(ModelView):
    column_display_pk = True
    column_labels = {
        'id': 'Код',
        'title':'Название категории',
        'description': 'Описание',
        'imageUrl':'Выберите фотографию'
    }
    form_columns = ['id','title','description']
    column_list = ['id', 'title','description']
    column_filters = ['id','title']
    column_editable_list=['title','description']
    create_modal=True
    edit_modal = True
    def on_form_prefill(self, form, model):
        form.id.render_kw = {'readonly': True}
