import json
import io
import numpy as np
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from UserApi.forms import UserProfileForm, UserLoginForm
from .models import UserDetail, CodeDetail


@csrf_exempt
def user_register(request):
    context = RequestContext(request)
    if request.method == "POST":
        upf = UserProfileForm(data=request.POST)
        upf.save()
        return redirect('/')
    else:
        user_profile = UserProfileForm()
        return render(request, 'UserApi/signup.html', {'user_profile': user_profile}, context)


@csrf_exempt
def admin_register(request):
    context = RequestContext(request)
    if request.method == "POST":
        upf = UserProfileForm(data=request.POST)
        upf.save()
        return redirect('/')
    else:
        user_profile = UserProfileForm()
        return render(request, 'UserApi/signup.html', {'user_profile': user_profile}, context)


@csrf_exempt
def code_view(request):
    if request.method == "POST":
        x = int(request.POST.get('x'))
        for i in range(x):
            code_detail = CodeDetail()
            code_detail.code = CodeDetail.generate_uniq_code()
            code_detail.save()
        return redirect('/dashboard')
    else:
        return render(request, 'UserApi/homepage.html')


@csrf_exempt
def dashboard(request):
    #print(args)
    code_list = CodeDetail.objects.filter(count__gte=1)
    list_list = []
    for i in code_list:
        val_dict = {}
        val_dict['code'] = i.code
        val_dict['count'] = i.count
        val_dict['status'] = i.status
        list_list.append(val_dict)
    return render(request, 'UserApi/dashboard.html', {'code_list': list_list, 'user_type': "true"})


@csrf_exempt
def code_used_count(request):
    try:
        code = request.GET.get('code')
        if CodeDetail.objects.get(code=code) is not None:
            code_detail = CodeDetail.objects.get(code=code)
            code_detail.count = code_detail.count + 1
            code_detail.status = 'used'
            code_detail.save()
            return HttpResponse(json.dumps({'status': True, 'message': 'API called successfully'}),
                                content_type='application/json')
        else:
            return HttpResponse(
                json.dumps({'status': False, 'error': 'data not saved'}), content_type='application/json')

    except ObjectDoesNotExist:
        return HttpResponse(
            json.dumps({'status': False, 'error': 'This app does not exist in our database'}),
            content_type='application/json')


def login(request):
    if request.method == "POST":
        data = request.POST
        email = request.POST.get('email')
        s = UserDetail.objects.filter(email=email)
        if s.count() == 0:
            return HttpResponse("Enter valid email & password")
        if s[0].password != data['password']:
            return HttpResponse("Enter valid email & password")

        else:
            return redirect('/dashboard')

    else:
        user = UserLoginForm()
        return render(request, 'UserApi/login.html', {'user': user})


def generate_csv(request):
    data = CodeDetail.objects.all()
    list_list = []
    header = ['Api_url','count', 'status']
    list_list.append(header)
    for i in data:
        value_list = []
        value_list.append('http://127.0.0.1:8000/code_used_count?code={}'.format(i.code))
        value_list.append(i.count)
        value_list.append(i.status)

        list_list.append(value_list)

    np.savetxt("file_name.csv", list_list, delimiter=",", fmt='%s')

    # return HttpResponse("csv file downloaded")
    with open('file_name.csv', 'rb') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=file_name.csv'
        return response
