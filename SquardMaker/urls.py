from django.contrib import admin
from django.urls import path
from . import views

app_name = 'SquardMaker'

urlpatterns = [
    path('admin/', admin.site.urls),

]