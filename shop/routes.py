from flask import url_for, redirect
from flask_admin import expose, BaseView, AdminIndexView
from sqlalchemy import desc

from models import Product


class MyMainView(AdminIndexView):
    @expose('/')
    def admin_main(self):
        product = Product.query.all()
        images = url_for('static', filename=f'shop/static/')
        return self.render('admin/index.html', posts=product, image=images)

class MySignInView(BaseView):
    @expose('/')
    def sing_in(self):
        return self.render('admin/sign_in.html', legend='Регистрация')


class MyLoginView(BaseView):
    @expose('/')
    def login(self):
        return self.render('admin/login.html', legend='Войти')


class MyAccountView(BaseView):
    @expose('/')
    def account(self):
        posts = Product.query.all()
        image = url_for('static', filename=f'storage/user_img')
        return self.render('admin/account.html', posts=posts, image=image)


class MyExitView(BaseView):
    @expose('/')
    def exit(self):
        return redirect(url_for('admin.admin_main'), 302)
