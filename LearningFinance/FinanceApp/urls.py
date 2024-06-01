from django.urls import path, include
from . import views
from django.contrib import admin

app_name = "FinanceApp"
urlpatterns = [

    path("", views.index, name="index"),
    path("admin/", admin.site.urls),

]
