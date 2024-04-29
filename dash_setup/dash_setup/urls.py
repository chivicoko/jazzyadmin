"""
URL configuration for dash_setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from bookstore.admin import bookstore_site
# from admin_dash.admin import profiler_site

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # custom admin side
    path('bookstore_site/', bookstore_site.urls),
    # path('profiler_site/', profiler_site.urls),

    path('', include('admin_dash.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.index_title = "SuperAdmin Panel"
admin.site.site_title = "SuperAdmin Page"
admin.site.site_header = "SuperAdmin Area"