from rest_framework.routers import DefaultRouter
from .views import ShopViewSet

router = DefaultRouter()
#router.register('products', ProductViewSet)
router.register('shop', ShopViewSet)
urlpatterns = router.urls

