# path関数をimport
from django.urls import path
#同ディレクトリからviews.pyをインポート
from . import views

#path関数(アクセスするアドレス、呼び出す関数)を追記
#path(アクセスするアドレス, 呼び出す処理, name="パス名")
urlpatterns = [
    #path('', views.index, name='index'),
    path('',views.home,name="home"),
    path('register', views.AccountRegistration.as_view(), name='register'),
    path('formpage', views.FormView.as_view(),name='formpage'),
    path('logout', views.Logout,name='Logout'),
    path('Login',views.Login,name="Login"),
]
