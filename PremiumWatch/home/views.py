from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class HomePageView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            "message": "Welcome to the PremiumWatch API!",
            "available_endpoints": [
                "users/",
                "api/token",
                "api/token/refresh/",
                "subscriptions/",
                "videos/",
            ],
        })
