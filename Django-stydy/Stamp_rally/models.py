#モデル読込
from django.db import models
#ユーザー認証
from django.contrib.auth.models import User

#モデルクラスを定義
class People(models.Model):
    #項目定義
    Name = models.CharField(max_length=100)          #文字列
    Tell = models.IntegerField(blank=True, null=True)#整数
    Mail = models.EmailField(max_length=100)         #Email
    Birthday = models.DateField()                    #日付
    Website = models.URLField()                      #URL
    FreeText = models.TimeField()                    #フリーテキスト
    
    #テキスト表示
    def __str__(self):
        return self.Name
    
        
#ユーザーアカウントのモデルクラス
class Account(models.Model):
        
    #ユーザー認証のインスタンス
    user = models.OneToOneField(User, on_delete=models.CASCADE)
        
    #追加フィールド
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    
    #テキスト表示
    def __str__(self):
        return self.user.username