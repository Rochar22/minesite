# Generated by Django 5.1.4 on 2024-12-06 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mineapp', '0002_alter_createuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
