"""
URL configuration for djangopro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from djangoapp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('admin/', admin.site.urls),
    path('student/',views.student,name='student'),
    path('faculty/',views.Faculty,name='Faculty'),
    path('stulogin/',views.studentlogin,name='studentlogin'),
    path('',views.index),
    path('stulogout/',views.logout,name='logout'),
    path('studentdashboard/',views.studentdashboard,name='studentdashboard'),
    path('facultydashboard/',views.facultydashboard,name='facultydashboard'),
    path('facultylogout/',views.logout_faculty,name='logout_faculty'),
    path('fac_login/',views.faclogin,name='faclogin'),
    path('gallery/',views.pics,name='gallery'),
    path('notices/',views.notices,name='notices'),
    path('liveclass/',views.file_list,name='file_list'),
    path('facultyclass/',views.live_class_update,name='liveclassfaculty'),
    path('civilengineering/',views.civilengineering,name='civilengineering'),
    path('computerscience/',views.cse,name='cse'),
    path('electronics/',views.ece,name='ece'),
    path('mechanical/',views.Me_engineering,name='mechanical'),
    path('appliedscience/',views.applied,name='applied'),
    path('Electrical/',views.eee,name='eee'),
    path('cefaculty/',views.cefaculty,name='cefaculty'),
    path('cehod/',views.cehod,name="cehod"),
    path('cevisionmission/',views.cevission,name="cevission"),
    path('clubs/',views.ceclubs,name="ceclubs"),
   path('cefacilities/',views.cefacilities,name="cefacilities"),
   path("publications/",views.cepublications,name="cefacilities"),
   path("placement/",views.ceplacement,name="ceplacement"),
   path("Events/",views.ceevents,name="ceevents"),
   path("campus/",views.campus,name="campus"),
   path("governingbody/",views.governingbody,name="governingbody"),
   path("pta/",views.pta,name="pta"),
   path("principaldesk/",views.principaldesk,name="principaldesk"),
   path('courses/',views.courses,name="courses"),
   path('ugc/',views.ugc,name="ugc"),
   path("college_union/",views.collegeunion,name="collegeunion"),
   path("ourcollege/",views.ourcollege,name="ourcollege"),
   path("Contactus/",views.contactus,name="contactus"),
   path("csefaculty/",views.csefaculty,name="csefaculty"),
   path("csevission/",views.csevission,name="csevission"),
   path("cseevents/",views.cseevents,name="cseevents"),
   path("newsemester/",views.newsemester,name="newsemester"),
   path("applicationform/",views.application,name="application"),
   path("courseselection/",views.courseselection,name="course"),
   path("facultycourseselection/",views.facultycourse,name="facultycourse"),
   path("semesterupdate/<str:username>/",views.semformupdate,name="semformupdate"),
   path("courseupdate/<str:username>/",views.cousre_update,name="course_update"),
   path("applicationapproval/",views.tutorapproval,name="tutorapproval"),
   path("attendance_faculty/",views.attendance_faculty,name="attendance_faculty"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
