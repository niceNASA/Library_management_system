# Generated by Django 3.2.6 on 2021-08-06 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_alter_user_book_nums'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='book_nums',
            new_name='book_borrowed',
        ),
    ]
