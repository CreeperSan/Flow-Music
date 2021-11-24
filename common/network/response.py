from django.http import JsonResponse


CODE_SUCCESS = 200
CODE_NOT_FOUND = 404
CODE_REQUEST_ERROR = 400
CODE_SERVER_ERROR = 500


__KEY_CODE = 'code'
__KEY_MESSAGE = 'msg'
__KEY_DATA = 'data'


def success():
    return JsonResponse({
        __KEY_CODE: CODE_SUCCESS,
        __KEY_MESSAGE: 'Success',
    })


def success_data(data):
    return JsonResponse({
        __KEY_CODE: CODE_SUCCESS,
        __KEY_MESSAGE: 'Success',
        __KEY_DATA: data,
    })


def params_error():
    return JsonResponse({
        __KEY_CODE: CODE_REQUEST_ERROR,
        __KEY_MESSAGE: 'Params error',
    })


def params_error_data(data):
    return JsonResponse({
        __KEY_CODE: CODE_REQUEST_ERROR,
        __KEY_MESSAGE: 'Params error',
        __KEY_DATA: data,
    })


def server_error():
    return JsonResponse({
        __KEY_CODE: CODE_SERVER_ERROR,
        __KEY_MESSAGE: 'Server internal error',
    })


def server_error_data(data):
    return JsonResponse({
        __KEY_CODE: CODE_SERVER_ERROR,
        __KEY_MESSAGE: 'Server internal error',
        __KEY_DATA: data,
    })


def not_found():
    return JsonResponse({
        __KEY_CODE: CODE_NOT_FOUND,
        __KEY_MESSAGE: 'Not found'
    })
