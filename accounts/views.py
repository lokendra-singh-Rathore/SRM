from django.core import paginator
from django.shortcuts import render, redirect 
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import *
from django.contrib.auth import login as dj_login,authenticate
from django.contrib import messages
import urllib
from .filters import Feefilter
from django.core.paginator import Paginator


def home(request):
	orders = Topic.objects.all()
	customers = Student.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending,'total_customers' :total_customers}

	return render(request, 'Trainer/dashboard.html', context)

def products(request):
	products = Trainer.objects.all()

	return render(request, 'Trainer/products.html', {'products':products})

def view_profile(request, pk_test):
	student = Student.objects.get(id=pk_test)
	topics = student.topic_set.all()
	fees=student.fee_set.all()
	order_count = topics.count()

	context = {'student':student, 'topics':topics, 'order_count':order_count,'fees':fees}
	return render(request, 'Trainer/class_and_fee_data.html',context)


def add_class(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			form = OrderForm()
			

	context = {'form':form}
	return render(request, 'Trainer/add_class.html', context)

def Add_fee(request):
	form = FeeForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = FeeForm(request.POST)
		if form.is_valid():
			form.save()
			form = FeeForm()
			

	context = {'form':form}
	return render(request, 'Trainer/fee_form.html', context)

def updateclass(request, pk):

	order = Topic.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {'form':form}
	return render(request, 'Trainer/add_class.html', context)

def deleteorder(request, pk):
	order = Topic.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('home')

	context = {'item':order}
	return render(request, 'Trainer/delete.html', context)



def add_student(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request,'Trainer/add_student.html',context)

def view_student(request,pk):
	View_student=Student.objects.get(id=pk)
	context={'View_student':View_student}
	return render(request,'Trainer/view_profile.html',context)


def studentlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        User=authenticate(request,username=username,password=password)
        if User is not None:
			#student = Student.objects.get(id=pk_test)
            use=username
            student= Student.objects.get(Father_Contact_no=use)
            topics = student.topic_set.all()
            
            fees=student.fee_set.all()
            order_count = topics.count()
            context = {'student':student, 'topics':topics, 'order_count':order_count,'fees':fees}
            dj_login(request,User)
            return render(request,'Student/user.html',context)
        else:
            messages.info(request,'id or password is wrong')
            return render(request,'Trainer/login.html')
            
    return render(request,'Trainer/login.html')

def user(request):
	return render(request,'Student/user.html') 

def bookdemo(request):
	form=demoform()
	if request.method=='POST':
		form=demoform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	print(form.errors)
	context={'form':form}
	return render(request,'Trainer/bookdemo.html',context)


def contact(request):
	form=contactform()
	if request.method=='POST':
		form=contactform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	print(form.errors)
	context={'form':form}
	return render(request,'Trainer/contact.html',context) 

def View_fee(request):
	fees=Fee.objects.all().order_by('id')
	myfilter=Feefilter(request.GET, queryset=fees)
	fees=myfilter.qs
	
	paginator=Paginator(fees,10)
	page_number=request.GET.get('page')
	page_fee=paginator.get_page(page_number)
	context={'fees':page_fee,'myfilter':myfilter}
	return render(request,'Trainer/view_fee.html',context)