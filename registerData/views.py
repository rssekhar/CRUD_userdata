from django.shortcuts import render,redirect

from registerData.form import UserForm
from registerData.models import User

# Create your views here.


def index(request):

    if request.method=="POST":
        form=UserForm(request.POST)

        if form.is_valid():
            form.save() #persist data in database, using queryset(Django ORM API) method==> create
            return redirect('/show')
        else:
            pass
    else:
        obj=UserForm() #GET request, Empty form
        return render(request,'index.html',{'usa':obj}) #HTTP GET method for displaying empty form

def show(request):  
    #name="TTL"
    dummyusers=User.objects.all()    
    return render(request,"show.html",{'usa_list':dummyusers})  

def edit(request,id):
    usa = User.objects.get(id=id)
    return render(request,"edit.html",{'usa':usa})
    

def update(request,id):
    usa = User.objects.get(id=id)
    form = UserForm(request.POST,instance=usa)
    if form.is_valid():
        form.save()
        return redirect('/show')

    return render(request,'edit.html',{'usa':usa})

def destroy(request,id):
    usa = User.objects.get(id=id)
    usa.delete()
    return redirect('/show')