from shop import db
class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(20), primary_key=True)
    role=db.Column(db.String(20), unique=False, nullable=False, default='Пользователь')
    username = db.Column(db.String(20), unique=False, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class Shop(db.Model):
    __tablename__ = "shop"
    id = db.Column(db.String(20), primary_key=True)
    title = db.Column(db.Text(200), unique=False, nullable=False)
    description = db.Column(db.Text(500), nullable=False)
    imageUrl = db.Column(db.String(20), nullable=False, default='default.jpg')

class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.String(20), primary_key=True)
    description = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, unique=False, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.String(20), db.ForeignKey('category.id'), nullable=True)
    shop = db.Column(db.String(20), db.ForeignKey('shop.id'), nullable=True)
    price = db.Column(db.Numeric, nullable=False)
    images = db.Column(db.String(100), nullable=False, default='default-image.png')
    active = db.Column(db.Boolean)
    category = db.relationship("Category", backref="products", lazy=True)
    def __str__(self):
        return self.title


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.String(20), primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.Text(500), nullable=False)
    def __str__(self):
        return self.title