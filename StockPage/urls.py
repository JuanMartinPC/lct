from django.urls import path
from StockPage import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.productos, name='inicio'),
    path('productos', views.productos, name='productos'),
    path('crear', views.crear, name='crear'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)