
from django.contrib import admin
from django.urls import path,include
from myApp import views
from rest_framework.urlpatterns import format_suffix_patterns
from .loginForm import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/',views.book_list ),
    path('book/<int:id>', views.book_detail),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
 

]

urlpatterns=format_suffix_patterns(urlpatterns)