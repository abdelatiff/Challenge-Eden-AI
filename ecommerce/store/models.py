from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=30)
    Reference = models.CharField(default='145',max_length=30)
    image = models.FileField(upload_to='store/static/store/img')
    price = models.FloatField()
#    def save(self):
#        self.file_name = self.Rep.split('//')[:-1]
#        super().save(self)
    def __str__(self):
        return self.name