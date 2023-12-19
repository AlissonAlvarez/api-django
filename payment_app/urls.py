from rest_framework import routers
from .api import PaymentViewSets

router = routers.DefaultRouter()

router.register('api/payment-tc/process', PaymentViewSets, 'payment_app')


urlpatterns = router.urls