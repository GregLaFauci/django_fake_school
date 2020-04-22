import os
#configure settings for a project
#Need to run this before calling models from application 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_system.settings')

import django
#import settings
django.setup()

import random
from my_app.models import Student
from faker import Faker

fakegen = Faker()

def populate(N=5):
    sub_list = ['Mathematics','Biology','Geometry','Martial Arts','Physics']

    '''
    Create N Students to add 
    '''
    for entry in range(N):
        fake_name = fakegen.name().split()
        firstName = fake_name[0]
        lastName = fake_name[1]
        fakeemail = fakegen.email()
        rand_subject = random.choice(sub_list)

        #enter the data into a database
        student_crt = Student.objects.get_or_create(
            first_name=firstName,
            last_name=lastName,
            email=fakeemail,
            subject=rand_subject,
            )[0]

       
if __name__ == '__main__':
    print('Populating the db... please, wait')
    populate(100)
    print('Polpulating Complete!')