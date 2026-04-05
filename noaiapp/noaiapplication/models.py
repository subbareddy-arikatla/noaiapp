from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField(default=4) 
    phonenumber=models.CharField(max_length=20,null=True,blank=True)

class Musian(models.Model):
    first_name=models.CharField(max_length=50, blank=False)
    last_name=models.CharField(max_length=50, null=True, blank=False)
    instrument=models.CharField(max_length=100)

class Album(models.Model):
    artist=models.ForeignKey(Musian,on_delete=models.CASCADE)
    name=models.CharField(max_length=100 ,blank=False)
    release_date=models.DateField()
    num_stars=models.IntegerField()

class Person(models.Model):
    SHIRT_SIZES={
        'S':'small',
        'M':'medium',
        'L':'Large',
    }
    name=models.CharField(max_length=60)
    shirt_size=models.CharField(max_length=1,choices=SHIRT_SIZES)
class Runner(models.Model):
    medalType=models.TextChoices('medalType','GOLD SLIVER BRONZE')
    name=models.CharField(max_length=60)
    medal=models.CharField(blank=True, choices=medalType, max_length=10)
class Apple(models.Model):
    name=models.CharField(max_length=45,primary_key=True)


# poll=models.ForeignKey(Poll,on_delete=models.CASCADE,verbose_name='the related poll')
# sites=models.ManyToManyField(Site,verbose_name='list of sites')
# place=models.OneToOneField(
#     place,
#     on_delete=models.CASCADE,
#     verbose_name='related place',
# )
class Manufacture(models.Model):
    #...
    pass
class Car(models.Model):
    manufacturer=models.ForeignKey(Manufacture,on_delete=models.CASCADE)

class Person(models.Model):
    name=models.CharField(max_length=128)
    def __str__(self):
        return self.name
class Group(models.Model):
    name=models.CharField(max_length=128)
    members=models.ManyToManyField(Person,through='Membership')

class MemberShip(models.Model):
    person=models.ForeignKey(Person,on_delete=models.CASCADE)
    group=models.ForeignKey(Group,on_delete=models.CASCADE)
    date_joined=models.DateField()
    invite_reason=models.CharField(max_length=64)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["person", "group"], name="unique_person_group"
            )
        ]
class Question(models.Model):
    question_name=models.TextField()
    question_type=models.CharField(max_length=255)
    question_category=models.CharField(max_length=255)
    option_a=models.CharField(max_length=255)
    option_b=models.CharField(max_length=255)
    option_c=models.CharField(max_length=255)
    option_d=models.CharField(max_length=255)
    correct_ans=models.CharField(max_length=255)