from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny  # Import AllowAny

class HomeView(APIView):
    permission_classes = [AllowAny]  # Allow access without authentication
    def get(self, request):
        return Response({"message": "Welcome to the Fitness Tracker API!"})