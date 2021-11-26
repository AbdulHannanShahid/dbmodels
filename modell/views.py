from django.contrib.auth.backends import AllowAllUsersModelBackend
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Posts, Bio, Comment, Likes
from django.http import HttpResponseRedirect
from modell.templatetag import extras
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import TaskSerializer
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django import forms
import time
import asyncio
# Create your views here.


def index(request):
    if request.method == "POST":
        prod = User()

        prod.user_name = request.POST.get('fname', '')
        bio_email = request.POST.get('email', '')
        bio_password = request.POST.get('password', '')
        prod.save()
        bio = Bio(bio_email=bio_email, bio_password=bio_password, user=prod)
        bio.save()
    return render(request, 'index.html')


def registerPage(request):
    print("abc")
    context = {}
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('/postspage')
        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('postpage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('postpage')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    users = request.user
    print("test++", users)
    logout(request)
    return redirect('home')
# @login_required(login_url='login')


def postspage(request):
    users = request.user
    print("test++", users)
    myposts = Posts.objects.all()
    return render(request, 'postspage.html', {'myposts': myposts})
# @login_required(login_url='login')


def post(request, id):

    myid = id
    post = Posts.objects.filter(posts_id=myid)[0]
    print("post", post)
    if request.method == "POST":
        parentid = request.POST.get('parentSno')
        print(parentid)
        if request.POST.get("btn1"):
            myposts = Posts(posts_id=id)
            pos = User(user_id=1)
            pod = Likes(user=pos, posts=myposts)
            pod.save()

        # comment_reply(myid)
        parentid = request.POST.get('parentSno', '')
        myposts = Posts(posts_id=id)
        pos = User(user_id=1)
        print(parentid)
        if parentid != "":
            prod = Comment()
            prod.comment_content = request.POST.get('reply', '')
            parent1 = Comment.objects.get(comment_id=parentid)
            com = Comment(comment_content=prod.comment_content,
                          user=pos, posts=myposts, parent=parent1)
            com.save()
            print(parent1)
        else:
            prod = Comment()
            prod.comment_content = request.POST.get('comment', '')
            com = Comment(comment_content=prod.comment_content,
                          user=pos, posts=myposts)
            com.save()
        if request.POST.get("btn2"):
            Comment.objects.all().delete()
    abc = Comment()
    # return HttpResponseRedirect(request.path_info)
    pst = Comment.objects.filter(posts=post, parent=None)
    replies = Comment.objects.filter(posts=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.comment_id not in replyDict.keys():
            replyDict[reply.parent.comment_id] = [reply]
        else:
            replyDict[reply.parent.comment_id].append(reply)
    return render(request, 'post.html',
                  {'post': post, 'pst': pst, 'replyDict': replyDict})  # 'reply':reply
# def comment_reply(request, id,myid):
#    print(id)
 #   print(myid)
  #  comment = Comment.objects.filter(comment_id=myid)[0]
   # myposts= Posts(posts_id=id)
    #pos = User(user_id= 1)
    #prod= Comment(comment_id=myid)

   # reply=Reply()
   # if request.method == "POST":
    #    reply.reply_content= request.POST.get('reply','')
    #   rep=Reply(reply_content=reply.reply_content,user=pos,posts=myposts,comment=prod)
    #  rep.save()
    # if request.POST.get("btn4"):
    #    Reply.objects.all().delete()

    # return render(request, 'reply.html',{'comment':comment,'reply':reply})


@api_view(['GET'])
def api_check(request):
    apiurls = {
        'this/': 'home',
        'api-auth/': 'rest_framework.urls',
        'postspage/': 'postpage',
        'postspage/<int:id>/': 'posts'
    }
    return Response(apiurls)


@api_view(['GET'])
def api_users(request):
    user1 = Bio.objects.all()
    serializer = TaskSerializer(user1, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_userdetails(request, pk):
    user1 = Bio.objects.get(id=pk)
    serializer = TaskSerializer(user1, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def api_createuser(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def api_updateuser(request, id):
    user1 = Bio.objects.get(id=id)
    serializer = TaskSerializer(instance=user1, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def api_deleteuser(request, id):
    user1 = Bio.objects.get(id=id)
    user1.delete()
    return Response("this item is successfully deleted")
