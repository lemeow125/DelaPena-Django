from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'subjects', views.SubjectViewSet)
router.register(r'subjects_professors', views.SubjectProfessorViewSet)
router.register(r'subjects_students', views.SubjectStudentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),

]
