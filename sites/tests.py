from django.test import TestCase
from .models import *
import datetime as dt

# Create your tests here.
class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.user = User(id=1,password='jose123',email='jose@gmail.com',first_name='joseph',last_name='shitandi')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        
    # Testing Save Method
    def test_save_method(self):
        self.user.save_user()
        user = User.objects.all()
        self.assertTrue(len(user) > 0)
        
    def test_delete_user(self):
        self.user.delete_user()
        user = User.objects.all()
        self.assertTrue(len(user)== 0) 
        
    def test_update_user(self):
        self.user.save_user()
        self.user.update_user(self.user.id, 'Joseph')
        changed_user = User.objects.filter(last_name ='Joseph')
        self.assertTrue(len(changed_user) > 0)  
    
    # def test_email_user(self, subject, message, from_email=None, **kwargs):
    #     self.user.save_user()
    #     self.user.email_user(subject='Welcome',)
    #     changed_user = User.objects.filter(username ='Joseph')
    #     self.assertTrue(len(changed_user) > 0)     

class ProfileTestClass(TestCase):
    
    #  Saving user instance
    def setUp(self):
        self.user = User(id=1,password='jose123',email='jose@gmail.com',first_name='joseph',last_name='shitandi')
        self.user.save_user()

    
        self.profile = Profile(id=1,email="joseph@gmail.com",user=self.user,name="joseph",status=True)
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        
    # Testing Save Method
    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)
        
    def test_delete_profile(self):
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)== 0) 
        
    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile(self.profile.id, 'Joseph')
        changed_profile = Profile.objects.filter(name ='Joseph')
        self.assertTrue(len(changed_profile) > 0)        
        