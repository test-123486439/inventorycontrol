
# Create your models here.
from django.db import models
class InventoryPost(models.Model):
# Create your models here.
    CATEGORY=(('食料品','食料品'),
              ('日用品','日用品'),
              ('生活用品','生活用品'))
    title=models.CharField(
        verbose_name='商品名',
        max_length=200
        
    )
    content =models.TextField(
        verbose_name='商品説明'
    )
    posted_at=models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )
    category=models.CharField(
        verbose_name='カテゴリ',
        max_length=50,
        choices=CATEGORY
    )
    quantity = models.PositiveIntegerField(  
        verbose_name='在庫数',
        default=0
    )



    def __str__(self):
        return self.title