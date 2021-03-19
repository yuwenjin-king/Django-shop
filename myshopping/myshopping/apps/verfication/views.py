import re

from django.shortcuts import render

# Create your views here.
from django.views import View

class regiscode(View):

    def get(self,request,uuid):
        #校验参数
        #相遇请求
        #保存验证码
        #
        pass
    def post(self,request):
        pass

    def authenticate(self, request, username=None,password=None,**kwargs):
        #使用账号查询用户
        if re.match(r'^1[3-9]\d(9)$',username):
            user = User.objects.get(mobile=username)
        else:
            user = User

