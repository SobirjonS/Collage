from rest_framework import serializers
from .models import (
    Slider,
    About,
    OurHistory,
    Result,
    AboutCard,
    Teacher,
    Blog,
    BlogCategory,
    Tag,
    Course,
    Contact
    )

class SliderSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Slider
        fields = ['id', 'title', 'image_url', 'description']

    def get_title(self, obj):
        return {
            'uz': obj.title_uz,
            'ru': obj.title_ru,
            'en': obj.title_en
        }
        
    def get_image_url(self,obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

    def get_description(self, obj):
        return {
            'uz': obj.description_uz,
            'ru': obj.description_ru,
            'en': obj.description_en
        }
        
class AboutSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = About
        fields = ['id','title','slug','image_url','description']
         
    def get_title(self, obj):
        return {
            'uz': obj.title_uz,
            'ru': obj.title_ru,
            'en': obj.title_en
        }
        
    def get_image_url(self,obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

    def get_description(self, obj):
        return {
            'uz': obj.description_uz,
            'ru': obj.description_ru,
            'en': obj.description_en
        }


class OurHistorySerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = OurHistory
        fields = ['id','history_year','description','image_url']
    
    def get_description(self, obj):
        return {
            'uz': obj.description_uz,
            'ru': obj.description_ru,
            'en': obj.description_en
        }
        
    def get_image_url(self,obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
    
    
class ResultSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    icon_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Result
        fields = ['id','name','amount','icon_url']
        
    def get_name(self,obj):
        return {
            'uz':obj.name_uz,
            'ru':obj.name_ru,
            'en':obj.name_en
        }
    
    def get_icon_url(self,obj):
        request = self.context.get('request')
        if obj.icon:
            return request.build_absolute_uri(obj.icon.url)
        return None
    
    
class AboutCardSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    icon_url = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    
    class Meta:
        model = AboutCard
        fields = ['id','name','description','icon_url']
    
    def get_name(self,obj):
        return {
            'uz':obj.name_uz,
            'ru':obj.name_ru,
            'en':obj.name_en
        }
    def get_description(self,obj):
        return {
            'uz':obj.name_uz,
            'ru':obj.name_ru,
            'en':obj.name_en
        }
    def get_icon_url(self,obj):
        request = self.context.get('request')
        if obj.icon:
            return request.build_absolute_uri(obj.icon.url)
        return None
    
class TeacherSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    direction = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()
    
    class Meta:
        model = Teacher
        fields = ['id','name','image_url','direction','link']
    
    def get_name(self,obj):
        return {
            'uz':obj.name_uz,
            'ru':obj.name_ru,
            'en':obj.name_en
        }
    
    def get_image_url(self,obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
    
    def get_direction(self,obj):
        return {
            'uz':obj.direction_uz,
            'ru':obj.direction_ru,
            'en':obj.direction_en
        }
    
    def get_link(self,obj):
        return {
            'facebook' : obj.facebook_link,
            'twitter' : obj.twitter_link,
            'linkedin' : obj.linkedin_link,
            'skype' : obj.skype_link
            
        }
class HomePageSerializer(serializers.Serializer):
    sliders = SliderSerializer(many=True)
    about = AboutSerializer(many=True)
    our_history = OurHistorySerializer(many=True)
    results = ResultSerializer(many=True)
    
    
class AboutPageSerializer(serializers.Serializer):
    about = AboutSerializer(many=True)
    card = AboutCardSerializer(many=True)
    
    
class TeacherPageSerializer(serializers.Serializer):
    teacher = TeacherSerializer(many=True)
    

class BlogCategorySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    
    class Meta:
        model = BlogCategory
        fields = ['id','name']
        
    def get_name(self,obj):
        return {
            'uz':obj.name_uz,
            'ru':obj.name_ru,
            'en':obj.name_en
        }
        
        
class BlogSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog
        fields = ['id','title','category','slug','image_url','description','is_new','created_at','updated_at']
         
    def get_title(self, obj):
        return {
            'uz': obj.title_uz,
            'ru': obj.title_ru,
            'en': obj.title_en
        }
        
    def get_image_url(self,obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

    def get_description(self, obj):
        return {
            'uz': obj.description_uz,
            'ru': obj.description_ru,
            'en': obj.description_en
        }

class TagSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    
    class Meta:
        model = Tag
        fields = ['id','name']
        
    def get_name(self,obj):
        return {
            'uz':obj.name_uz,
            'ru':obj.name_ru,
            'en':obj.name_en
        }

class BlogPageSerializer(serializers.Serializer):
    blog = BlogSerializer(many=True)
    category = BlogCategorySerializer(many=True)
    tag = TagSerializer(many=True)
    

class CourseSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = ['id','name','description','image_url','created_at','updated_at']
        
    def get_name(self,obj):
        return {
            'uz':obj.name_uz,
            'ru':obj.name_ru,
            'en':obj.name_en
        }
        
    def get_image_url(self,obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
        
    def get_description(self, obj):
        return {
            'uz': obj.description_uz,
            'ru': obj.description_ru,
            'en': obj.description_en
        }
        
        
class CoursePageSerializer(serializers.Serializer):
    course = CourseSerializer(many=True)
    
    
class BlogDetailPageSerializer(serializers.Serializer):
    blog = BlogSerializer(many=False)
    category = BlogCategorySerializer(many=True)
    tags = TagSerializer(many=True)
    

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'detail']
        