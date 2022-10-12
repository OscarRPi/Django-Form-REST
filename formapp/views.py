# formapp/views.py

import json

from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from formapp.models import Data_User

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from formapp.forms import DataForm

class UserView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    #Para enviar al cliente
    def get(self,request,id=0):
        
        if (id>0):
            users = list(Data_User.objects.filter(id_usuario=id).values())
            if( len(users) > 0 ):
                user=users[0]
                datos = {'message':"Success",'users':user}
            else:
                datos = {'message':"User not found..."}    
        else:
            users = list(Data_User.objects.values())
            if len(users)>0:
                datos = {'message':"Success",'users':users}
            else:
                datos = {'message':"Users not found..."}
                
        response = JsonResponse(datos)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    
    def post(self,request):
        
        jd = json.loads(request.body)
        
        Data_User.objects.create(
            nombres   = jd[0]['nombres'],
            apellidos = jd[0]['apellidos'],
            correo    = jd[0]['correo'],
            ciudad    = jd[0]['ciudad'],
        )
        
        datos = {'message':"Success"}
        response = JsonResponse(datos)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    
    def put(self,request, id):
        
        jd = json.loads(request.body)
        users = list(Data_User.objects.filter(id_usuario=id).values())
        
        if( len(users) > 0 ):
                    
            user = Data_User.objects.get(id_usuario=id)
            
            user.nombres    = jd[0]['nombres'],
            user.apellidos  = jd[0]['apellidos']
            user.correo     = jd[0]['correo']
            user.ciudad     = jd[0]['ciudad']

            user.save()

            datos = {'message':"Success"}
        
        else:
            datos = {'message':"User not found..."} 
            
        response = JsonResponse(datos)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    
    def delete(self,request, id):
        
        users = list(Data_User.objects.filter(id_usuario=id).values())
        if( len(users) > 0 ):
            Data_User.objects.filter(id_usuario=id).delete()
            datos = {'message':"Success"}
        else:
            datos = {'message':"User not found..."}
            
        response = JsonResponse(datos)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    
    
'''


def create(request):  
    if request.method == "POST":  
        
        form = DataForm(request.POST)  
                    
        if form.is_valid():  
            try:
                form.save()  
                return redirect('/')
            except:
                pass
    else:  
        form = DataForm()  
    return render(request,'formapp/form.html',{'form':form}) 

def read(request):  
    users = Data_User.objects.all()  
    return render(request,"formapp/index.html",{'users':users})  

def update(request, id):  
    user = Data_User.objects.get(id_usuario=id)  
    form = DataForm(request.POST, instance = user)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'formapp/edit.html', {'user': user}) 

def edit(request, id):  
    user = Data_User.objects.get(id_usuario=id)  
    return render(request,'formapp/edit.html', {'user':user})  

def delete(request, id):  
    user = Data_User.objects.get(id_usuario=id)  
    user.delete()  
    return redirect("/")



'''