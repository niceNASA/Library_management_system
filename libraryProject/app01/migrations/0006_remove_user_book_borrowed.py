# Generated by Django 3.2.6 on 2021-08-06 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_rename_book_nums_user_book_borrowed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='book_borrowed',
        ),
    ]
