# Generated by Django 3.2.6 on 2021-08-31 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_rename_product_article_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]