from modeltranslation.translator import register, TranslationOptions
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
    )


@register(Slider)
class SliderTranslateOptions(TranslationOptions):
    fields = ('title','description')
    
    
@register(About)
class AboutTranslateOptions(TranslationOptions):
    fields = ('title','description')
    
@register(OurHistory)
class OurHistoryTranslateOptions(TranslationOptions):
    fields = ('description',)
    
@register(Result)
class ResultTranslateOptions(TranslationOptions):
    fields = ('name',)

@register(AboutCard)
class AboutCardTranslateOptions(TranslationOptions):
    fields = ('name','description')
    
@register(Teacher)
class TeacherTranslateOptions(TranslationOptions):
    fields = ('name','direction')
    
@register(Blog)
class BlogTranslateOptions(TranslationOptions):
    fields = ('title','description',)
    
@register(BlogCategory)
class BlogCategoryTranslateOptions(TranslationOptions):
    fields = ('name',)
    
@register(Tag)
class TagTranslateOptions(TranslationOptions):
    fields = ('name',)
    
@register(Course)
class CourseTranslateOptions(TranslationOptions):
    fields = ('name', 'description')