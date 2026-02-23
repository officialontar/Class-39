from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_student/', views.add_student, name='add_student'),
    path('all_student/', views.all_student, name='all_student'),
    path('content/', views.content, name='content'),
    path('detele_student/<int:std_id>', views.detele_student, name='detele_student'),
    path('edit_student/<int:std_id>', views.edit_student, name='edit_student'),

]