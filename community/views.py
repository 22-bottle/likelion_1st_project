from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, CommentForm
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request, 'index.html')

def study(request):
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'study.html', {'posts':posts})

def project(request):
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'project.html', {'posts':posts})

def exhibition(request):
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'exhibition.html', {'posts':posts})

def create(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            unfinished.save()
        if unfinished.category == 'TP':
            return redirect('study')
        elif unfinished.category == 'EX':
            return redirect('exhibition')
        elif unfinished.category == 'AC':
            return redirect('project')
    else:
        form = PostForm()
    return render(request, 'create.html', {'form':form})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()

    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form})

def create_comment(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.author = request.user
        finished_form.save()
    return redirect('detail', post_id)

def modify(request, post_id):
    post = Post.objects.get(id=post_id)
    print(post.id)

    user_id = request.user.username
    if post.author.username != user_id:
        return redirect('login')
    
    else:
        if request.method == 'POST' or request.method == 'FILES':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post.category = form.cleaned_data['category']
                post.title = form.cleaned_data['title']
                post.body = form.cleaned_data['body']
                post.photo = form.cleaned_data['photo']
                post.date = timezone.datetime.now()
                post.save()
                return redirect('detail', post_id)
        else:
            form = PostForm(instance=post)
            return render(request, 'detail_modify.html', {'form':form})


def delete(request, post_id):
    user_id = request.user.username
    form = get_object_or_404(Post, pk=post_id)

    if form.author.username != user_id:
        return redirect('login')

    form.delete()
    return redirect('/')