from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


from shop import views

urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('products/', views.product_list, name='products'),

    path('team/', TemplateView.as_view(template_name='shop/news.html'), name='team'),

    #Блог
    path('blog/', TemplateView.as_view(template_name='shop/blog.html'), name='blog'),

    # О нас
    path('about/', TemplateView.as_view(template_name='shop/weo.html'), name='about'),

    # Вход
    path('login/', TemplateView.as_view(template_name='shop/vhod.html'), name='login'),

    # Регистрация
    path('register/', views.register, name='register'),
]

# для картинок товаров
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)