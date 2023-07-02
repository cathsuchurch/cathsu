from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_login, name='render_login'),
    path('perform_login', views.perform_login, name='perform_login'),
    path('perform_logout', views.perform_logout, name='perform_logout'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('all_members', views.all_members, name='all_members'),
    path('add_member', views.add_member, name='add_member'),
    path('executive', views.executive, name='executive'),
    path('document', views.document, name='document'),
    path('active_members', views.active_members, name='active_members'),
    path('affiliate_members', views.affiliate_members, name='affiliate_members'),
    path('patrons', views.patrons, name='patrons'),



]
