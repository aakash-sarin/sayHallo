from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def hallo(request):
    try:
        name = request.GET.get('name', None)
        if name is None: 
            return Response(
                {"error": "Missing 'name' parameter"},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = {
            'name': name,
            'message': f"Hallo {name}!"
        }
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e: 
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)