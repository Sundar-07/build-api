from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.index,name='index'),
    path('project',views.ProjectList.as_view(),name='project-list'),
    path('project/<int:unit_status>',views.ProjectDetail.as_view(),name='project-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)


