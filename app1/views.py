from django.shortcuts import render
from django.db import connection

# Create your views here.
def xyz(request):
    return render(request, "index.html")
def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


# def login(request):
#     # login details fetch
#     email1 = request.POST['email1']
#     psw1 = request.POST['psw1']
#
#     cursor = connection.cursor()
#
#     query = "select password, is_verify from signuppage where email= '"+email1+"'"
#     cursor.execute(query)
#     row = cursor.fetchall()
#     if len(row) == 0:
#         data = {"email": 'Email Not Valid', "password": psw1}
#         return render(request, "second.html", data)
#
#     password = row[0][0]
#     otp_verify= row[0][1]
#     if otp_verify == 1:
#         if psw1 == password :  #user succesfull login if psw is correct
#
#             cursor = connection.cursor()
#             query = "select * from signuppage where email= '" + email1 + "'"
#             cursor.execute(query)
#             row = cursor.fetchall()
#             fname=row[0][1]
#             lname=row[0][2]
#             phone=row[0][4]
#             data = {"email": email1, "password": psw1 , "fname":fname,"lname":lname,"phone":phone}
#             return render(request, "first.html", data)
#
#         else:
#             data = {"email": "Password is Not Correct!! Please Forgot", "password": psw1}
#             return render(request, "second.html", data)
#     else:
#         data = {"email": email1}
#         return render(request, "otp_verify.html", data)
#
#
#

