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

    @property
    def energy(self):
        return round((self.food.energy / 100) * self.weight, 1)

    @property
    def proteins(self):
        return round((self.food.proteins / 100) * self.weight, 1)

    @property
    def fats(self):
        return round((self.food.fats / 100) * self.weight, 1)

    @property
    def carbohydrates(self):
        return round((self.food.carbohydrates / 100) * self.weight, 1)