from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view),
    path('admin/', admin.site.urls),
    path('login/', views.login_view),
    path('feed/', views.feed_view),
]