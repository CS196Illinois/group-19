from django.db import models
import datetime


# Create your models here.

class SentimentManager(models.Manager):
    def get_by_natural_key(self, unique_key_name, average):
        return self.get(unique_key_name=unique_key_name, average=average)

class OutletSentiment(models.Model):
    unique_key_name = models.CharField(max_length=50, unique=True); 
    cnn = models.FloatField()
    politico = models.FloatField()
    usa_today = models.FloatField()
    upi = models.FloatField()
    federalist = models.FloatField()
    average = models.FloatField()
    average_consevative = models.FloatField()
    average_liberal = models.FloatField()

    objects = SentimentManager()

    def natural_key(self):
        return (self.cnn, self.politico, self.usa_today, self.upi, self.federalist, 
          self.average, self.average_consevative, self.average_liberal)


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

