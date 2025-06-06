from django.contrib import admin
from .models import *



# Register your models here.
#username=G*********5
#email:g**********.com
#password:************
# admin.py
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'pdf_file', 'apply_link')  # Display these fields in the admin interface
    search_fields = ('title',)




class gallery_Admin(admin.ModelAdmin):
     list_display = ('title', 'images', 'video', 'Description')  # Customize display
     search_fields = ('title',) 
     
admin.site.register(gallery,gallery_Admin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(student_login)
admin.site.register(faculty_login)
admin.site.register(Folder)
admin.site.register(File)
admin.site.register(cefacaulty)
admin.site.register(csefacaulty)
admin.site.register(course)
admin.site.register(courseselected)
admin.site.register(application_form)
admin.site.register(tutorapprovalform)
admin.site.register(studentsubjects)
admin.site.register(ecefaculty)
admin.site.register(eeefaculty)
admin.site.register(mefaculty)
admin.site.register(asfaculty)
