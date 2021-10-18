from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from main.views import MainView, NasaPictureDetail

urlpatterns = [
                  path('', MainView.as_view()),
                  path('<int:pk>/', NasaPictureDetail.as_view(), name='photo-detail'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
