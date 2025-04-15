from django.urls import path
from . import views
from .views import VacancyList, VacancyDetail

urlpatterns = [
    path('companies/', views.company_list, name='company-list'),
    path('companies/<int:id>/', views.company_detail, name='company-detail'),
    path('companies/<int:id>/vacancies/', views.company_vacancies, name='company-vacancies'),
    path('cbv/vacancies/', VacancyList.as_view(), name='vacancy-list'),
    path('cbv/vacancies/<int:id>/', VacancyDetail.as_view(), name='vacancy-detail'),
    path('vacancies/top_ten/', views.top_ten_vacancies, name='top-ten-vacancies'),
]