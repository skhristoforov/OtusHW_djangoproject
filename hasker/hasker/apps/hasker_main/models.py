from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class HaskerTag(models.Model):
    tag = models.SlugField(max_length=32, unique=True)

    def __str__(self):
        return '#' + self.tag

    def __unicode__(self):
        return str(self)


class HaskerUser(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    date = models.DateTimeField('date published', default=datetime.now)
    email = models.EmailField(primary_key=True)

    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='hasker_main/static/profile_images', blank=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return str(self)


class HaskerQuestion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    # author = models.ForeignKey(HaskerUser)
    date = models.DateTimeField('date published', default=datetime.now)
    title = models.CharField(max_length=128)
    text = models.TextField()
    votes = models.IntegerField(default=0)
    tags = models.ManyToManyField(HaskerTag, max_length=3)

    def __str__(self):
        return str(self.id) + ' ' + str(self.title)

    def __unicode__(self):
        return str(self)


class HaskerAnswer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField('date published', default=datetime.now)
    # author = models.ForeignKey(HaskerUser)
    text = models.TextField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + ' '

    def __unicode__(self):
        return str(self)