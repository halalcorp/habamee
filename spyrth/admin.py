from __future__ import unicode_literals
from django.contrib import admin
from authtools.admin import NamedUserAdmin
from .models import *
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse


admin.site.register(programs)