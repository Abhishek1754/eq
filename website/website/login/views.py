from django.shortcuts import render
import mysql.connector as sql
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

class UserViewSet (viewsets.ModelViewSet):
    permission_classes=(IsAuthenticated,)
    serializer_class=UserSerializer
queryset=get_user_model().objects.all()



em=''
pwd=''

def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Abhishek123456",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
                if key=="password":
                    pwd=value

                    c="select * from users where emails='{} and passwords='{}'".format(em,pwd)
                    cursor.execute(c)
                    t=tuple(cursor.fetchall())
                    if t==():
                        return render(request,'error.html')
                    else:
                        return render(request,'welcome.html')
            return render(request,'login_page.html')

 


        
            
                        
                    
                        

                


    
