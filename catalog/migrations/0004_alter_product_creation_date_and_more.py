# Generated by Django 4.2.1 on 2023-05-10 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_category_product_delete_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='creation_date',
            field=models.DateField(verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_modified_date',
            field=models.DateField(verbose_name='Дата последнего изменения'),
        ),
    ]
