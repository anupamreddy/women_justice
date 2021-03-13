from . import views
from django.urls import path, include
from django.contrib.auth import	views as auth_views

app_name="account"

urlpatterns = [
    path('',views.home_page,name="home_page"),
    path('victim_login/',views.victim_login,name="victim_login"),
    #path('police_login/',views.police_login,name="police_login"),
    path('police_login/',auth_views.LoginView.as_view(),name="police_login"),
    path('police_logout/',auth_views.LogoutView.as_view(),name="police_logout"),
    path('signup/',views.signup,name="signup"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('file_case/',views.file_case,name="file_case"),
]
