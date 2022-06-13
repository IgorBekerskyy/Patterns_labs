"""jira URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from jira_lab.views.compensation_view import CompensationListCreateAPIView, CompensationRetrieveUpdateAPIView
from jira_lab.views.employee_view import EmployeeListCreateAPIView, EmployeeRetrieveUpdateAPIView
from jira_lab.views.csv_view import UploadDataCSVFile
from jira_lab.views.caretaker_view import CaretakerListCreateAPIView, CaretakerRetrieveUpdateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),



    path('caretaker/', CaretakerListCreateAPIView.as_view()),
    path('caretaker/<int:pk>/', CaretakerRetrieveUpdateAPIView.as_view()),

    path('compensation/', CompensationListCreateAPIView.as_view()),
    path('compensation/<int:pk>/', CompensationRetrieveUpdateAPIView.as_view()),

    path('employee/', EmployeeListCreateAPIView.as_view()),
    path('employee/<int:pk>/', EmployeeRetrieveUpdateAPIView.as_view()),

    path('test_csv/', UploadDataCSVFile.as_view()),
]
