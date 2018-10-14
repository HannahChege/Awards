from django.test import TestCase
from .models import Profile, Project
from django.contrib.auth.models import User


class ProfileTestClass(TestCase):
    """
    Test profile class and its functions
    """
    def setUp(self):

        self.user = User.objects.create(id =1,username='hannah')
        self.profile = Profile(dp='hannah.jpg', bio='Life is too short', contact="0711139310",user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        """
        Function to test that profile is being saved
        """
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        """
        Function to test that a profile can be deleted
        """
        self.profile.save_profile()
        

    # def test_update_method(self):
    #     """
    #     Function to test that a profile's details can be updated
    #     """
    #     self.profile.save_profile()
    #     new_profile = Profile.objects.filter(bio='LIfe is too short').update(bio='You only live once')

    
    # def test_get_profile_by_id(self):
    #     """
    #     Function to test if you can get a profile by its id
    #     """
    #     self.profile.save_profile()
    #     this_pro= self.profile.get_by_id(self.profile.user_id)
    #     profile = Profile.objects.get(user_id=self.profile.user_id)
    #     self.assertTrue(this_pro, profile)



# class ProjectTestClass(TestCase):
#     """
#     Test project class and its functions
#     """
#     def setUp(self):

#         self.user = User.objects.create(id =1,username='a')
#         #creating an new profile
#         self.profile = Profile(profile_pic='hii.jpg', bio='This is me', contact="1234567",user=self.user)
#         self.profile.save_profile()
#         self.project = Project(title='projects',landing_page='land.jpg', description='This projects', link='https://www.test.com', profile=self.profile, user=self.user)

#     def test_instance(self):
#         self.assertTrue(isinstance(self.project, Project))

#     def test_save_method(self):
#         """
#         Function to test that project is being saved
#         """
#         self.project.save_pro()
#         projects = Project.objects.all()
#         self.assertTrue(len(projects) > 0)

#     def test_delete_method(self):
#         """
#         Function to test that a project can be deleted
#         """
#         self.project.save_pro()
#         self.project.del_pro()

#     def test_update_method(self):
#         """
#         Function to test that a project's details can be updated
#         """
#         self.project.save_pro()
#         new_project = Project.objects.filter(title='projects').update(title='New one')
#         projects = Project.objects.get(title='New one')
#         self.assertTrue(projects.title, 'New one')
