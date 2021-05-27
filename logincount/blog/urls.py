from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('about',views.about ,name="about"),
    path('contact',views.contact ,name="Contact"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('signup', views.user_signup, name="signup"),
    path('login', views.user_login, name="login"),
    path('logout', views.user_logout, name="logout"),

    #======post================
    path('addpost',views.add_post, name='addpost'),
    path('updatepost/<int:id>', views.update_post, name='updatepost'),
    path('deletepost/<int:id>', views.delete_post, name='deletepost'),

]