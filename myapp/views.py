
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .forms import PostForm
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView,TemplateView


def home(req):
    if req.user.is_authenticated:
        # u = User.objects.get(username=req.user)
        posts = Article.objects.filter(Private = False)
        print(posts)
        return render(req,'myapp/home.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')


def dashboard(req):
    if req.user.is_authenticated:
        print(req.user)
        u= User.objects.get(username=req.user)
        posts = Article.objects.filter(user=u.id)
        print(posts)
        return render(req,'myapp/dashboard.html',{'posts':posts })
    else:
        return HttpResponseRedirect('/login/')

def add_article(req):
    if req.user.is_authenticated:
        user = req.user
        u = User.objects.get(username=req.user)
        req.session["user_id"]=u.id
        # print(req.session["user_id"])
        if req.method== "POST":
            form = PostForm(req.POST)
            # print(req.user)
            # print(req.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['article']
                private = form.cleaned_data['Private']
                pst = Article(user = req.user, title=title,article = desc, Private = private)
                pst.save()
                return HttpResponseRedirect('/myapp/dashboard/')
        else:
            form = PostForm()
        return render(req,'myapp/createpost.html',{'form':form,'user':user})
    else:
        return HttpResponseRedirect('/login/')

def edit_article(req,id):
    if req.user.is_authenticated:
        if req.method == "POST":
            pi = Article.objects.get(pk=id)
            form = PostForm(req.POST,instance=pi)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/myapp/dashboard/')
        else:
            pi = Article.objects.get(pk = id)
            form = PostForm(instance=pi)
        return render(req,'myapp/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


def delete_confirm(req,id):
    id = id
    return render(req,'myapp/delete_confirm.html',{'id':id})



def delete_article(req,id):
    if req.user.is_authenticated:
        if req.method == "POST":
            pi = Article.objects.get(pk = id)
            pi.delete()
        return HttpResponseRedirect('/myapp/dashboard/')
    else:
        return HttpResponseRedirect('/login/')


def author_list(req):
    if req.user.is_authenticated:
        print(req.user)
        u= User.objects.all()
        print(u)
        for x in u:
            print(x.first_name," ",x.last_name)
        user = req.user
        full_name = user.get_full_name()
        # print(full_name)
        gps = user.groups.all()
        return render(req,'author/author_list.html',{'name':u})
    else:
        return HttpResponseRedirect('/login/')

def title_list(req):
    if req.user.is_authenticated:
        print(req.user)
        u= Article.objects.all()
        print(u)
        l = []
        for x in u: 
            l.append(x.title)
        l = set(l)
        return render(req,'title/title_list.html',{'name':l})
    else:
        return HttpResponseRedirect('/login/')

def author_article(req,id):
    if req.user.is_authenticated:
        # u = User.objects.get(username=req.user)    
        u = User.objects.get(pk = id)
        print(u)
        posts = Article.objects.filter(user_id = id)
        # print(posts)
        return render(req,'myapp/home.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')

def article_on_topics(req,topic):
    if req.user.is_authenticated:
        # u = User.objects.get(username=req.user)    
        # u = User.objects.get(title = topic)
        # print(u)
        posts = Article.objects.filter(title = topic)
        # print(posts)
        return render(req,'myapp/home.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')

def article_detail(req,id):
    if req.user.is_authenticated:
        pi = Article.objects.get(pk=id)
        return render(req,'myapp/article_detail.html',{'pi':pi})
    else:
        return HttpResponseRedirect('/login/')
