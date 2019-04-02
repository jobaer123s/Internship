"""intern_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from login.views import home,user_login,user_signup,learn,user_logout
from post.views import post_list,postCreate,apply,contact,detail
from student.views import student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),

    #signup. login , logout url

    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('learn/', learn, name='learn'),

    #post, detail, apply, contact url

    path('', include('post.urls')),

    path('detail/<int:id>', detail, name='detail'),
    path('post/', postCreate, name='postCreate'),
    path('list/', post_list, name='post_list'),
    path('apply/<title>', apply, name='apply'),
    path('contact/', contact, name='contact'),

    #student url

    path('student/', student, name='student'),




]
