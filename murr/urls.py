from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('cards/', include('work_card.urls')),
    path('murrs/', include('card_murr.urls'))
]
