from django.shortcuts import render
from django.contrib.auth.models import  User
from person_manager.models import  Person
def add_person(request):
    context = {}
    template = "add_user.html"
    return(render(request,template,context))
def save_person(request):
    context = {}
    print("save function!")
    template = "base.html"

    last_name = request.GET['last_name']
    first_name = request.GET['first_name']
    email_address = request.GET['email_address']
    street = request.GET['street']
    city = request.GET['city']
    zip_code = request.GET['zip_code']
    state = request.GET['state']
    print(last_name,first_name,email_address,street,state,zip_code,city)
    user = User.objects.get_or_create(first_name = first_name,last_name = last_name,username = email_address,password = str(first_name) + str(last_name))
    print(user)
    print(user[0])
    person = Person.objects.get(corresponding_user = user[0])

    person.street = street
    person.city = city
    person.zip_code = zip_code
    person.state = state
    person.save()

    return(render(request,template,context))

