from .models import Payment
from rest_framework import viewsets, permissions
from .serializers import PaymentSerializer

class PaymentViewSets(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PaymentSerializer
