from django.urls import path
from . import views
app_name = 'sitemap'

urlpatterns = [
    path('', views.SitemapView.as_view(), name="sitemap"),
]