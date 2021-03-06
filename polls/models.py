import datetime

from django.db import models
from django.utils import timezone
from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)


class Question(models.Model):
    question = models.Manager()
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    categories = models.ManyToManyField(Category)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.question_text)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def get_categories(self):
        return " ".join([p.title for p in self.categories.all()])


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)


