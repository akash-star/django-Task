from django.urls import path, include
from scheduling.views import CallingViewScheduler, ServerStateView 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('main-content', CallingViewScheduler, basename='main-view')


urlpatterns = [
    path('', include(router.urls)),
    path('ping/', ServerStateView.as_view(), name='ping-test')
]

