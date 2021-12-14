"""helllo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from todolist import views

urlpatterns = [
    path('', include('todolist.urls')),
    path('admin/', admin.site.urls),
    path('contactapi/<int:pk>/', views.contact_details),
    path('contactapi/', views.contact_list),
    path('contactdata/', views.contact_data, name="contactdata"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('<int:id>/update', views.update_data, name="updatedata"),
    path('stu/', views.student_create, name="studata"),
]
