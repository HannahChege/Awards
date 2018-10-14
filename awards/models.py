from django.db import models
import datetime as dt
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
class Profile(models.Model):
    username = models.CharField(max_length =30)
    bio = models.TextField()
    dp = models.ImageField( blank=True)
    posted_time = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE, primary_key=True)
   
    def __str__(self):
        return self.user.username



    def save_profile(self):
        self.save()  

    def delete_profile(self):
        self.delete()  

    @classmethod
    def update_profile(cls,update):
        pass
     
    @classmethod
    def search_by_profile(cls,name):
        profile = Profile.objects.filter(user__username__icontains=name)
        return profile 
    @classmethod 
    def get_by_id(cls,id):
        profile = Profile.objects.get(user = id)
        return profile

class Project(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to = 'images/', default='No image')
    description = models.TextField()
    posted_time = models.DateTimeField(auto_now=True) 
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    url = models.TextField()
    user=models.ForeignKey(User)
    

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


class Comments(models.Model):
       """
       Class that contains comments details
       """
       comment = HTMLField()
       posted_date = models.DateTimeField(auto_now=True)
       project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
       user = models.ForeignKey(User, on_delete=models.CASCADE,null="True")

       def __str__(self):
               return self.comment

       class Meta:
               ordering = ['posted_date']

       def save_comment(self):
               self.save()

       def del_comentm(self):
               self.delete()

       @classmethod
       def get_comments_by_image_id(cls, image):
               comments = Comments.objects.get(image_id=image)
               return comments

class MoringaMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)