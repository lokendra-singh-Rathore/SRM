from django.db import models
from django.db.models.base import Model
from django.db.models.fields import AutoField, DateField
from django.forms.widgets import DateInput

# Create your models here.

class Student(models.Model):
    Student_name=models.CharField(max_length=50,null=True)
    Class=models.FloatField(max_length=10,null=True,blank=True)
    Father_name=models.CharField(max_length=50,null=True,)
    Mother_name=models.CharField(max_length=50,null=True)
    School_name=models.CharField(max_length=50,null=True)
    Father_Contact_no=models.IntegerField()
    Mother_Contact_no=models.IntegerField()
    Email=models.CharField(max_length=30,null=True,blank=True)
    Address=models.CharField(max_length=100,null=True,blank=True)
    Father_occupation=models.CharField(max_length=100,null=True,blank=True)
    Mother_occupation=models.CharField(max_length=100,null=True,blank=True)
    DOB=models.DateField(null=True,blank=True)
    Date_joined=DateField(null=True,auto_now_add=True,blank=True)
    GENDER=(
        ('Male','Male'), 
        ('Female','female'),
        ('Other','Other')
    )
    Gender=models.CharField(max_length=50,null=True,choices=GENDER)

    def __str__(self):
        return self.Student_name
	


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Trainer(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Topic(models.Model):
	student = models.ForeignKey(Student, null=True, on_delete= models.SET_NULL)
	trainer = models.ForeignKey(Trainer, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True)


class Fee(models.Model):
    Mode = (
			('Cash', 'Cash'),
			('Card', 'Card'),
			('Paytm', 'Paytm'),
			) 
    student = models.ForeignKey(Student, null=True, on_delete= models.SET_NULL)
    payment_mode = models.CharField(max_length=200, null=True, choices=Mode)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    total_amount=models.IntegerField()
    paid_amount=models.IntegerField()
    upcoming_Due_Date=models.DateTimeField( null=True)


class Studentlogin(models.Model):
    student = models.ForeignKey(Student, null=True, on_delete= models.SET_NULL)
    trainer = models.ForeignKey(Trainer, null=True, on_delete= models.SET_NULL)
    name2=models.CharField(max_length=40,null=True)

class bookdemo(models.Model):
    your_name=models.CharField(max_length=100,null=True)
    student_name=models.CharField(max_length=100,null=True)
    contact=models.IntegerField(null=True)
    school_name=models.CharField(max_length=100,null=True)
    msg=models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.your_name


class contact(models.Model):
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    email=models.EmailField(null=True)
    phone=models.IntegerField(null=True)
    msg=models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.first_name


class image(models.Model):
    student_name=models.CharField(max_length=50,null=True)
    project_name=models.CharField(max_length=50,null=True)
    project_image=models.ImageField(upload_to='static/images/gallery')

    def __str__(self):
        return self.student_name