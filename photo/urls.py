from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns=[
    path('',views.fashion,name = 'fashion'),
    path('search/', views.search_results, name='search_results'),
    re_path(r'image/(\d+)',views.image,name ='image'),
    re_path(r'location/(\d+)',views.filter_by_location,name='location')
]

# urlpatterns=[
#     path('admin/', admin.site.urls),
#     path('views', views.index, name='index'),
# ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
