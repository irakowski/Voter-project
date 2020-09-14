import datetime

from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Category(models.Model):
    """
    Representation of the category db table
    """
    name = models.CharField(max_length=160)
    slug = models.SlugField(max_length=160)
    question = models.ManyToManyField(Question)
    description = models.TextField()
    
    def __str__(self):
        """
        Returns human-readable category name
        """
        return self.name

    def save(self, *args, **kwargs):
        """
        Automatically creates slug for category name
        """
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)        
        