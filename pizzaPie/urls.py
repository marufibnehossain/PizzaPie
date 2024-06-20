from django.contrib import admin
from django.urls import path
from pizza.views import index, login_page,register_page
from pizza import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),  # Homepage
    path('login/', views.login_page, name="login"),  # Login page
    path('postsign/', views.postsign, name='postsign'),
    path('signup/', views.register_page, name="signup"),  # Register page
]
