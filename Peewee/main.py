import peewee
from datetime import datetime


database = peewee.MySQLDatabase("pythondb", 
                                 host="localhost",
                                 port=3306, 
                                 user="root", 
                                 passwd="02419224596E")

class Product(peewee.Model):
    title = peewee.CharField(max_length=50)
    price = peewee.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        database = database
        db_table = "products"

    def __str__(self):
        return self.title
    
class Category(peewee.Model):
    title = peewee.CharField(max_length=20)

    class Meta:
        database = database
        db_table = "categories"

    def __str__(self):
        return self.title   

class ProductCategory(peewee.Model):
    product = peewee.ForeignKeyField(Product, backref="categories")
    category = peewee.ForeignKeyField(Category, backref="products")

    class Meta:
        database = database
        db_table = "product_categories"

if __name__ == "__main__":
    
    database.drop_tables([Product, Category, ProductCategory])
    database.create_tables([Product, Category, ProductCategory])

    ipad = Product.create(title="Ipad", price=500.50)
    iphone = Product.create(title="Iphone", price=800.00)
    tv = Product.create(title="Tv", price=600.00)

    Product.create(title="Product1", price=600.00)
    Product.create(title="Product2", price=600.00)
    Product.create(title="Product3", price=600.00)

    technology = Category.create(title="Technology")
    home = Category.create(title="Home")

    ProductCategory.create(product=ipad, category=technology)
    ProductCategory.create(product=iphone, category=technology)
    ProductCategory.create(product=tv, category=technology)

    ProductCategory.create(product=tv, category=home)

    # Mostrar en consoal todos los productos con sus correspondientes categorias!
    #LeftJoin

    products = Product.select(
        Product.title
    ).join(
        ProductCategory,
        peewee.JOIN.LEFT_OUTER
    ).where(
        ProductCategory.id == None
    )

    for product in products:
        print(product.title)
