from django.contrib import admin
import config.models as config_model

# config
admin.site.register(config_model.Language)
admin.site.register(config_model.Location)
admin.site.register(config_model.Gender)
admin.site.register(config_model.ArtistType)
admin.site.register(config_model.ArtistStatus)
admin.site.register(config_model.BloodType)
admin.site.register(config_model.MusicStyle)
admin.site.register(config_model.LyricFormat)
