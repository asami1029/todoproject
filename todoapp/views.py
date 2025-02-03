from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import BlogPost
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404
# Create your views here.
class IndexView(ListView):
    template_name='index.html'
    context_object_name='orderby_records'
    queryset=BlogPost.objects.order_by('-posted_at')
    
class PostView(DetailView):
    template_name='post.html'
    context_object_name='orderby_records'
    queryset=BlogPost.objects.order_by('-posted_at')


class BlogDetail(DetailView):
    template_name='post.html'
    model=BlogPost
    context_object_name = 'record'

class ContactView(FormView):
    template_name='contact.html'
    form_class=ContactForm
    success_url=reverse_lazy('todoapp:contact')
    def form_valid(self,form):
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        title=form.cleaned_data['title']
        message=form.cleaned_data['message']
        subject='お問い合わせ:{}'.format(title)
        message=\
            '送信者名:{0}\nメールアドレス:{1}\nタイトル:{2}\nメッセージ:\n{3}'.format(name,email,title,message)
        from_email='fko2347064@stu.o-hara.ac.jp'
        to_list=['fko2347064@stu.o-hara.ac.jp']
        message=EmailMessage(subject=subject,body=message,from_email=from_email,to=to_list)
        message.send()
        messages.success(self.request,'お問い合わせは正常に送信されました。')
        return super().form_valid(form)
        
    