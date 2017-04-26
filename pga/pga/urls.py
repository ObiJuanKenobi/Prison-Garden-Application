"""pga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView

from . import views
from pga.admin_views import *
from . import user_quiz_views
from . import admin_quiz_mgmt

urlpatterns = [

    #Home page & authentication-related urls:
    url(r'^$', views.home_page, name='home'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html', 'extra_context': views.get_home_page_dict() }, name='logout', ),
    

    #Admin urls:
    url(r'^admin/', admin.site.urls),
    url(r'^pgaadmin/unit/(?P<unit>[A-Za-z0-9\-\s]+)/supplementaryMaterials', AdminSuppMatView.as_view()),
    url(r'^pgaadmin/unit/(?P<unit>[A-Za-z0-9\-\s]+)/(?P<lesson>[A-Za-z0-9\-\s]+)', AdminLessonView.as_view()),
    url(r'^pgaadmin/unit/(?P<unit>[A-Za-z0-9\-\s]+)', AdminUnitView.as_view()),
    url(r'^pgaadmin/quiz/editQuestion', admin_quiz_mgmt.edit_quiz_question),
    url(r'^pgaadmin/quiz/editAnswer', admin_quiz_mgmt.edit_quiz_answer),
    url(r'^pgaadmin/quiz/(?P<unit>[A-Za-z0-9\-\s]+)', AdminQuizView.as_view()),
    url(r'^pgaadmin/quizStatistics/(?P<unit>[A-Za-z0-9\-\s]+)', adminQuizStatistics),
    url(r'^pgaadmin/quizStatistics', adminQuizStatisticsOverview),
    url(r'^pgaadmin/changeColor/(?P<course>[A-Za-z0-9\-\s]+)/(?P<color>[A-Za-z0-9\-\s]+)', adminSetCourseColor),
    url(r'^pgaadmin/userProgress/(?P<user>[A-Za-z0-9\-\s]+)', adminUserProgress),
    url(r'^pgaadmin/userProgress', adminUserProgressOverview),
    url(r'^pgaadmin/courseMgmt', CourseMgmtView.as_view()),#views.adminCourseMgmt),
    url(r'^pgaadmin/courseInfo', adminCourseInfo),
    url(r'^pgaadmin/', adminHome),

    #User-quiz urls:
    url(r'^takeQuiz/(?P<course>[A-Za-z0-9\-\s]+)', views.quiz_wrapper),
    url(r'^quiz/(?P<course>[A-Za-z0-9\-\s]+)', user_quiz_views.quiz, name='quiz'),
    url(r'^gradeQuiz/(?P<course>[A-Za-z0-9\-\s]+)', user_quiz_views.grade_quiz, name='quiz'),
    url(r'^quizResults/(?P<course>[A-Za-z0-9\-\s]+)', user_quiz_views.quiz_results, name='quizResults'),
    
    #General course urls:
    url(r'^lesson/(?P<course>[A-Za-z0-9\-\s]+)/(?P<lesson>[A-Za-z0-9\-\s\_]+)/', views.lesson, name='courseNav'),
    url(r'^gardenNav/', views.gardenNav, name='gardenNav'),
    url(r'^courseNav/(?P<course>[A-Za-z0-9\-\s]+)/', views.courseNav, name='courseNav'),

    #Demo url - remove
    url(r'^pests', views.pests, name='pests'),

    #Record keeping urls:
    url(r'^table_form/$', views.createRecordTable_Form, name='table_form'),
    url(r'^table_home/$', views.recordTable_Home, name='table_home'),
    
    #Garden planning urls:
    url(r'^garden/(?P<garden>[A-Za-z0-9\-\s]+)', views.garden, name='garden'),
    url(r'^savePlan/$', views.savePlan, name='savePlan'),
    url(r'^showPlans/$', views.showPlans, name='showPlans'),
    url(r'^deletePlan/$', views.deletePlan, name='deletePlan'),
    url(r'^getBedCanvas/$', views.getBedCanvas, name='getBedCanvas')
]

urlpatterns += staticfiles_urlpatterns()
