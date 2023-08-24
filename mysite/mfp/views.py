from django.shortcuts import render

# Create your views here.
from .models import Restaurant, C_store, Restroom

# def index(request):
#     latest_restaurant_list = Restaurant.objects.order_by("-pub_date")[:5]
#     latest_c_store_list = C_store.objects.order_by("-pub_date")[:5]
#     latest_restroom_list = Restroom.objects.order_by("-pub_date")[:5]
#     context = {
#         "latest_restaurant_list": latest_restaurant_list,
#         "latest_c_store_list": latest_c_store_list,
#         "latest_restroom_list": latest_restroom_list,
#     }
   
#     return render(request, "index.html", context)


from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

from .forms import LoginForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class SignupView(CreateView):
    """ ユーザー登録用ビュー """
    form_class = UserCreationForm # 作成した登録用フォームを設定
    template_name = "registration/signup.html" 
    success_url = reverse_lazy("login.html") # ユーザー作成後のリダイレクト先ページ

   
class LoginView(LoginView):
    """ログインページ"""
    form_class = LoginForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        next_url = self.request.GET.get('next')
        if next_url:
            return redirect(next_url)
        return super().form_valid(form)


class LogoutView(LogoutView):
    """ログアウトページ"""
    template_name = "registration/logged_out.html"

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = '/login/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['latest_restaurant_list'] = Restaurant.objects.order_by("-pub_date")[:5]
        context['latest_c_store_list'] = C_store.objects.order_by("-pub_date")[:5]
        context["latest_restroom_list"] = Restroom.objects.order_by("-pub_date")[:5]
        return context
    
    

# from django.shortcuts import render
# from django.contrib.auth import get_user_model
# def top(request):
#     # ユーザーモデルを取得する
#     user = get_user_model()
#     # ユーザーをすべて取得する
#     users = user.objects.all()
#     # ユーザー一覧をコンテキスト情報に入れる
#     context = {'users': users}
#     # top.htmlをレンダリング
#     return render(request, 'mfp/index.html', context)

# def index(request):
#     return HttpResponse("Hello, world. You're at the mfp index.")