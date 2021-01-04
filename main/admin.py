from django.contrib import admin
from .models import *
# Register your models here.



admin.site.register(Competition)
admin.site.register(Pdf_question)
admin.site.register(Pdf_student_response)
admin.site.register(MCQ_question)
admin.site.register(MCQ_option)

admin.site.register(MCQ_student_response)

admin.site.register(FIB_question)
admin.site.register(FIB_student_response)

admin.site.register(Student_data)
admin.site.register(Expert_data)
admin.site.register(Attempted_contests)
admin.site.register(Game)

