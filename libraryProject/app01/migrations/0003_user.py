# Generated by Django 3.2.6 on 2021-08-06 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
                ('book_nums', models.IntegerField(default=0, verbose_name='借书数')),
            ],
        ),
    ]
