from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="home"),  
	path('logout/', views.logoutUser, name="logout"),
   path('abc/', views.index, name="abc" ),
   path('apicheck/', views.api_check, name="apiviews" ),
   path('apiusers/', views.api_users, name="apiusers" ),
   path('apicreateuser/', views.api_createuser, name="apicreateuser" ),
   path('apiuserdetails/<int:pk>/', views.api_userdetails, name="apiusersdetails" ),
   path('apiuserupdate/<int:id>/', views.api_updateuser, name="apiuserupdate" ),
   path('apiuserdelete/<int:id>/', views.api_deleteuser, name="apiuserdelete" ),
   path('postspage/', views.postspage, name="postpage" ),
   path('postspage/<int:id>/', views.post, name="posts"),
   
]