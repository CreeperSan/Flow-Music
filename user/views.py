import json
import common.network.response as network_response
from django.http import JsonResponse


def user_login(request):
    request_body = request.body
    print(request_body)
    # request_body_json = json.loads(request_body)
    # username = request_body_json.get('username', '')
    # password = request_body_json.get('password', '')
    return JsonResponse({
        'code': 200,
        'msg': '登录成功',
        # 'username' : username,
        # 'password' : password,
    })


def user_register(request):
    try:
        request_json = json.loads(request.body)
        username = request_json.get('username', '')
        password = request_json.get('password', '')
        email = request_json.get('email', '')
    except:
        return network_response.params_error()
    # 检查参数
    if len(username) <= 0 or len(password) <= 0 or len(email) <= 0:
        return network_response.params_error()

    return JsonResponse({
        'code': 'register'
    })


def user_auth(request):
    return JsonResponse({
        'code': 200,
    })
