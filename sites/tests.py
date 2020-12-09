from django.test import TestCase
from .models import *
import datetime as dt

# Create your tests here.
class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.user = User(id=1,password='jose123',email='jose@gmail.com',username='shitandi',first_name='joseph',last_name='shitandi')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        
    # Testing Save Method
    def test_save_method(self):
        self.user.save_user()
        user = User.objects.all()
        self.assertTrue(len(user) > 0)
        