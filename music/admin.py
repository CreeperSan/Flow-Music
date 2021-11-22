from django.contrib import admin
import music.models as music_model

# music
admin.site.register(music_model.ManagementCompany)
admin.site.register(music_model.Artist)
admin.site.register(music_model.Music)
admin.site.register(music_model.Album)
admin.site.register(music_model.Lyric)