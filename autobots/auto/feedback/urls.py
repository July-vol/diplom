from django.urls import path
from .views import FeedBackView, FeedBacksView
from feedback import views
urlpatterns = [
    path('', FeedBackView.as_view(), name='feedback_view'),
    path('', FeedBacksView.as_view(), name='feedbacks_view'),
    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
    # feedback
    path('current', views.currenttodos, name='currenttodos'),
    path('create/', views.createtodo, name='createtodo'),
    path('feedback/<int:feedback_pk>/', views.viewtodo, name='viewtodo'),


]
