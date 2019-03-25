from django.urls import path

from .views import index, by_rubric, WorkCardCreateView


urlpatterns = [
    path('', index, name='index'),  # show all murrs
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),  # show all murrs by specific rubric
    path('add/', WorkCardCreateView.as_view(), name='add')  # add murr
]
