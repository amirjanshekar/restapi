# Generated by Django 3.2.6 on 2021-08-31 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='family',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]