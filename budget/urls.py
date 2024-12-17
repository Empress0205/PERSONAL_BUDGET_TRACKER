from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),            # Home page
    path('register/', views.register, name='register'),  # Registration page
    path('login/', views.login, name='login'),      # Login page
    path('dashboard/', views.dashboard, name='dashboard'), # Dashboard page
    path('logout/', views.logout_view, name='logout'), 
    path('add_income/', views.add_income, name='add_income'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('history/', views.history, name='history'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)