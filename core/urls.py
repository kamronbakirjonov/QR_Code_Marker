
from django.contrib import admin
from django.urls import path

from main.views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,QRCodeGeneratorView.as_view(), name='qr_code_generator'),
    path('qr-codes/',QRCodesView.as_view(), name='qr_code'),
    path('qr_code/<int:qr_code_id>/', QRCodeDetailsView.as_view()),
    path('students/',StudentsView.as_view(), name='students'),
    path('from/', StudentRequestView.as_view() ,name='student_request'),
    path('success/', StudentSuccessView.as_view(),name='student_success'),
] +  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
