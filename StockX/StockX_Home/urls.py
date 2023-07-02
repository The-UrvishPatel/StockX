from django.contrib import admin
from django.urls import path,include
from StockX_Home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.indexpage, name="IndexPage"),
    # path('<str:symbol>', views.indexpage, name="IndexPage"),
    path('data', views.indexpage_data, name="DataPage"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)