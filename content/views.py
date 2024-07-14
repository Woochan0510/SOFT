from uuid import uuid4

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed
import os
from clone_coding.settings import MEDIA_ROOT

# Create your views here.

class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id') # select * from content_feed

        return render(request, "silvergram/main.html", context=dict(feeds=feed_list))
    
class UploadFeed(APIView):
    def post(self, request):
        
        #일단 파일 불러오기
        file = request.FILES['file']
        uuid_name = uuid4().hex #랜덤하게 이름을 만들어줌
        save_path = os.path.join(MEDIA_ROOT, uuid_name) #위에서 생성한 랜덤한 이름으로 루트 지정
        
        with open(save_path, 'wb+') as destination: #실제 파일을 저장하는 부분
            for chunk in file.chunks():
                destination.write(chunk)

        file = request.data.get('file')
        image = uuid_name
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')

        Feed.objects.create(image=image, content=content, user_id=user_id, profile_image=profile_image,like_count=0)

        return Response(status=200)