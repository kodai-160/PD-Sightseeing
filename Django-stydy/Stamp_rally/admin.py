from django.contrib import admin

#モデルをインポート
from . models import People
from . models import Account

#管理ツールに登録
admin.site.register(People)
admin.site.register(Account)