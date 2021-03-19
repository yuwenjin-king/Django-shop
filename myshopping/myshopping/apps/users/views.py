from django.shortcuts import render

# Create your views here.
from django.views import View
class Register_View(View):
    '''用户注册'''
    pass
    def get(self,request):
        '''提供用户注册页面'''
        return render(request, 'register.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        mobile = request.POST.get('mobile')
        allow = request.POST.get('allow')

        sql = '''
        INSERT INTO user('username','password','password2','mobile','allow')VALUES (%s,%s,%s,%s,%s,%s)
        '''

