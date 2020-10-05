from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.core import serializers
from blogs.models import User
from blogs.models import Comment
from blogs.models import Post
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
# from rest_framework.parsers import JSONParser 


import datetime

#################################################################################################
############################################# test ##############################################
#################################################################################################
# Create your views here.
def hello(request):
    tags=['post1', 'post2', 'post3', 'post4']
    rating=4
    return render(request, 'index.html', 
    {
        'postTopic':'POST',
        'postByUser':'Pattarakorn',
        'tags':tags,
        'rating':rating
    })


@csrf_exempt
def addPost(request):
   
    if request.method == 'POST':
        user_name = request.POST['name']
        user_email = request.POST['email']
        a = User(name=user_name,email=user_email)
        a.save()
        b = Post(topic="mytoppic",date=datetime.date.today,user_id=a)
        b.save()
        c = Comment(comment="5555566665",date="66666",post_id=b,user_id=a)
        c.save()
        return JsonResponse({"status":"Ok"})
    elif request.method == 'GET':
        # post.save()
        # a = Post.objects.all()
        post_id = request.GET['id']
        # if post_id!="all":
            # a = get_object_or_404(Post, id = post_id)
            # response = {
            #     'id': a.id,
            #     'topic' : a.topic,
            #     'user_id':{
            #         'name' : a.user_id.name,
            #         'email' : a.user_id.email
            #     }
            # }
        # else:
        a = get_object_or_404(Post,id = post_id)
        a.objects.application
        # for data in a:
        #     response.append({
        #         'id': data.id,
        #         'topic' : data.topic,
        #         'user_id':{
        #             'name' : data.user_id.name,
        #             'email' : data.user_id.email
        #         }
        #     })
        response = {
                'id': a.id,
                'topic' : a.topic,
                'user_id':{
                    'name' : a.user_id.name,
                    'email' : a.user_id.email
                }
            }
        return JsonResponse(response)
        # return HttpResponse(json.dumps(response), content_type="text/json-comment-filtered")
    elif request.method == 'DELETE':
        # post.save()
        posts = Post.objects.filter(header="5555566665").delete()
        # Post.objects.get(header="555555").delete()
        # post_list = serializers.serialize('json', posts)
        # Post.save()
        return JsonResponse({"aaa":"sssss"})


# @csrf_exempt
# class FindPost(View):
#     def get(self, request, id):
#         test = get_object_or_404(Post, id=id)
#         response = {
#             'id' : test.id,
#             'topic': test.topic,
#             'user_id': test.user_id.id,
#         }
#         return HttpResponse(json.dumps(response), content_type='application/json')


# class CreatePost(View):
#     def post(self, request):
#         test = User(request.POST)
#         print(test)
#         print(request.data)
#         return test

        
# @csrf_exempt
# def adduser(request):
#     name = request.POST['name']
#     email = request.POST['email']
#     a = User(name=name,email=email)
#     a.save()
#     return JsonResponse({"aaa":"sssss"})
    

# class sendPost(serializers.ModelSerializer):
#     def get(self, request, name):
#         a = User(name=name,email="soku@kosu.com")
#         a.save()
#         return JsonResponse({"status":"Ok"})

#         class Meta:


#################################################################################################
############################################# user ##############################################
#################################################################################################
        
def apiuserget(request):
    user_id = request.GET['id']
    if user_id != 'all':
        a = get_object_or_404(User, id = user_id)
        response = {
            'name' : a.name,
            'email' : a.email
        }
        return HttpResponse(json.dumps(response), content_type="text/json-comment-filtered")
    else:
        # a = User.objects.all()
        response = list()
        for a in User.objects.all():
            response.append({
                'name' : a.name,
                'email' : a.email
            })
        return HttpResponse(json.dumps(response), content_type="text/json-comment-filtered")

@csrf_exempt
def apiuserpost(request):
    a = User(name="soku",email="soku@kosu.com")
    a.save()
    return JsonResponse({"status":"Ok"})
        
def apiuserupdate(request):
    # post.save()
    # posts = User.objects.filter(header="5555566665").update(rowupdate)
    return JsonResponse({"aaa":"sssss"})
        
@csrf_exempt
def apiuserdelete(request):
    user_id = request.DELETE['id']
    User.objects.filter(id=user_id).delete()
    # User.objects.get(id="555555").delete()
    return JsonResponse({"status":"Ok"})



#################################################################################################
############################################# post ##############################################
#################################################################################################
        
def apipostget(request):
    post_id = request.GET['id']
    a = get_object_or_404(Post, id = post_id)
    # b = get_object_or_404(Comment, post_id = a.id)
    # comment_len = b.object.count()
    response = {
        'id': a.id,
        'topic' : a.topic,
        # 'number_comment' : comment_len,
        'date' : a.date.isoformat(),
        'user_id':{
            'name' : a.user_id.name,
            'email' : a.user_id.email
        }
    }
    return HttpResponse(json.dumps(response), content_type="text/json-comment-filtered")

@csrf_exempt
def apipostpost(request):
    post_user = request.POST['username']
    post_topic = request.POST['topic']
    a = get_object_or_404(User, name = post_user)
    b = Post(topic="mytoppic",date=datetime.date.today,user_id=a)
    b.save()
    return JsonResponse({"status":"Ok"})
        
def apipostupdate(request):
    # post.save()
    # posts = Post.objects.filter(header="5555566665").delete()
    # Post.objects.get(header="555555").delete()
    # post_list = serializers.serialize('json', posts)
    # Post.save()
    return JsonResponse({"aaa":"sssss"})
        
@csrf_exempt
def apipostdelete(request):
    post_id = request.DELETE['id']
    a=Post.objects.get(id=post_id)
    # Post.objects.get(id="555555").delete()
    return JsonResponse({"status":"Ok"})

        
#################################################################################################
############################################ comment ############################################
#################################################################################################
        
def apicommentget(request):
    comment_id = request.GET['id']
    a = get_object_or_404(Comment, id = comment_id)
    response = {
        'id': a.id,
        'comment' : a.comment,
        'date' : a.date.isoformat(),
        'post_id' : {
            'id': a.post_id.id,
            'topic' : a.post_id.topic,
            'date' : a.post_id.date.isoformat(),
            'user_id':{
                'name' : a.post_id.user_id.name,
                'email' : a.post_id.user_id.email,
            }
        },
        'user_id':{
            'name' : a.user_id.name,
            'email' : a.user_id.email
        }
    }
    return HttpResponse(json.dumps(response), content_type="text/json-comment-filtered")

@csrf_exempt
def apicommentpost(request):
    post_id = request.POST['id']
    a = get_object_or_404(Post, id = post_id)
    b = get_object_or_404(User, id = a.user_id.id)
    c = Comment(comment="5555566665",date="66666",post_id=a,user_id=b)
    c.save()
    return JsonResponse({"status":"Ok"})
        
def apicommentupdate(request):
    # Comment.save()
    # coment = Comment.objects.filter(header="5555566665").delete()
    return JsonResponse({"aaa":"sssss"})
        
def apicommentdelete(request):
    # Comment.save()
    # comment = Post.objects.filter(header="5555566665").delete()
    # Comment.objects.get(header="555555").delete()
    # post_list = serializers.serialize('json', comment)
    # Comment.save()
    return JsonResponse({"aaa":"sssss"})