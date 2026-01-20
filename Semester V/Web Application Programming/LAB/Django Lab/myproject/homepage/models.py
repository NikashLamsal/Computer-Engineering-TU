from django.db import models

# Create your models here.
class item(models.Model):
    item_name = models.CharField(max_length=100)
    item_id = models.IntegerField()
    item_description = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.item_description}'
