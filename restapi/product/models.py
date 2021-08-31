from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    family = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name) + ' ' + str(self.family)


class Article(models.Model):
    title = models.CharField(max_length=100)
    author_name = models.ForeignKey(Product, null=True, max_length=200, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title
