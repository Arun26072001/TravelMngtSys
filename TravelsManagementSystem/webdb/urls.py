
from django.contrib import admin
from django.urls import path, include
from authorize import views
from django.contrib.auth.views import LogoutView, LoginView



urlpatterns = [
    
    path('secret/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('', views.auth, name='index'),
    path('welcome/<str:accesses>', views.welcome, name='welcome'),
    path('enquiry/<str:MobNum>',views.enquiry, name='enquiry'),
    path('allotment/<str:MobNum>',views.allotment, name='alart'),
    path('vehicle_details/<str:MobNum>',views.driver, name='driver'),
    path('datatable/<str:date>',views.datatable, name='datatable'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('admin/defender/', include('defender.urls')),
    
    
]



handler404 = 'authorize.views.error_404'