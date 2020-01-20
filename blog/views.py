from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from blog.models import Article


# 主页
def index(request):
    articles = Article.objects.all()
    return render(request, "blog/index.html", {"articles": articles})


# 文章页
def article_page(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, "blog/article.html", {"article": article})


# 文章编辑页
def page_edit(request, article_id):
    if str(article_id) == "0":
        return render(request, "blog/edit.html")

    article = Article.objects.get(pk=article_id)
    return render(request, "blog/edit.html", {"article": article})


# 文章发表方法
def action_edit(request):
    title = request.POST.get("title", "title")
    content = request.POST.get("content", "content")
    article_id = request.POST.get("article_id", "0")
    # 发表新文章
    if article_id == "0":
        Article.objects.create(title=title, content=content)
        articles = Article.objects.all()
        return render(request, "blog/index.html", {"articles": articles})
    # 修改文章并返回文章页
    article = Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    # return render(request, 'blog/article.html', {'article': article})
    return HttpResponseRedirect(reverse("blog:article", args=(article.id,)))

