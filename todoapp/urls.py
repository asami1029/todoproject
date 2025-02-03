from django.urls import path
from . import views

app_name='todoapp'


urlpatterns=[
	# ヘッダーのulr
    path('',views.IndexView.as_view(),name='index'),
    path('post/<int:pk>/', views.BlogDetail.as_view(), name='post'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path(
        'blog-detail/<int:pk>/',
        views.BlogDetail.as_view(),
        name='blog_detail'
        ),
    path(
        'blog-detail/<int:pk>/',
        views.BlogDetail.as_view(),
        name='blog_detail'),
]