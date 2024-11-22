from django.contrib import admin
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import (
    Slider,
    About,
    OurHistory,
    Result,
    AboutCard,
    Teacher,
    BlogCategory,
    Blog,
    Tag,
    Course,
    Contact,
    )


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_ru', 'title_en')
    fieldsets = (
        (_('Uzbek'), {'fields': ('title_uz', 'description_uz')}),
        (_('Russian'), {'fields': ('title_ru', 'description_ru')}),
        (_('English'), {'fields': ('title_en', 'description_en')}),
        (_('Image'), {'fields': ('image',)}),
    )


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title_uz','title','title_en')
    fieldsets = (
        (_('Uzbek'), {'fields': ('title_uz', 'description_uz')}),
        (_('Russian'), {'fields': ('title_ru', 'description_ru')}),
        (_('English'), {'fields': ('title_en', 'description_en')}),
        (_('Slug'), {'fields': ('slug', )}),
        (_('Image'), {'fields': ('image',)}),
    )
    
    
@admin.register(OurHistory)
class OurhistoryAdmin(admin.ModelAdmin):
    list_display = ('history_year',)
    fieldsets = (
        (_("History year"),{'fields':('history_year',)}),
        (_('Uzbek'), {'fields': ('description_uz',)}),
        (_('Russian'), {'fields': ('description_ru',)}),
        (_('English'), {'fields': ('description_en',)}),
        (_('Image'), {'fields': ('image',)}),
    )
    
    
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('name_uz','name_ru','name_en')
    fieldsets = (
        (_('Uzbek'),{'fields':('name_uz',)}),
        (_('Russian'),{'fields':('name_ru',)}),
        (_('English'),{'fields':('name_en',)}),
        (_('Amount'), {'fields': ('amount',)}),
        (_('Icon'), {'fields': ('icon',)}),
        
    )
    
   
    
@admin.register(AboutCard)
class AboutCardAdmin(admin.ModelAdmin):
    list_display = ('name_uz','name_ru','name_en')
    fieldsets = (
        (_('Uzbek'),{'fields':('name_uz','description_uz')}),
        (_('Russian'),{'fields':('name_ru','description_ru')}),
        (_('English'),{'fields':('name_en','description_en')}),
        (_('Icon'), {'fields': ('icon',)}),
    )
    

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name_uz','name_ru','name_en')
    fieldsets = (
        (_('Uzbek'),{'fields':('name_uz','direction_uz')}),
        (_('Russian'),{'fields':('name_ru','direction_ru')}),
        (_('English'),{'fields':('name_en','direction_en')}),
        (_('Image'), {'fields': ('image',)}),
        (_('Link'), {'fields': ('facebook_link','twitter_link','linkedin_link','skype_link')}),
    )


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_uz','name_ru','name_en')
    fieldsets = (
        (_('Uzbek'),{'fields':('name_uz',)}),
        (_('Russian'),{'fields':('name_ru',)}),
        (_('English'),{'fields':('name_en',)}),
    )
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title_uz','title_ru','title_en')
    fieldsets = (
        (_('Uzbek'), {'fields': ('title_uz', 'description_uz')}),
        (_('Russian'), {'fields': ('title_ru', 'description_ru')}),
        (_('English'), {'fields': ('title_en', 'description_en')}),
        (_('Category'), {'fields': ('category', )}),
        (_('Image'), {'fields': ('image', )}),
        (_('Slug'), {'fields': ('slug', )}),
        (_('New'), {'fields': ('is_new', )}),
    )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name_uz','name_ru','name_en')
    fieldsets = (
        (_('Uzbek'),{'fields':('name_uz',)}),
        (_('Russian'),{'fields':('name_ru',)}),
        (_('English'),{'fields':('name_en',)}),
    )
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name_uz','name_ru','name_en')
    fieldsets = (
        (_('Uzbek'),{'fields':('name_uz','description_uz')}),
        (_('Russian'),{'fields':('name_ru','description_ru')}),
        (_('English'),{'fields':('name_en','description_en')}),
        (_('Image'), {'fields': ('image', )}),
    )

admin.site.register(Contact)