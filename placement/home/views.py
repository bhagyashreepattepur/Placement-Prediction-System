
from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import signup
#import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def plscement(request):
    return render(request,"plscement.html")

def register(request):
    if request.method=='POST':
        usern=request.POST['usrname']
        pasd=request.POST['password']
        DOB=request.POST['DOB']
        gender=request.POST['gender']
        phone=request.POST['phone']
        place=request.POST['place']
        user=signup.objects.create(username=usern,password=pasd,DOB=DOB,gender=gender,phone=phone,place=place)
        user.save()
        return redirect("login")
    else:
        return render(request,"register.html")
def home(request):
    return render(request,"home.html")

def login(request):
    if request.method=="POST":
        usern=request.POST['uname']
        pasd=request.POST['Password']
        if signup.objects.filter(username=usern).exists():
            if signup.objects.filter(password=pasd).exists():
                return redirect('plscement')
            else:
                message.info(request,'Incorrect Password')
                return render(request,'login.html')
        else:
            message.info(request,'Incorrect Username')
            return render(request,'login.html')
    else:
        return render(request,"login.html")

def plscement(request):
    if request.method=='POST':
        cgpa=float(request.POST['CGPA'])
        tenth=int(request.POST['Tenth'])
        twelth=int(request.POST['Twelth'])
        amcat=int(request.POST['AMCAT'])

        df=pd.read_csv("static/dataset/data.csv")
        x=df.drop(["PLACED",'PCOUNT'],axis=1)
        y=df["PLACED"]
        X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.45)
        log=RandomForestClassifier()
        log.fit(X_train,y_train)
        pred=log.predict([[tenth,twelth,cgpa,amcat]])
        result=''
        if pred==1:
            result="You are eligible"
        else:
            result="You are not eligible"
        return render(request,"plscement.html",{"result":result})
    else:
        return render(request,"plscement.html")