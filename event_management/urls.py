 
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from events.views import EventListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('events.urls' )),
    path('users/', include('users.urls')),
    # path('', EventListView.as_view(), name='home'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
