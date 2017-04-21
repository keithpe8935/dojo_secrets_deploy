# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from models import Secret,Like
#TODO: Add code to secret displays to indicate time since the secret was posted.
import datetime;

# Create your views here.
def index(request):
    print "Inside index view"

    context = {
        'secrets': Secret.objects.order_by('-created_at'),
        #'likes': Like.objects.order_by('-created_at')
        'likes': Like.objects.order_by('-secret__created_at')
    }

    return render(request,'dojo_secrets_app/index.html',context)

def popular(request):
    print "Inside popular view"
    context = {
        'popular_secrets': Secret.objects.order_by('-likes_count')
    }

    return render(request,'dojo_secrets_app/popular.html',context)

def create_secret(request):
    print "Inside create_secret view"
    if request.session['id']:
        print request.POST
        print request.session['id']
        result = Secret.objects.create_secret(request.POST)
        return redirect('dojo_secrets_app:index')
    else:
        print "User is not logged in. Can't post a secret unless user is logged in."
        return redirect('dojo_secrets_app:index')

def delete_secret(request,id):
    print "Inside delete_secret (in views)"
    if request.method=="POST":
        print request.POST
        print request.session['id']
        print id
        result = Secret.objects.delete_secret(id)

    else:
        print "User is not logged in. Can't delete a secret unless user is logged"
        print "TODO: If the user is not logged in we shouldn't even get here."

    if request.POST['delete_from']=='recent':
        return redirect('dojo_secrets_app:index')
    elif request.POST['delete_from']=='popular':
        return redirect('dojo_secrets_app:popular')

# TODO: Currently users can like a secret (it was useful for testing). Change so once a specific user has
# 'liked' a secret he can't like it again (remove like link or better yet, just disable it)

def like_secret(request, id):
    print "Inside like_secret view"
    print id
    result = Secret.objects.add_like(id, request.session['id'])
    if request.POST['like_from']=='recent':
        return redirect('dojo_secrets_app:index')
    elif request.POST['like_from']=='popular':
        return redirect('dojo_secrets_app:popular')
