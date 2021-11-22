from django.db import models


# 经纪公司
class ManagementCompany(models.Model):
    id = models.AutoField(primary_key=True)                                                                             # 数据库 自增ID
    create_time = models.DateTimeField(auto_now_add=True)                                                               # 数据库 添加时间
    update_time = models.DateTimeField(auto_now=True)                                                                   # 数据库 更新时间
    name = models.CharField(max_length=256, unique=True)                                                                # 经纪公司 名称
    location = models.OneToOneField('config.Location', on_delete=models.PROTECT)                                        # 经纪公司 所在地区
    website = models.CharField(max_length=512)                                                                          # 经纪公司 官网
    logo = models.TextField()                                                                                           # 经纪公司 Logo


# 艺术家
class Artist(models.Model):
    id = models.AutoField(primary_key=True)                                                                             # 数据库 自增ID
    create_time = models.DateTimeField(auto_now_add=True)                                                               # 数据库 添加时间
    update_time = models.DateTimeField(auto_now=True)                                                                   # 数据库 更新时间
    name = models.CharField(max_length=256, unique=True)                                                                # 艺术家 名称
    description = models.JSONField()                                                                                    # 艺术家 简介，支持 markdown 、 html 与 text，[{format:'markdown', content:..}, ...]
    type = models.OneToOneField('config.ArtistType', on_delete=models.PROTECT)                                          # 艺术家 类型，
    status = models.OneToOneField('config.ArtistStatus', on_delete=models.PROTECT)                                      # 艺术家 状态，
    gender = models.OneToOneField('config.Gender', on_delete=models.PROTECT)                                            # 艺术家 艺术家性别
    birthday = models.DateField()                                                                                       # 艺术家 出生日期
    birth_place = models.OneToOneField('config.Location', on_delete=models.PROTECT, related_name='birth_place_location')# 艺术家 出生地区（简略，与出生地址任选其一，优先地址）
    birth_place_str = models.CharField(max_length=256)                                                                  # 艺术家 出生地址（详细，与出生地区任选其一，优先地址）
    release_date = models.DateField()                                                                                   # 艺术家 出道日期
    location = models.OneToOneField('config.Location', on_delete=models.PROTECT, related_name='location_location')      # 艺术家 地区
    language = models.ManyToManyField('config.Language')                                                                # 艺术家 语言
    blood_type = models.OneToOneField('config.BloodType', on_delete=models.PROTECT)                                     # 艺术家 血型
    height = models.FloatField()                                                                                        # 艺术家 身高（单位 cm）
    weight = models.FloatField()                                                                                        # 艺术家 体重（单位 kg）
    management_company = models.OneToOneField('ManagementCompany', on_delete=models.PROTECT)                            # 艺术家 所在经济公司
    members_count = models.SmallIntegerField()                                                                          # 艺术家 人数规模
    avatar = models.TextField()                                                                                         # 艺术家 头像
    images = models.JSONField()                                                                                         # 艺术家 图片[{url:string}, ...]


# 音乐
class Music(models.Model):
    id = models.AutoField(primary_key=True)                                             # 数据库 自增ID
    create_time = models.DateTimeField(auto_now_add=True)                               # 数据库 添加时间
    update_time = models.DateTimeField(auto_now=True)                                   # 数据库 更新时间
    title = models.CharField(max_length=256)                                            # 音乐 标题
    subtitle = models.CharField(max_length=256)                                         # 音乐 副标题
    artist = models.ManyToManyField('Artist')                                           # 音乐 所属艺术家
    album = models.ManyToManyField('Album', related_name='music_album')                 # 音乐 所属专辑
    release_date = models.DateField()                                                   # 音乐 发行时间
    style = models.OneToOneField('config.MusicStyle', on_delete=models.PROTECT)         # 音乐 流派
    duration = models.IntegerField()                                                    # 音乐 持续时间（单位ms）
    bitrate = models.IntegerField()                                                     # 音乐 比特率（单位 kbps）
    url = models.TextField()                                                            # 音乐 OSS地址
    size = models.IntegerField()                                                        # 音乐 文件大小
    format = models.CharField(max_length=32)                                            # 音乐 文件格式（mp3,flac,...）
    bpm = models.FloatField()                                                           # 音乐 每分钟节拍数
    images = models.JSONField()                                                         # 音乐 图片[{url:string}, ...]
    # uploader = models.OneToOneField('',  on_delete=models.PROTECT)                      # 音乐 上传人


# 专辑模型
class Album(models.Model):
    id = models.AutoField(primary_key=True)                                             # 数据库 自增ID
    create_time = models.DateTimeField(auto_now_add=True)                               # 数据库 添加时间
    update_time = models.DateTimeField(auto_now=True)                                   # 数据库 更新时间
    name = models.CharField(max_length=512)                                             # 专辑 名称
    release_date = models.DateField()                                                   # 专辑 发售日期
    artist = models.ManyToManyField('Artist')                                           # 专辑 艺术家
    image = models.TextField()                                                          # 专辑 封面
    description = models.TextField()                                                    # 专辑 描述
    music = models.ManyToManyField('Music', related_name='album_music')                 # 专辑 所包含的音乐


# 歌词模型
class Lyric(models.Model):
    id = models.AutoField(primary_key=True)                                             # 数据库 自增ID
    create_time = models.DateTimeField(auto_now_add=True)                               # 数据库 添加时间
    update_time = models.DateTimeField(auto_now=True)                                   # 数据库 更新时间
    title = models.CharField(max_length=256)                                            # 歌词 标题
    subtitle = models.CharField(max_length=256)                                         # 歌词 副标题
    artist = models.CharField(max_length=128)                                           # 歌词 歌手
    duration = models.IntegerField()                                                    # 歌词 持续时间
    url = models.TextField()                                                            # 歌词 下载地址
    format = models.OneToOneField('config.LyricFormat', on_delete=models.PROTECT)       # 歌词 文件格式
    # uploader = models.OneToOneField('',  on_delete=models.PROTECT)                      # 歌词 上传人

