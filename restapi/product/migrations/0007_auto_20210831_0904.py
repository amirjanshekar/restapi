# Generated by Django 3.2.6 on 2021-08-31 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_article_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='name',
            new_name='author_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='author_name',
        ),
    ]
