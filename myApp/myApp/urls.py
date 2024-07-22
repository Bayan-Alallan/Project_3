
from django.contrib import admin
from django.urls import path,include
from myApp import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token


from myApp.views import register_user


urlpatterns = [

    path('admin/', admin.site.urls),
    path('book/',views.book_list ),
    path('book/<int:id>', views.book_detail),
    path('register/', views.register_user, name='register_user'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),


   
]
    
    
     

  
  


urlpatterns=format_suffix_patterns(urlpatterns)