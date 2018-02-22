# _*_ coding:utf-8 _*_
from django.shortcuts import render
from .models import UserMassage
# Create your views here.

def getform(request):
    # all_messages = UserMassage.objects.all()
    # for message in all_messages():
    #     print(message.name)

    # if request.method == 'POST':
    #     name = request.POST.get('name','')
    #     message = request.POST.get('message','')
    #     address = request.POST.get('address','')
    #     email = request.POST.get("email",'')
    #     user_message = UserMassage()
    #     user_message.name = name
    #     user_message.massage = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message .save()

    message = None
    all_message = UserMassage.objects.filter(name = '童壮')
    if all_message:
        message = all_message[0]


    return render(request,'massageform.html',{
        'my_message':message
    })