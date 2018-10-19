from django.db import models
import datetime as dt
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver



@receiver(post_save,sender=User)
def create_profile(sender, instance,created,**kwargs):
   if created:
       Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender, instance,**kwargs):
   instance.profile.save()
# Create your models here.

class Project(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to = 'images/', default='No image')
    description = models.TextField()
    posted_time = models.DateTimeField(auto_now=True) 
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    url = models.TextField()
    user=models.ForeignKey(User)
    rating = models.TextField()
    

    def save_project(self):
        self.save()
    def delete_project(self):
        self.delete()    
    
    @classmethod
    def get_all_projects(cls):
        projects = Image.objects.all()
        return projects 
    
    @classmethod
    def get_project_by_id(cls, id):
        project = cls.objects.filter(id=id).all()
        return project     
    @classmethod
    def get_profile_pic(cls,profile):
        projects = Project.objects.filter(profile__pk = profile)
        return projects
        pass
      
    def display_projects(cls):
        projects=cls.objects.all()
        return projects

    @classmethod
    def search_profile(cls, query):
       profile = cls.objects.filter(user__username__icontains=query)
       return profile
    

    @classmethod
    def all_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_single_project(cls, project_id):
        return cls.objects.get(pk=project_id)

    def average_design(self):
        all_ratings = list(map(lambda x: x.rating, self.designrating_set.all()))
        return np.mean(all_ratings)

    def average_usability(self):
        all_ratings = list(map(lambda x: x.rating, self.usabilityrating_set.all()))
        return np.mean(all_ratings)

    def average_content(self):
        all_ratings = list(map(lambda x: x.rating, self.contentrating_set.all()))
        return np.mean(all_ratings)

    def __str__(self):
        return self.title

class DesignRating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)


class UsabilityRating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)


class ContentRating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)
