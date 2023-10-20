from django import forms
from django.contrib.auth.models import User
from . models import People
from . models import Account

#フォームクラス作成
# class Contact_Form(forms.Form):
    
#     Name = forms.CharField(label="名前")
#     Tell = forms.IntegerField(label="電話番号")
#     Mail = forms.EmailField(label="メールアドレス")
#     Birthday = forms.DateField(label="生年月日")
#     Website = forms.URLField(label="webサイト")
#     FreeText = forms.CharField(widget=forms.Textarea,label="備考")

class Contact_Form(forms.ModelForm):
    
    class Meta():
        #モデルクラスを指定
        model = People
        
        #表示するモデルクラスのフィールドを定義
        fields = ('Name', 'Tell', 'Mail', 'Birthday', 'Website', 'FreeText')
        
        #表示ラベルを定義
        labels = {'Name':"名前",
                  'Tell':"電話番号",
                  'Mail':"メール",
                  'Birthday':"生年月日",
                  'Website':"Webサイト",
                  'FreeText':"備考",
        }
        
# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力:非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")
    
    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','email','password')
        # フィールド名指定
        labels = {'username':"ユーザーID", 'email':"メール"}
        
class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
        model = Account
        fields = {'last_name','first_name'}
        labels = {'last_name':"苗字",'first_name':"名前"}