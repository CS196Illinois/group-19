from django.db import models
import datetime


# Create your models here.


class OutletSentiment(models.Model):
    cnn = models.FloatField()
    politico = models.FloatField()
    usa_today = models.FloatField()
    upi = models.FloatField()
    federalist = models.FloatField()
    average = models.FloatField()
    average_consevative = models.FloatField()
    average_liberal = models.FloatField()


class DaySentimentData(models.Model):
    date = models.DateField()

    date_str = models.SlugField()

    word_map_path = models.CharField(max_length=50, default=""); 

    outlet_sentiment = models.ForeignKey(OutletSentiment,
                                          on_delete=models.DO_NOTHING, null=True, blank=True, related_name='sentiment')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.date.strftime('%m/%d/%Y')

    def save(self, *args, **kwargs):
      self.date_str = str(self.date)
      super().save(*args, **kwargs) 


#username: ngs
#pass: djangotime

