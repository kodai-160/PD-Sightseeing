from django.shortcuts import render
from django.views.generic import TemplateView #テンプレートタグ
from .forms import AccountForm, AddAccountForm #ユーザーアカウントフォーム

# ログイン、ログアウトに使用
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from typing import Any
from . import forms


def index(request):
    #変数設定
    params = {"message_me": "Hello World"}
    #出力
    return render(request, "Stamp_rally_html/index.html", context=params)

# お問い合わせフォーム
class FormView(TemplateView):
    
    #初期変数定義
    def __init__(self):
        self.params = {"Message":"情報を入力してください",
                       "form":forms.Contact_Form(),
                       }
        
    #GET時の処理を記載
    def get(self,request):
        return render(request, "Stamp_rally_html/formpage.html",context=self.params)
    
    #POST時の処理を記載
    def post(self,request):
        if request.method == "POST":
            self.params["form"] = forms.Contact_Form(request.POST)
            
            #フォーム入力が有効な場合
            if self.params["form"].is_valid():
                #入力項目をデータベースに保存
                self.params["form"].save(commit=True)
                self.params["Message"] = "入力情報が送信されました"
                
        return render(request, "Stamp_rally_html/formpage.html",context=self.params)
    
    
    
# ログイン
def Login(request):
    #POST
    if request.method == 'POST':
        # フォームの入力ユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')
        
        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)
        
        #ユーザー認証
        if user:
            # ユーザーアクティベイト判定
            if user.is_active:
                login(request, user)
                # ホームページ機能
                return HttpResponseRedirect(reverse('home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        #ユーザー認証失敗
        else:
            return HttpResponse('ログインIDまたはパスワードが間違っています')
        
    #GET
    else:
        return render(request, 'Stamp_rally_html/login.html')
    
#ログアウト
@login_required
def Logout(request):
    logout(request)
    #ログイン遷移画面
    return HttpResponseRedirect(reverse('Login'))


#ホーム
def home(request):
    params = {"UserID":request.user,}
    return render(request, "Stamp_rally_html/home.html", context=params)
    
    
#ユーザー登録画面
class  AccountRegistration(TemplateView):
    
    def __init__(self):
        self.params = {
            "AccountCreate":False,
            "account_form":AccountForm(),
            "add_account_form":AddAccountForm(),
        }

    # GET処理
    def get(self, request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request, "Stamp_rally_html/register.html", context=self.params)
        
    # POST処理
    def post(self, request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)
        
        # フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDBに保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()
            
            #下記情報追加
            #下記操作のため、コミットなし
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐づけ
            add_account.user = account
            
            # モデル保存
            add_account.save()
            
            # アカウント作成情報更新
            self.params["AccountCreate"] = True
            
        else:
            # フォームが有効でないとき
            print(self.params["account_form"].errors)
            
        return render(request, "Stamp_rally_html/register.html", context=self.params)