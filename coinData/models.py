from django.db import models

# Create your models here.
class coinsSupportedCoinListModel(models.Model):
    coin_id = models.CharField(max_length=100, unique=True)
    symbol = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True)
    coin_slug = models.CharField(max_length=100, unique=True)

    #images
    thumb = models.CharField(max_length=300, unique=True)
    small = models.CharField(max_length=300, unique=True)
    large = models.CharField(max_length=300, unique=True)

    is_supported = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name









