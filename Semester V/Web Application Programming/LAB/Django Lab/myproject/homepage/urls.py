from django.urls import path
from homepage import views
# from homepage.views import index , contacts

urlpatterns = [
    path('',views.index,name='home'),
    path('contacts/',views.contacts,name='contacts'),
]