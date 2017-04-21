# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import Login



class SecretManager(models.Manager):

    #TODO: Remove this find_secret def
    #def find_secret(self, data):
    #    secret = Secret.objects.filter(
    #        #email__exact=data['email']
    #    )
    #    return Secret

    def create_secret(self, data):
        print "Inside create_secret (in models)"
        #secret = Secret.objects.create(secret=data['secret'],login=data['login_id'])
        try:
            login = Login.objects.get(id=data['login_id'])
            secret = Secret.objects.create(secret=data['secret'],login=login)
            print 'all is well'
        except:
            print 'error happened'

        return Secret

    def delete_secret(self, id):
        print "Inside delete_secret (in models)"
        print id
        try:
            query = Secret.objects.get(id=id)
            query.delete()
            print 'all is well'
        except Exception as e:
            print '%s (%s)' % (e.message, type(e))
            print 'error happened'
        return

    def add_like(self, secret_id, user_id):
        print "Inside add_like (models)"
        print secret_id
        print user_id
        try:
            login = Login.objects.get(id=user_id)
            secret = Secret.objects.get(id=secret_id)
            like = Like(login=login,secret=secret)
            like.save()

            # Now update the likes_count in Secret table
            secret = Secret.objects.get(id=secret_id)
            secret.likes_count += 1
            secret.save()

            print 'all is well'
        except Exception as e:
            print '%s (%s)' % (e.message, type(e))
            print 'error happened'
        return


class LikeManager(models.Manager):
    def create_like(self,data):
        print "Inside create_like (in models)"
        return Like

# Create your models here.
class Secret(models.Model):
    secret = models.CharField(max_length=255)
    login = models.ForeignKey(Login,on_delete=models.CASCADE)
    likes_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SecretManager()

class Like(models.Model):
    login = models.ForeignKey(Login,on_delete=models.CASCADE)
    secret = models.ForeignKey(Secret, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LikeManager()
