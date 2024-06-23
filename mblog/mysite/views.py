from django.shortcuts import render, redirect
#from django.http import HttpResponse
from mysite.models import Post
from datetime import datetime

# Create your views here.
# Views functions: read DB post records and show in index
'''
def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + str(post) + "<hr>")
        post_lists.append("<small>" +str(post.body) + "</small><br><br>")
    return HttpResponse(post_lists)
'''
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, "index.html", locals()) #locals() 會打包-dict記憶體中所有的區域變數

# to every article
def showpost(request, slug):
    try:
        #從數據庫中查找 Post 模型中 slug 字段等於 slug 參數的文章。
        post = Post.objects.get(slug = slug) 
        if post != None:
            return render(request, 'post.html', locals())
    #捕獲所有異常。如異常（找不到文章或數據錯誤），重定向到首頁。
    except:
        return redirect('/')
    
#