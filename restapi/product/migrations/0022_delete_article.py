# Generated by Django 3.2.6 on 2021-08-31 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_article_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
    ]