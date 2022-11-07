from django.db import models

# Create your models here.
class CryptoAnalyzerAnalysisImageModel(models.Model):
    image_url = models.CharField(max_length=300, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    

