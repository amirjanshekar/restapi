# Generated by Django 3.2.6 on 2021-08-31 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_article_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author_name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]