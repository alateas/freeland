from django.db import models

class Food(models.Model):
    title         = models.CharField(max_length=200)
    energy        = models.FloatField()
    proteins      = models.FloatField()
    fats          = models.FloatField()
    carbohydrates = models.FloatField()
    
    def __unicode__(self):
        return self.title

class Portion(models.Model):
    food   = models.ForeignKey(Food)
    weight = models.IntegerField()

    def __unicode__(self):
        return "%s (%d g)" % (self.food.title, self.weight)