from django.conf.urls import path,re_path
from .. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('fashion',views.fashion,name = 'fashion'),
    path('search/', views.search_results, name='search_results'),
    re_path(r'image/(\d+)',views.image,name ='image'),
    re_path(r'location/(\d+)',views.filter_by_location,name='location')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)