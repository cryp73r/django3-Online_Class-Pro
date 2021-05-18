from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .name import name
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import datetime, pytz
from .verify import verify
from .verifyCS import verifyCS
from .verifyIT import verifyIT
from .models import classdetailcs3334, classdetailcs3132, classdetailcs4142, classdetailcs4344, classdetailcs45, classdetailit4142, classdetailit4344
from .groupCS import groupCS
from .groupIT import groupIT
from .api_call_cs import apiCallCS
from .api_call_it import apiCallIT
from .api_call_ver import apiCallVer

# Create your views here.

session_username = ""

def home(request):
    if request.user.is_authenticated:
        return redirect('currentusr')
    else:
        return render(request, 'classdetail/home.html')

def signupusr(request):
    if request.method == 'GET':
        return render(request, 'classdetail/signup.html', {'name':name(), 'form':UserCreationForm()})
    else:
        if len(request.POST['password1']) <= 7:
            return render(request, 'classdetail/signup.html', {'name':name(), 'form':UserCreationForm(), 'error':'Required Password 8 characters long.'})
        else:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    # Create User
                    user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
                    user.save()
                    # Login User after Signup
                    login(request, user)
                    global session_username
                    session_username = request.POST['username']
                    return redirect('currentusr')
                except IntegrityError:
                    # Username Taken
                    return render(request, 'classdetail/signup.html', {'name':name(), 'form':UserCreationForm(), 'error':'Roll No. Already Registered. Try Logging in...'})
            else:
                # Passwords Missmatch
                return render(request, 'classdetail/signup.html', {'name':name(), 'form':UserCreationForm(), 'error':'Passwords didn\'t matched.'})

