from django.db import models
from django.contrib.auth.models import User


# 用户账号
class AccountInfo(models.Model):
    id = models.AutoField(primary_key=True)                                                 # 数据库 自增ID
    avatar = models.TextField()                                                             # 账号 头像
    nickname = models.TextField()                                                           # 账号 头像
    birthday = models.DateField()                                                           # 账号 日期
    gender = models.OneToOneField('config.Gender', on_delete=models.PROTECT)                # 账号 性别
    description = models.TextField()                                                        # 账号 个人简介
    user = models.OneToOneField('auth.User', on_delete=models.PROTECT)                      # 账号 Django账号对应
