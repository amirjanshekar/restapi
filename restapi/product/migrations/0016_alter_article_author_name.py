# Generated by Django 3.2.6 on 2021-08-31 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_article_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product', verbose_name='name'),
        ),
    ]