from django.urls import path
from . import views
from .views import merchstore_list, merchstore_detail

app_name = "merchstore"

urlpatterns = [
    path("", merchstore_list, name="merchstore_home"),
    path('merchstore/list', merchstore_list, name="merchstore_list"),
    path('merchstore/item/<int:param>', merchstore_detail, name="merchstore_detail"),
    ]