def loginusr(request):
    if request.method == 'GET':
        return render(request, 'classdetail/login.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'classdetail/login.html', {'form':AuthenticationForm(), 'error':'Invalid Username or Password'})
        else:
            login(request, user)
            global session_username
            session_username = request.POST['username']
            return redirect('currentusr')

@login_required
def logoutusr(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def chnpsw(request):
    if request.method == 'GET':
        return render(request, 'classdetail/chnpsw.html', {'form':UserCreationForm()})
    else:
        if len(request.POST['password1']) <= 7:
            return render(request, 'classdetail/signup.html', {'form':UserCreationForm(), 'error':'Required Password 8 characters long.'})
        else:
            if request.POST['password1'] == request.POST['password2']:
                if  session_username==request.POST['username']:   # Fixes Vulneribility
                    usr = User.objects.get(username=request.POST['username'])
                    usr.set_password(request.POST['password1'])
                    usr.save()
                    # Login again after Change
                    login(request, usr)
                    return redirect('currentusr')
                else:
                    # Vulneribility
                    return render(request, 'classdetail/chnpsw.html', {'form':UserCreationForm(), 'error':'Vulnerability Error'})
            else:
                # Passwords Missmatch
                return render(request, 'classdetail/chnpsw.html', {'form':UserCreationForm(), 'error':'Passwords didn\'t matched.'})

@login_required
def currentusr(request):
    IST = pytz.timezone('Asia/Kolkata')
    wday = datetime.datetime.now(IST).weekday()
    global session_username
    session_username = request.user.username
    branch = verify(request.user.username)[0]
    t_table = []
    if branch=='10':
        t_table = verifyCS(request.user.username, wday)
    elif branch=='13':
        t_table = verifyIT(request.user.username, wday)
    else:
        t_table = []
    ldetail = []
    temp_list=[]
    odd = False
    groupA = classdetailcs3132
    groupB = classdetailcs3334
    groupC = classdetailcs45
    if odd:
        groupA = classdetailcs3132
        groupB = classdetailcs3334
    else:
        if branch=='10':
            groupA = classdetailcs4142
            groupB = classdetailcs4344
        elif branch=='13':
            groupA = classdetailit4142
            groupB = classdetailit4344
    c = 0   # lectures counter
    d = 0   # tutes counter
    e = 0   # labs counter
    for clad in t_table:
        if odd:
            if branch=='10':
                if groupCS(request.user.username)=='3' or groupCS(request.user.username)=='4':
                    if (clad != ' ' and clad != '100'):
                        detail = groupB.objects.get(pk=int(clad))
                        ldetail.append(detail)
                        if (int(clad) <= 6):
                            c += 1
                        elif (int(clad) >= 7 and int(clad) <= 14):
                            d += 1
                        elif (int(clad) >= 15 and int(clad) <= 20):
                            if clad not in temp_list:
                                temp_list.append(clad)
                    elif (clad == '100'):
                        ldetail.append('One Hour Quiz')
                    else:
                        ldetail.append('BREAK')
                elif groupCS(request.user.username)=='1' or groupCS(request.user.username)=='2':
                    if (clad != ' ' and clad != '100'):
                        detail = groupA.objects.get(pk=int(clad))
                        ldetail.append(detail)
                        if (int(clad) <= 6):
                            c += 1
                        elif (int(clad) >= 7 and int(clad) <= 14):
                            d += 1
                        elif (int(clad) >= 15 and int(clad) <= 20):
                            if clad not in temp_list:
                                temp_list.append(clad)
                    elif (clad == '100'):
                        ldetail.append('One Hour Quiz')
                    else:
                        ldetail.append('BREAK')
            elif branch=='13':
                if groupCS(request.user.username)=='3' or groupCS(request.user.username)=='4':
                    if (clad != ' ' and clad != '100'):
                        detail = groupB.objects.get(pk=int(clad))
                        ldetail.append(detail)
                        if (int(clad) <= 6):
                            c += 1
                        elif (int(clad) >= 7 and int(clad) <= 14):
                            d += 1
                        elif (int(clad) >= 15 and int(clad) <= 20):
                            if clad not in temp_list:
                                temp_list.append(clad)
                    elif (clad == '100'):
                        ldetail.append('One Hour Quiz')
                    else:
                        ldetail.append('BREAK')
                elif groupCS(request.user.username)=='1' or groupCS(request.user.username)=='2':
                    if (clad != ' ' and clad != '100'):
                        detail = groupA.objects.get(pk=int(clad))
                        ldetail.append(detail)
                        if (int(clad) <= 6):
                            c += 1
                        elif (int(clad) >= 7 and int(clad) <= 14):
                            d += 1
                        elif (int(clad) >= 15 and int(clad) <= 20):
                            if clad not in temp_list:
                                temp_list.append(clad)
                    elif (clad == '100'):
                        ldetail.append('One Hour Quiz')
                    else:
                        ldetail.append('BREAK')

        else:
            if branch=='10':
                if groupCS(request.user.username)=='3' or groupCS(request.user.username)=='4':
                    if (clad != ' ' and clad != '100'):
                        detail = groupB.objects.get(pk=int(clad))
                        if (clad == '6' or clad == '12' or clad == '18'):
                            ldetail.append([detail, groupB.objects.get(pk=int(clad)+1)])
                        else:
                            ldetail.append(detail)
                        if (int(clad) <= 7):
                            c += 1
                        elif (int(clad) >= 8 and int(clad) <= 19):
                            d += 1
                        elif (int(clad) >= 20 and int(clad) <= 25):
                            if clad not in temp_list:
                                temp_list.append(clad)
                    elif (clad == '100'):
                        ldetail.append('One Hour Quiz')
                    else:
                        ldetail.append('BREAK')
                elif groupCS(request.user.username)=='1' or groupCS(request.user.username)=='2':
                    if (clad != ' ' and clad != '100'):
                        detail = groupA.objects.get(pk=int(clad))
                        if (clad == '6' or clad == '12' or clad == '18'):
                            ldetail.append([detail, groupA.objects.get(pk=int(clad)+1)])
                        else:
                            ldetail.append(detail)
                        if (int(clad) <= 7):
                            c += 1
                        elif (int(clad) >= 8 and int(clad) <= 19):
                            d += 1
                        elif (int(clad) >= 20 and int(clad) <= 25):
                            if clad not in temp_list:
                                temp_list.append(clad)
                    elif (clad == '100'):
                        ldetail.append('One Hour Quiz')
                    else:
                        ldetail.append('BREAK')
                elif groupCS(request.user.username)=='5':
                    if (clad != ' ' and clad != '100'):
                        detail = groupC.objects.get(pk=int(clad))
                        if (clad == '6' or clad == '12'):
                            ldetail.append([detail, groupC.objects.get(pk=int(clad)+1)])
                        else:
                            ldetail.append(detail)
                        if (int(clad) <= 7):
                            c += 1
                        elif (int(clad) >= 8 and int(clad) <= 13):
                            d += 1
                        elif (int(clad) >= 14 and int(clad) <= 16):
                            if clad not in temp_list:
                                temp_list.append(clad)
                    elif (clad == '100'):
                        ldetail.append('One Hour Quiz')
                    else:
                        ldetail.append('BREAK')
            elif branch=='13':
                if groupIT(request.user.username)=='3':
                    if (clad != ' ' and clad != '100'):
                        detail = groupB.objects.get(pk=int(clad))
                        if (clad == '6' or clad == '12'):
                            ldetail.append([detail, groupB.objects.get(pk=int(clad)+1)])
                        else:
                            ldetail.append(detail)
                        if (int(clad) <= 7):
                            c += 1
                        elif (int(clad) >= 8 and int(clad) <= 19):
                            d += 1
                        elif (int(clad) >= 20 and int(clad) <= 25):
                            if clad not in temp_list:
                                temp_list.append(clad)
                    elif (clad == '100'):
                        ldetail.append('One Hour Quiz')
                    else:
                        ldetail.append('BREAK')
                elif groupIT(request.user.username)=='4':
                    if (clad != ' ' and clad != '100'):
                        detail = groupB.objects.get(pk=int(clad))
                        if (clad == '6' or clad == '18'):
                            detail = groupB.objects.get(pk=26)
                            ldetail.append([detail, groupB.objects.get(pk=int(clad)+1)])
                        else:
                            ldetail.append(detail)
                        if (int(clad) <= 7):
                            c += 1
                        elif (int(clad) >= 8 and int(clad) <= 19):
                            d += 1
                        elif (int(clad) >= 20 and int(clad) <= 25):
                            if clad not in temp_list:
                                temp_list.append(clad)
                    elif (clad == '100'):
                        ldetail.append('One Hour Quiz')
                    else:
                        ldetail.append('BREAK')
                elif groupIT(request.user.username)=='1' or groupIT(request.user.username)=='2':
                    if (clad != ' ' and clad != '100'):
                        detail = groupA.objects.get(pk=int(clad))
                        if (clad == '6' or clad == '12' or clad == '18'):
                            ldetail.append([detail, groupA.objects.get(pk=int(clad)+1)])
                        else:
                            ldetail.append(detail)
                        if (int(clad) <= 7):
                            c += 1
                        elif (int(clad) >= 8 and int(clad) <= 19):
                            d += 1
                        elif (int(clad) >= 20 and int(clad) <= 25):
                            if clad not in temp_list:
                                temp_list.append(clad)
                    elif (clad == '100'):
                        ldetail.append('One Hour Quiz')
                    else:
                        ldetail.append('BREAK')
    e = len(temp_list)

    return render(request, 'classdetail/current.html', {'ldetail':ldetail, 'c':c, 'd':d, 'e':e})

def apiv1CS(request):
    odd = False
    IST = pytz.timezone('Asia/Kolkata')
    wday = datetime.datetime.now(IST).weekday()
    return HttpResponse(apiCallCS(odd, wday), content_type='application/json')

def apiv1IT(request):
    odd = False
    IST = pytz.timezone('Asia/Kolkata')
    wday = datetime.datetime.now(IST).weekday()
    return HttpResponse(apiCallIT(odd, wday), content_type='application/json')

def apiv1Ver(request):
    return HttpResponse(apiCallVer(), content_type='application/json')