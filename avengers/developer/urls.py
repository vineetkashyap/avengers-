from django.urls import path
from . import views
urlpatterns = [
     path('',views.MyView.as_view(),name='home'),
     path('edit/<int:id>/',views.MyView.as_view(),name='edit'),
     path('del/<int:id>',views.MyView.as_view(),name='del'),
     
]
