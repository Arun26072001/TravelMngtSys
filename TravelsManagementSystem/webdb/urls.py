
from django.contrib import admin
from django.urls import path, include
from authorize import views
from django.contrib.auth.views import LogoutView, LoginView
from django.views.static import serve 
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    
    path('secret/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('auth/', views.auth, name='index'),
    path('welcome/<str:accesses>', views.welcome, name='welcome'),
    path('enquiry/<str:MobNum>',views.enquiry, name='enquiry'),
    path('allotment/<str:MobNum>',views.allotment, name='alart'),
    path('vehicle_details/<str:MobNum>',views.driver, name='driver'),
    path('datatable/<str:date>',views.datatable, name='datatable'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('admin/defender/', include('defender.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    
    
]


urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

handler404 = 'authorize.views.error_404'