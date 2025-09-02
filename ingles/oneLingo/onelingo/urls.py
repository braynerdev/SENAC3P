from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CoreLogoutView.as_view(), name='logout'),
    path('cadastro/', views.CadastroView.as_view(), name='cadastro'),
    path('success/', views.SuccessView.as_view(), name='success'),
]