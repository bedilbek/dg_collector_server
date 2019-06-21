from rest_framework import routers

from collector.views import DataViewSet

router = routers.SimpleRouter()
router.register('collector', DataViewSet, 'collector')

urlpatterns = router.urls

