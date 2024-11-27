from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    HomePageSerializer,
    AboutPageSerializer,
    TeacherPageSerializer,
    BlogPageSerializer,
    BlogDetailPageSerializer
)
from .models import (
    Slider,
    About,
    OurHistory,
    Result,
    Teacher,
    Blog
)

class HomePageAPIView(APIView):
    def get(self, request):
        data = {
            'sliders': Slider.objects.all(),
            'about': About.objects.all(),
            'our_history': OurHistory.objects.all(),
            'results': Result.objects.all(),
        }
        serializer = HomePageSerializer(data, context={'request': request})
        return Response(serializer.data)
    
    
class TeacherPageAPIView(APIView):
    def get(self,request):
        data = {
            'teacher': Teacher.objects.all(),
        }
        serializer = TeacherPageSerializer(data,context={'request':request})
        return Response(serializer.data)
    

class BlogPageAPIView(APIView):
    def get(self,request):
        data = Blog.objects.all()
        serializer = BlogPageSerializer(data,context={'request':request})
        return Response(serializer.data)

class BlogDetailAPIView(APIView):
    def get(self, request, slug):
        try:
            blog = Blog.objects.get(slug=slug)
        except Blog.DoesNotExist:
            return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)
        
        data = Blog.objects.all()
        serializer = BlogDetailPageSerializer(data, context={'request': request})
        return Response(serializer.data)
        