from django.shortcuts import render
from django.db import connection
from django.core.mail import send_mail
from .forms import ImageForm
from .models import Image

import random
# Create your views here.
def home(request):
    return render(request, "index.html")
def login(request):
    return render(request, "login.html")

# def profile(request):
#     email = request.POST['email']
#     username = request.POST['username']
#     fullname = request.POST['fullname']
#     bio = request.POST['bio']
#     data = {"fullname": fullname, "email": email, "bio":bio, 'username': username}
#     return render(request, "profile_img.html",data)



def signup(request):
    return render(request, "signup.html")



def update_profile(request):
    return render(request, "updateprofile.html")

def signup_page(request):
    email  = request.POST['email']
    fullname = request.POST['f_name']
    username= request.POST['user_name']
    password= request.POST['password']

    #connect  with data base server
    cursor = connection.cursor()
    query = "select * from signup where email= '"+email+"'"
    cursor.execute(query)
    cursor.fetchall()
    count = cursor.rowcount
    if count>0:
        data = {'email': "Email Already Exit ! Please Login"}
        return render(request, "second.html", data)
    else:
        otp = random.randint(1000, 9999)
        strotp = str(otp)
        #insert data into the database
        query = "insert into signup(email,fullname,username,password,created_by,otp) values (%s, %s,%s,%s,now(),%s)"
        value = (email,fullname,username,password,strotp)
        cursor.execute(query,value)

        body = 'Your Otp for our portal you signed up with email ' + email + ' is ' + strotp
        send_mail('OTP For Verification', body, 'skfashion2104@gmail.com', ['shitalkadam765@gmail.com'])
        # kamleshprajapat681@gmail.com
        # naikvasu368@gmail.com


        data = {"email": email , "fullname": fullname, "username":username,  "password": password}
        return render(request, "otp_verify.html", data)



def login_page(request):
    # login details fetch
    email = request.POST['email']
    password = request.POST['password']
    cursor = connection.cursor()
    query = "select password, is_verify from signup where email= '"+email+"'"
    cursor.execute(query)
    row = cursor.fetchall()
    if len(row) == 0:
        data = {"email": 'Email Not Valid', "password": password}
        return render(request, "second.html", data)

    password = row[0][0]
    otp_verify= row[0][1]
    if otp_verify == 1:
        if password == password:  #user succesfull login if psw is correct
            cursor = connection.cursor()
            query = "select * from signup where email= '" + email + "'"
            cursor.execute(query)
            row = cursor.fetchall()
            email    =row[0][1]
            fullname = row[0][2]
            username =row[0][3]
            bio=row[0][8]
            form = ImageForm()
            img = Image.objects.all()

            data = {"email": email,"username":username,"bio":bio,"fullname":fullname, 'img':img, 'form':form}
            return render(request, "index.html", data)

        else:
            data = {"email": "Password is Not Correct!! Please Forgot", "password": password,}
            return render(request, "second.html", data)
    else:
        data = {"email": email}
        return render(request, "otp_verify.html", data)






def otp_verify(request):
    otp1 = request.POST['otp1']
    otp2 = request.POST['otp2']
    otp3 = request.POST['otp3']
    otp4 = request.POST['otp4']
    email = request.POST['email']
    otp = str(otp1)+str(otp2)+str(otp3)+str(otp4)

    cursor = connection.cursor()
    query = "select otp from signup where email= '"+email+"'"
    cursor.execute(query)
    row = cursor.fetchone()
    print(row, "here is a row ")
    otp1= row[0]
    print(otp1, "here is a database otp")
    if otp == otp1:
        cursor = connection.cursor()
        query1="update signup set is_verify = 1 where email= '"+email+"' "
        cursor.execute(query1)
        #row1= cursor.fetchone()
        data = {"email": email, "otp": "Now you are verify user"}
        return render(request, "login.html", data)
    else:
        data = {"email": "please enter valid otp", "otp" : otp}
        return render(request, "second.html", data)
# updateprofile
def getupdatevalue (request):
    email = request.POST['email']
    fullname = request.POST['fullname']
    username = request.POST['username']
    bio = request.POST['bio']
    data = {"fullname": fullname, "email": email, 'username': username , "bio":bio}
    return render(request,"updateprofile.html",data)

def updateprofile(request):
    email=request.POST['email']
    username=request.POST['username']
    fullname=request.POST['fullname']
    bio=request.POST['Bio']
    cursor = connection.cursor()
    query1="update signup set fullname=%s ,username=%s, bio=%s where email= '"+email+"' "
    value = (fullname, username, bio)
    # form = ImageForm()
    # # img = Image.objects.all()
    cursor.execute(query1,value)
    data = {"fullname": fullname, "email": email, "bio":bio, 'username': username}
    return render(request, "second.html", data)

def search(request):
    search = request.POST['search']
    email = request.POST['email']
    fullname = request.POST['fullname']
    username = request.POST['username']
    bio = request.POST['bio']
    cursor = connection.cursor()
    ans ="%"+search+"%"
    query = "select email , username,bio from signup where username like '" +ans+ "'"
    cursor.execute(query)
    result = cursor.fetchall
    # email = result[0][0]
    # username= result[0][1]

    data = {"result":result,"fullname": fullname, "email": email, 'username': username , "bio":bio}
    return render(request, "index.html", data)


def profile_img(request):
    if request.method =="POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()

    email = request.POST['email']
    username = request.POST['username']
    fullname = request.POST['fullname']
    bio = request.POST['bio']

    data = {"fullname": fullname, "email": email, "bio":bio, 'username': username,'img':img, 'form':form}
    return render(request, "profile_img.html",data)





