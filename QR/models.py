from django.db import models

# Create your models here.
class QRCode(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(verbose_name="Codigo QR")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Código QR"
        verbose_name_plural = "Códigos QR"
        ordering = ['created_at']
    
    def __str__(self):
        return (self.name)