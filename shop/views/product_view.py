import os

from flask import url_for
from markupsafe import Markup
from flask_admin import form
import uuid
from flask_admin.contrib.sqla import ModelView
from shop import bcrypt
file_path = os.path.abspath(os.path.dirname(__name__))
def name_gen_image(model, file_data):
    unique_filename = str(uuid.uuid4())
    filename, file_extension = os.path.splitext(file_data.filename)
    hash_name = f'{model}/{model.title}_{unique_filename}{file_extension}'
    return hash_name
class ProductView(ModelView):
    column_display_pk = True
    column_labels = {
        'id': 'Код',
        'title': 'Название товара',
        'description': 'Описание',
        'amount':'Количество',
        'category': 'Категория',
        'price': 'Цена',
        'images': 'Изображения',
        'shop': 'Магазины',
        'active': 'Наличие',

    }
    column_display_pk = True
    form_columns = ['id', 'title', 'description', 'images', 'shop','category', 'amount', 'price', 'active']
    column_list = ['id', 'title', 'description', 'shop', 'images','category', 'amount', 'price', 'active']
    column_filters = ['id', 'title','category']
    column_sortable_list = ['title', 'amount','category', 'price']
    column_searchable_list = ['id', 'title']
    column_editable_list = ['title', 'description','amount', 'category','price','active']
    def on_form_prefill(self, form, model):
        form.id.render_kw = {'readonly': True}
    def _list_thumbnail(view, context, model, name):
        if not model.images:
            return ''
        url = url_for('static', filename=os.path.join('storage/user_img/', model.images))
        if model.images.split('.')[-1] in ['jpg', 'jpeg', 'png', 'svg', 'gif']:
            return Markup(f'<img src={url} width="100">')

    column_formatters = {
        'images': _list_thumbnail
    }

    form_extra_fields = {
                    "images": form.ImageUploadField('',
                    base_path=
                    os.path.join(file_path, 'shop/static/storage/user_img'),
                    url_relative_path='storage/user_img/',
                    namegen=name_gen_image,
                    max_size=(1200, 780, True),
                    thumbnail_size=(200, 200, True),

            )}

    def create_form(self, obj=None):
        return super(ProductView, self).create_form(obj)

    def edit_form(self, obj=None):
        return super(ProductView, self).edit_form(obj)