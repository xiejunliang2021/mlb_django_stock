# import os
# import django
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_study_mlb.settings")### 把test02 改成自己的项目名即可
# django.setup()
#


from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField('用户名', max_length=30, default='')
    password = models.CharField('密码', max_length=50, default='')
    create_date = models.DateTimeField('创建时间', auto_now_add=True)
    update_date = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return "%s--%s" % (self.username, self.password)


class Book(models.Model):
    title = models.CharField('书名', max_length=50, default='')
    price = models.DecimalField('价格', max_digits=7, decimal_places=2)
    info = models.CharField('描述', max_length=100, default='')
    market_price = models.DecimalField("定价", max_digits=7, decimal_places=2, default=1)
    code = models.DecimalField("工厂价", max_digits=7, decimal_places=1, default=50)
    is_active = models.BooleanField("是否活跃", default=True)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return "%s_%s_%s_%s" % (self.title, self.price, self.market_price, self.info)


class Author(models.Model):
    name = models.CharField('作者姓名', max_length=11, default='')
    age = models.IntegerField('年龄', default=18)
    email = models.EmailField('邮箱')
    time_create = models.DateTimeField('创建时间', auto_now_add=True)
    time_update = models.DateTimeField('更新时间', auto_now=True)
    birthday = models.DateField('作者生日', default='1986-10-13')

    class Meta:
        db_table = 'author'

    def __str__(self):
        return '%s_%s_%s_%s_%s_%s' % (
            self.name, self.age, self.email, self.time_create, self.time_update, self.birthday)


class Tactics(models.Model):
    ts_code = models.CharField("股票代码", max_length=9, default='')
    name = models.CharField("股票名称", max_length=20, default='')
    trade_date = models.DateField("策略时间", default='')
    buy_01 = models.DecimalField("第一买点", max_digits=9, decimal_places=2)
    buy_02 = models.DecimalField("第二买点", max_digits=9, decimal_places=2)
    stop_win = models.DecimalField("止赢", max_digits=9, decimal_places=2)
    stop_loss = models.DecimalField("止损", max_digits=9, decimal_places=2)

    class Meta:
        db_table = "tb_tactics"
        ordering = ["-trade_date"]

    def __str__(self):
        return "%s_%s_%s_%s_%s_%s_%s_%s" % (
            self.code, self.name, self.trade_date, self.buy_01, self.buy_02, self.buy_03, self.stop_surplus,
            self.stop_loss)


class Code(models.Model):
    code = models.CharField("股票代码", max_length=11, default='')
    name = models.CharField("股票名称", max_length=15, default='')
    area = models.CharField("股票地区", max_length=21, default='')
    industry = models.CharField("所属行业", max_length=21, default='')
    list_date = models.CharField("上市日期", max_length=10, default='')
    is_active = models.BooleanField("是否活跃", default=True)

    class Meta:
        db_table = "tb_code"

    def __str__(self):
        return "%s_%s_%s_%s_%s" % (
            self.code, self.name, self.area, self.industry, self.list_date)



