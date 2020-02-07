from django.contrib import admin
from django.urls import path
from p_library import views
from p_library.views import AuthorEdit, AuthorList  
from p_library import urls

from django.contrib import admin  
from django.urls import include, path  
from p_library.views import AuthorEdit, AuthorList, FriendsEdit, FriendsList 
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from p_library.views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many   


from .views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many    
from django.contrib import admin  
from django.urls import path  
from .views import AuthorEdit, AuthorList, FriendsEdit, FriendsList
from p_library.views import index, base, login, auth
from django.contrib.auth.views import LoginView, LogoutView

from p_library.views import index, RegisterView, CreateUserProfile  
from django.contrib.auth.views import LoginView, LogoutView  
from django.urls import reverse_lazy  
from django.urls import path
from allauth.account.views import login, logout
from allauth.socialaccount.models import SocialAccount     

app_name = 'p_library'  
urlpatterns = [  
    path('author/create', AuthorEdit.as_view(), name='author_create'),  
    path('authors', AuthorList.as_view(), name='author_list'),
    path('author/create_many', author_create_many, name='author_create_many'),  
    path('author_book/create_many/', author_create_many, name='author_book_create_many'), 
    path('friends/create', FriendsEdit.as_view(), name='friend_form'),  
    path('friends', views.index, name='index'),
    path('index/', index, name='index'),
    path('index/login', login, name='login'),  
	path('base/', base, name='base'),
	path('base/login', login, name='login'),
	path('', views.auth, name='auth'),  
    path('login/', login, name='login'),  
    path('logout/', logout, name='logout'),  
    path('register/', RegisterView.as_view(  
        template_name='register.html',  
		success_url=reverse_lazy('p_library:base')  
    ), name='register'),
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),
    path('auth/', views.auth, name='auth'),
    path('index/', views.index),


 

]