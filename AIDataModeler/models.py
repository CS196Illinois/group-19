from django.db import models


# Create your models here.


class SentimentModel(models.Model):
    positivity = models.FloatField()
    negativity = models.FloatField()


class DaySentimentData(models.Model):
    date = models.DateField()
    overall_sentiment = models.ForeignKey(SentimentModel, on_delete=models.DO_NOTHING, related_name='overall')
    conservative_sentiment = models.ForeignKey(SentimentModel, on_delete=models.DO_NOTHING, related_name='conservative')
    liberal_sentiment = models.ForeignKey(SentimentModel, on_delete=models.DO_NOTHING, related_name='liberal')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


#username: ngs
#username: djangotime

