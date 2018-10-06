import json
import traceback

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import UserDetail, CodeDetail


@csrf_exempt
def user_registration(request):
    try:
        print(request.body)
        user_data = UserDetail()
        user_data.name = request.POST.get('name')
        user_data.email = request.POST.get('email')
        user_data.user_type = request.POST.get('user_type')
        user_data.password = request.POST.get('password')
        user_data.save()
        return HttpResponse(json.dumps({'status': True, 'message': 'user registered successfully'}),
                            content_type='application/json')
    except Exception as err:
        traceback.print_tb(err.__traceback__)
        return HttpResponse(
            json.dumps({'status': False, 'error': 'data not saved'}), content_type='application/json')


@csrf_exempt
def admin_registration(request):
    try:
        print(request.body)
        user_data = UserDetail()
        user_data.name = request.POST.get('name')
        user_data.email = request.POST.get('email')
        user_data.user_type = request.POST.get('user_type')
        user_data.password = request.POST.get('password')
        user_data.save()
        return HttpResponse(json.dumps({'status': True, 'message': 'admin registered successfully'}),
                            content_type='application/json')
    except Exception as err:
        traceback.print_tb(err.__traceback__)
        return HttpResponse(
            json.dumps({'status': False, 'error': 'data not saved'}), content_type='application/json')


@csrf_exempt
def code_detail(request):
    try:
        code = CodeDetail.generate_uniq_code()
        while len(CodeDetail.objects.filter(code=code)) != 0:
            code = CodeDetail.generate_uniq_code()
        code_detail = CodeDetail()
        code_detail.x = request.POST.get('x')
        code_detail.code = code
        code_detail.save()
        return HttpResponse(json.dumps({'status': True, 'message': 'data saved successfully'}),
                            content_type='application/json')
    except Exception as err:
        traceback.print_tb(err.__traceback__)
        return HttpResponse(
            json.dumps({'status': False, 'error': 'data not saved'}), content_type='application/json')


def code_used_count(request):
    try:
        print(request.GET.urlencode())
        code = request.GET.get('code')
        print(code)
        if CodeDetail.objects.get(code=code):
            code_detail = CodeDetail.objects.get(code=code)
            code_detail.count = code_detail.count + 1
            code_detail.save()
            return HttpResponse(json.dumps({'status': True, 'message': 'data saved successfully'}),
                                content_type='application/json')
        else:
            return HttpResponse(
                json.dumps({'status': False, 'error': 'data not saved'}), content_type='application/json')

    except ObjectDoesNotExist:
        return HttpResponse(
            json.dumps({'status': False, 'error': 'This app does not exist in our database'}), content_type='application/json')
