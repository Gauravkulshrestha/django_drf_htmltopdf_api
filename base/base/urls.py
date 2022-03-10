from django.contrib import admin
from django.urls import path
from pdf_convert.views import HTML_to_PDFView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pdf-api/', HTML_to_PDFView.as_view()), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
