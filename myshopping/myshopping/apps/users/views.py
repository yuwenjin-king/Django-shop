from django.shortcuts import render

# Create your views here.
from django.views import View
class Register_View(View):
    '''用户注册'''
    pass
    def get(self,request):
        '''提供用户注册页面'''
        return render(request, 'register.html')

