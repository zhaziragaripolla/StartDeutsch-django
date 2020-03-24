from django.urls import include, path
from rest_framework import routers
from exam.views import *
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'tests', TestViewSet)
router.register(r'listening-questions', ListeningQuestionViewSet)
router.register(r'reading-questions', ReadingQuestionViewSet)
router.register(r'letters', LetterViewSet)
router.register(r'forms', FormViewSet)
router.register(r'words', WordViewSet)
router.register(r'cards', CardViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
]
