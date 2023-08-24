from django.urls import path

from . import views

# app_name = 'mfp'
# urlpatterns = [
#     # path("", views.index, name="index"),
# ]


# from django.conf.urls import url
from django.urls import path

from . import views

app_name="mfp"
urlpatterns = [
    # path("", views.TopView.as_view(), name="top"),
    # path("home/", views.HomeView.as_view(), name="home"),
    path("", views.IndexView.as_view(), name="index"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignupView.as_view(), name="signup"),
]


# from django.contrib.auth.views import LoginView, LogoutView
# from django.urls import path
# from .views import index
# urlpatterns = [
#     path('login/',
#         LoginView.as_view(
#             redirect_authenticated_user=True,
#             template_name='registration/login.html'
#             ),
#         name='login'),
#     path('', index, name='index'),    # トップページ追加
#     path('logout/',
#         LogoutView.as_view(template_name='registration/logged_out.html'),
#         name='logout'),
# ]