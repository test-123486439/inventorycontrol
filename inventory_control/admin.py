from django.contrib import admin
from .models import InventoryPost
# Register your models here.
admin.site.register(InventoryPost)

class InventoryPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'quantity', 'posted_at')  # 一覧に表示する項目
    list_filter = ('category',)  # サイドバーでカテゴリ絞り込み
    search_fields = ('title', 'content')  # 検索ボックスで検索可能

