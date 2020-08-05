from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def about(request):
    return render(request,'about.html',{})

def services(request):
    return render(request,'services.html',{})

def opening_hour(request):
    return render(request,'opening_hour.html',{})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        # subject = request.POST['subject']
        message = request.POST['message']

         
        # send an email 
        
        send_mail(    
            message_name,
            "I'm  " + message_name + ',\n' + message + ',\n' +'by - ' + message_email,
            # message,
            message_email,
            ['nishantkkr68@gmail.com'],
            
            
            fail_silently = False
        
        )
        return render(request,'contact.html',{'message_name': message_name})
    else:
        return render(request,'contact.html',{})


def pricing(request):
    return render(request,'pricing.html',{})

def blog_home(request):
    return render(request,'blog_home.html',{})

def blog_single(request):
    return render(request,'blog_single.html',{})

