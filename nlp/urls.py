from django.urls import path
from . import views

urlpatterns = [
    path ("", views.index, name="home") #""にアクセスするとview.pyのindex関数が動く
]