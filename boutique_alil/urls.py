
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# C:\Users\tranq\OneDrive\Bureau\boutique_alil\boutique_alil\urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),  
    path('', include('store.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


