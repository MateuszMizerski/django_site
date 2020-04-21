import datetime

from time import timezone
from django.db import models


class Product(models.Model):
    type_mapping = (
        ('P', 'price'),
        ('A', 'Another'),
    )

    product_name = models.CharField(max_length=200)
    product_type = models.CharField(max_length=1, choices=type_mapping)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.product_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Product, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
