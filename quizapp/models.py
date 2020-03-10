from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):

    COLLEGES = (
        ('D.J Sanghvi','D.J Sanghvi'),
        ('IIT Powai','IIT Powai'),
        ('IIIT Delhi','IIIT Delhi'),
        ('VJTI','VJTI'),

    )

    course = models.CharField(max_length = 3)
    col_name =models.CharField("College Name:",max_length=20,choices= COLLEGES)
    birth_date = models.DateField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()




class Subject(models.Model):
    name = models.CharField(max_length=10)
    

    def __str__(self):
        return self.name

class Tests(models.Model):
    name=models.CharField("Name of Test",max_length=20)
    subs=models.ManyToManyField(Subject)
    # SUBJECT_CHOICES=(
    #     ('Physics','Physics'),
    #     ('Chemistry','Chemistry'),
    #     ('Maths','Maths'),
    # )

    # sub = MultiSelectField(choices=SUBJECT_CHOICES,max_choices=3)

    def __str__(self):
        return self.name

class Questions(models.Model):

    question_description = models.TextField()
    tests = models.ForeignKey(Tests,on_delete=models.CASCADE)
    question_number=models.CharField(max_length=2)

    CHOICES = (
        ('choice_1','A'),
        ('choice_2','B'),
        ('choice_3','C'),
        ('choice_4','D'),

        )

    choice_1 = models.TextField()
    choice_2 = models.TextField()
    choice_3 = models.TextField()
    choice_4 = models.TextField()

    correct_choice = models.CharField(

        max_length = 10,
        choices = CHOICES
    )

    def __str__(self):
        return self.question_number


    



