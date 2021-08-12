from django.db import models

# Create your models here.
# 出版社数据库对象模型
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False)
    address = models.CharField(max_length=64, null=False)

# 书籍数据库对象模型
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    nums = models.IntegerField(verbose_name="库存数")
    sales = models.IntegerField(verbose_name="售出数")
    publisher = models.ForeignKey(to='Publisher', on_delete=models.CASCADE)

# 用户数据库对象模型
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    password = models.CharField(max_length=256)

# 借阅记录数据库对象模型
class Borrow(models.Model):
    book_id = models.ForeignKey(to="Book", on_delete=models.CASCADE)
    user_id = models.ForeignKey(to="User", on_delete=models.CASCADE)
    time = models.DateTimeField('date borrowed')
