from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.tax.models import TaxRate
from apps.tax.serializers import TaxRateSerializer
from apps.utils.helpers.django import get_object_or_none


class TaxRateByZipView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        postcode = request.query_params.get('postcode')
        if not postcode:
            return Response({'error': 'postcode is required'}, status=status.HTTP_400_BAD_REQUEST)

        tax_rate = get_object_or_none(TaxRate, **{'zipcode': postcode})
        if not tax_rate:
            return Response({'error': 'tax rate not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaxRateSerializer(tax_rate)

        return Response(serializer.data, status=status.HTTP_200_OK)
