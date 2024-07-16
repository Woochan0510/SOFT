from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
class Register(APIView):
    def get(self, request):
        return render(request, "user/register.html")
    
    def post(self, request):
        #TODO: 회원가입
        email = request.data.get('email', None)
        nickname = request.data.get('nickname', None)
        name = request.data.get('name', None)
        password = request.data.get('password', None)

        User.objects.create(email=email, nickname=nickname, name=name, password=make_password(password),profile_image="default_image.jpg")
    
        return Response(status=200)

class Login(APIView):
    def get(self, request):
        return render(request, "user/login.html")
    
    def post(self, request):
        #TODO: 로그인
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(status=404, data=dict(message="회원정보가 잘못되었습니다."))
        
        if user.check_password(password):
            #로그인함.
            request.session['email'] = email
            return Response(status=200)
        else:
            return Response(status=400, data=dict(message="회원정보가 잘못되었습니다."))