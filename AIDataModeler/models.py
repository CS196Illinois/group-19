from django.db import models
import datetime


# Create your models here.


class SentimentModel(models.Model):
    positivity = models.FloatField()
    negativity = models.FloatField()


class DaySentimentData(models.Model):
    date = models.DateField()

    date_str = models.SlugField()

    word_map_path = models.CharField(max_length=50, default=""); 

    overall_sentiment = models.ForeignKey(SentimentModel,
    on_delete=models.DO_NOTHING, related_name='overall')

    conservative_sentiment = models.ForeignKey(SentimentModel,
    on_delete=models.DO_NOTHING, related_name='conservative')

    liberal_sentiment = models.ForeignKey(SentimentModel,
    on_delete=models.DO_NOTHING, related_name='liberal')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.date.strftime('%m/%d/%Y')

    def save(self, *args, **kwargs):
      self.date_str = str(self.date)
      super().save(*args, **kwargs) 


#username: ngs
#username: djangotime

