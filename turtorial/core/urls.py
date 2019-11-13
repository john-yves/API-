from django.urls import path,include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('languages',views.LanguageView)
router.register('contents',views.Contentview)
router.register('programmers',views.Programmerview)



urlpatterns = [
    path('',include(router.urls))
]
