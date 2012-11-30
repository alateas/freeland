from django.db import models

class Groceries(models.Model):
    title         = models.CharField(max_length=200)
    energy        = models.FloatField()
    proteins      = models.FloatField()
    fats          = models.FloatField()
    carbohydrates = models.FloatField()

    def __unicode__(self):
        return self.title