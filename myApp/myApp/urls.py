
from django.contrib import admin
from django.urls import path,include
from myApp import views
from rest_framework.urlpatterns import format_suffix_patterns

from myApp.views import register_user


urlpatterns = [

    path('admin/', admin.site.urls),
    path('book/',views.book_list ),
    path('book/<int:id>', views.book_detail),
    path('register/', register_user, name='register_user'),

   
]
    
    
     

  
  


urlpatterns=format_suffix_patterns(urlpatterns)