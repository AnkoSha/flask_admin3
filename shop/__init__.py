from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_admin.contrib.sqla import ModelView



db = SQLAlchemy()
babel = Babel()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    db.init_app(app)
    babel.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    from shop.routes import MyMainView
    from models import Users,Shop,Category,Product
    from shop.views.user_view import UsersView
    from shop.views.category_view import CategoryView
    from shop.views.product_view import ProductView
    from shop.views.shop_view import ShopView
    from shop.routes import MySignInView, MyLoginView, MyAccountView,MyExitView
    admin = Admin(app, name='Мои товары', index_view=MyMainView(),template_mode='bootstrap4',url='/')
    admin.add_view(MySignInView(name='Регистрация', url='register'))
    admin.add_view(MyLoginView(name='Логин', url='login'))
    admin.add_view(MyAccountView(name='Аккаунт', url='account'))
    admin.add_view(UsersView(Users,db.session))
    admin.add_view(ShopView(Shop, db.session))
    admin.add_view(CategoryView(Category,db.session))
    admin.add_view(ProductView(Product, db.session))
    admin.add_view(MyExitView(name='Выход', url='exit'))
    return app