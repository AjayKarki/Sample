from rest_framework import routers
from demoapp import viewsets

router = routers.DefaultRouter()
router.register('subject', viewsets.SubjectViewSet)

for url in router.urls:
    print(url)

    # a4ee57a7a9a4da1ca3123a32206d38a617b00a78