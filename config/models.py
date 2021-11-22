from django.db import models


# 语言
class Language(models.Model):
    id = models.AutoField(primary_key=True)                                             # 数据库 自增ID
    create_time = models.DateTimeField(auto_now_add=True)                               # 数据库 添加时间
    update_time = models.DateTimeField(auto_now=True)                                   # 数据库 更新时间
    name = models.CharField(max_length=128, unique=True)                                # 语言名称 （使用语言对应，zh-ch）
    alias = models.CharField(max_length=128)                                            # 语言别名 （使用语言对应，中文-粤语）


# 地区
class Location(models.Model):
    id = models.AutoField(primary_key=True)                                             # 数据库 自增ID
    create_time = models.DateTimeField(auto_now_add=True)                               # 数据库 添加时间
    update_time = models.DateTimeField(auto_now=True)                                   # 数据库 更新时间
    name = models.CharField(max_length=128, unique=True)                                # 地区名称 （使用电话区号对应，86）
    alias = models.CharField(max_length=128)                                            # 地区名称 （使用邮政编码对应，中国内地）


# 艺术家性别
# 0 - 未设置，1 - 男， 2 - 女， 3 - 无性别，4 - 双性别，5 - 男转女， 6 - 女转男， 7 - 不适用
class Gender(models.Model):
    id = models.AutoField(primary_key=True)                                                     # 数据库 自增ID
    create_time = models.DateTimeField(auto_now_add=True)                                       # 数据库 添加时间
    update_time = models.DateTimeField(auto_now=True)                                           # 数据库 更新时间
    gender = models.IntegerField(unique=True)                                                   # 艺术家性别 标志位
    alias = models.CharField(max_length=64)                                                     # 艺术家性别 标志对应的别名，仅用于后台配置时展示


# 艺术家类型
# 0 - 未设置，1 - 个人， 2 - 组合
class ArtistType(models.Model):
    id = models.AutoField(primary_key=True)                                                     # 数据库 自增ID
    create_time = models.DateTimeField(auto_now_add=True)                                       # 数据库 添加时间
    update_time = models.DateTimeField(auto_now=True)                                           # 数据库 更新时间
    type = models.IntegerField(unique=True)                                                     # 艺术家类型 标志位
    alias = models.CharField(max_length=64)                                                     # 艺术家类型 标志对应的别名，仅用于后台配置时展示


# 艺术家状态
# 0 - 未设置，1 - 活跃，2 - 暂停活动， 3 - 解散，4 - 停止活动（自然人死亡）
class ArtistStatus(models.Model):
    id = models.AutoField(primary_key=True)                                                     # 数据库 自增ID
    create_time = models.DateTimeField(auto_now_add=True)                                       # 数据库 添加时间
    update_time = models.DateTimeField(auto_now=True)                                           # 数据库 更新时间
    status = models.IntegerField(unique=True)                                                   # 艺术家状态 标志位
    alias = models.CharField(max_length=64)                                                     # 艺术家状态 标志对应的别名，仅用于后台配置时展示


# 艺术家血型
# 0 - 未设置，1 - A型，2 - B型，3 - AB型，4 - O型，5 - 其他
class BloodType(models.Model):
    id = models.AutoField(primary_key=True)                                                     # 数据库 自增ID
    create_time = models.DateTimeField(auto_now_add=True)                                       # 数据库 添加时间
    update_time = models.DateTimeField(auto_now=True)                                           # 数据库 更新时间
    blood_type = models.IntegerField(unique=True)                                               # 艺术家血型 标志位
    alias = models.CharField(max_length=64)                                                     # 艺术家血型 标志对应的别名，仅用于后台配置时展示


# 音乐流派
class MusicStyle(models.Model):
    id = models.AutoField(primary_key=True)                                             # 数据库 自增ID
    create_time = models.DateTimeField(auto_now_add=True)                               # 数据库 添加时间
    update_time = models.DateTimeField(auto_now=True)                                   # 数据库 更新时间
    name = models.CharField(max_length=128, unique=True)                                # 音乐流派 名称（具体展示文本让应用本地做映射）


# 歌词文件格式
# 0 - 纯文本
class LyricFormat(models.Model):
    id = models.AutoField(primary_key=True)                                                     # 数据库 自增ID
    create_time = models.DateTimeField(auto_now_add=True)                                       # 数据库 添加时间
    update_time = models.DateTimeField(auto_now=True)                                           # 数据库 更新时间
    format = models.IntegerField(unique=True)                                                   # 歌词文件格式 标志位
    alias = models.CharField(max_length=64)                                                     # 歌词文件格式 标志对应的别名，仅用于后台配置时展示


