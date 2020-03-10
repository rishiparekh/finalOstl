from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import UserForm,ProfileForm
from .models import User,Profile

# Create your views here.
def create(request):
    return render(request,'quizapp/index.html')

#@transaction.atomic
def signupview(request):
    if request.method=="POST":
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            print("inside valid yeah !!!")
            email = user_form.cleaned_data.get('email')
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password')
            user_object = User(email=email,username=username,password=password)
            user_object.save()
            col_name = profile_form.cleaned_data.get('col_name')
            course = profile_form.cleaned_data.get('course')
            birth_date = profile_form.cleaned_data.get('birth_date')
            print(email, username, password, user_object, col_name, course, birth_date)
            prof_obj = Profile.objects.create(user = user_object,col_name=col_name,course=course,birth_date=birth_date)
            
            prof_obj.save()
            # user_form.save()

            # profile_form.save()

        return redirect("home/")
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    
    context={
        'user_form':user_form,
        'profile_form':profile_form,
    }


    
    return render(request, 'quizapp/signin.html',context)


def HomeView(request):
    return render(request,"quizapp/home.html")