# Generated by Django 3.2.6 on 2021-08-06 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='book_nums',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.book'),
        ),
    ]
