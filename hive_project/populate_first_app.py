import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hive_project.settings')
import django
django.setup()


import random
from faker import Faker
from first_app.models import UserProfile ,Post
from django.contrib.auth.models import User



fakegen = Faker()

def populate(N=10):
  for nmber_users in range(N):
    fake_first_name  = fakegen.first_name()
    fake_last_name = fakegen.last_name()
    fake_username = fakegen.user_name()
    fake_password  = fakegen.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    fake_email     = fakegen.email()

    user =  User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, username=fake_username, password= fake_password, email= fake_email)[0]

  #def create_user_profile_info():
    fake_bio = fakegen.text(max_nb_chars=160)
    userprofile_info = UserProfile.objects.get_or_create(user = user, bio = fake_bio)[0]

    for nmber_post in range(random.randint(0,25)):
  #def create_tweet():
      fake_text  = fakegen.text(max_nb_chars=140)
      fake_date  = fakegen.date(pattern='%Y-%m-%d')

      post = Post.objects.get_or_create(text=fake_text, date=fake_date, user=userprofile_info)[0]


#def populate():
#  signups = []
  
if __name__ == '__main__':
  print('Starting to populate...')
  populate(20)
  print('Finished populating!')
  









