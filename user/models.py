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


# 账户登录信息
class AccountToken(models.Model):
    id = models.AutoField(primary_key=True)                                                 # 数据库 自增ID
    user = models.ManyToManyField('auth.User')                                              # 对应的账户
    platform = models.OneToOneField('config.Platform', on_delete=models.PROTECT)            # 账户信息 - 平台
    device_brand = models.CharField(max_length=128)                                         # 账户信息 - 机器品牌
    device_name = models.CharField(max_length=128)                                          # 账户信息 - 机器名称
    device_code = models.CharField(max_length=128)                                          # 账户信息 - 机器标识
    app_version = models.IntegerField()                                                     # 账户信息 - 应用版本
    create_time = models.DateTimeField()                                                    # 账户信息 - 首次使用时间
    update_time = models.DateTimeField()                                                    # 账户信息 - 更新时间
