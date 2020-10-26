from django.contrib import admin
from django.urls import path
from search import views as search_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search_views.search),
]
