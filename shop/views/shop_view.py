import os

from flask import url_for
from markupsafe import Markup
from flask_admin import form
import uuid
from flask_admin.contrib.sqla import ModelView
file_path = os.path.abspath(os.path.dirname(__name__))
# Функция, которая будет генерировать имя файла из модели и загруженного файлового объекта.
def name_gen_image(model, file_data):
    unique_filename = str(uuid.uuid4())  # Генерация уникального имени файла
    filename, file_extension = os.path.splitext(file_data.filename)
    hash_name = f'{model}/{model.title}_{unique_filename}{file_extension}'
    return hash_name
class ShopView(ModelView):
    column_display_pk = True
    column_labels = {
        'id': 'Код',
        'title':'Название категории',
        'description': 'Описание',
    }
    form_columns = ['id','title','description','imageUrl']
    column_list = ['id', 'title','description','imageUrl']
    column_filters = ['title']
    create_modal=True
    edit_modal = True
    def on_form_prefill(self, form, model):
        form.id.render_kw = {'readonly': True}

    column_editable_list = ['title', 'description']
    def _list_thumbnail(view, context, model, name):
        if not model.imageURL:
            return ''
        url = url_for('static', filename=os.path.join('storage/shop_img/', model.imageURL))
        if model.imageURL.split('.')[-1] in ['jpg', 'jpeg', 'png', 'svg', 'gif']:

            return Markup(f'<img src={url} width="100">')

    column_formatters = {
        'imageURL': _list_thumbnail
    }

    form_extra_fields = {
        # ImageUploadField Выполняет проверку изображений, создание эскизов, обновление и удаление изображений.
         "imageURL": form.ImageUploadField('',
                                            # Абсолютный путь к каталогу, в котором будут храниться файлы
                                            base_path=
                                            os.path.join(file_path, 'shop/static/storage/shop_img'),
                                            # Относительный путь из каталога. Будет добавляться к имени загружаемого файла.
                                            url_relative_path='storage/shop_img/',
                                            namegen=name_gen_image,
                                            # Список разрешенных расширений. Если не указано, то будут разрешены форматы gif, jpg, jpeg, png и tiff.
                                            max_size=(1200, 780, True),
                                            thumbnail_size=(200, 200, True),
                                            )}

    def create_form(self, obj=None):
        return super(ShopView, self).create_form(obj)

    def edit_form(self, obj=None):
        return super(ShopView, self).edit_form(obj)


