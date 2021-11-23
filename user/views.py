import json
from django.http import JsonResponse


def user_login(request):
    request_body = request.body
    print(request_body)
    # request_body_json = json.loads(request_body)
    # username = request_body_json.get('username', '')
    # password = request_body_json.get('password', '')
    return JsonResponse({
        'code' : 200,
        'msg' : '登录成功',
        # 'username' : username,
        # 'password' : password,
    })


def user_register(request):
    return JsonResponse({
        'code' : 'register'
    })
