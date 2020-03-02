from django.urls import include, path
from rest_framework import routers
from exam.views import CourseViewSet, TestViewSet
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'tests', TestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
]
