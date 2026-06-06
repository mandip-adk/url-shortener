from django.urls import path
from .views import register_view, CustomLoginView, CustomLogOutView

urlpatterns = [
    path("register/", register_view, name= "register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogOutView.as_view(), name="logout"),

]