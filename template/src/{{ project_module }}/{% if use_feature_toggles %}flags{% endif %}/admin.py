# Waffle's own admin registration targets its default models, which are
# swapped out (Django silently ignores registering swapped models); the
# custom models are registered here instead, reusing waffle's ModelAdmin
# classes.
from django.contrib import admin
from waffle.admin import FlagAdmin, SampleAdmin, SwitchAdmin

from .models import Flag, Sample, Switch

admin.site.register(Flag, FlagAdmin)
admin.site.register(Sample, SampleAdmin)
admin.site.register(Switch, SwitchAdmin)
