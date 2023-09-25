"""
URL configuration for Aptis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
app_name = 'Core'
from django.urls import path
from Core.views import *
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('speaking/', Speaking_p.as_view(), name='speaking'),
    path('speaking/<int:speaking_id>/', speaking_detail, name='speaking_detail'),
    path('speaking/<int:speaking_id>/delete/', speaking_detail, name='speaking_delete'),
    path('speaking/practice/<int:speaking_id>/delete/', speaking_practice_detail, name='speaking_practice_delete'),
    path('speaking/practice/', Speaking_practice.as_view(), name='speaking_practice'),
    path('speaking/practice/all/', Speaking_practice_all.as_view(), name='speaking_practice_all'),

    path('writing/', Writing_p.as_view(), name='writing'),
    path('writing/<int:writing_id>/', writing_detail, name='writing_detail'),
    path('writing/<int:writing_id>/delete/', writing_detail, name='writing_detail'),
    path('writing/practice/', Writing_practice.as_view(), name='writing_practice'),
    path('writing/practice/<int:speaking_id>/delete/', writing_practice_detail, name='writing_practice_delete'),

    path('writing/practice/all/', Writing_practice_all.as_view(), name='writing_practice_all'),
]
