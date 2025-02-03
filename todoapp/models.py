from django.db import models

# Create your models here.
class BlogPost(models.Model):
    CATEGORY=(('ニュース','ニュース')),
    # image = models.ImageField(upload_to = 'photos')

    title=models.CharField(
        verbose_name='タイトル',
        max_length=200
    )
    content=models.TextField(
        verbose_name='本文'
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
    
    slug = models.SlugField(
        unique=True,  # 重複しないslug
        blank=True,  # 初期は空でもOK
        verbose_name='スラッグ'
    )

    def __str__(self):
        return self.title