from django.contrib import admin
from .models import Question, Answer, QuestionComment, AnswerComment, AnswerPoint, QuestionPoint, TagDetails
from django_summernote.admin import SummernoteModelAdmin



class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    #summernote_fields = ('content',)

#admin.site.register(SomeModelAdmin)
admin.site.register(Question,SomeModelAdmin)
#admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionComment)
admin.site.register(AnswerComment)
admin.site.register(AnswerPoint)
admin.site.register(QuestionPoint)
admin.site.register(TagDetails)
