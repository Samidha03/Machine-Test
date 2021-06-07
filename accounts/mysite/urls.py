from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.register,name='register'),
    path('client_register/',views.client_register.as_view(),name='client_register'),
    path('project_register/',views.project_register.as_view(),name='project_register'),
    path('login/',views.login_request, name='login'),
    path('logout/',views.logout_view, name='logout'),
]
