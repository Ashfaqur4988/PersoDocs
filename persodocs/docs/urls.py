from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('docs/<int:doc_id>/', views.doc_detail, name='doc_detail'),
    path('generate/<int:doc_id>/', views.generate_doc, name='generate_doc'),
    path('delete/<int:doc_id>/', views.delete_doc, name='delete_doc'),
    path('update/<int:doc_id>/', views.update_doc, name='update_doc'),
    path('user_guide/', views.user_guide, name='user_guide'),
    path('register/', views.register, name='register'),
    
]