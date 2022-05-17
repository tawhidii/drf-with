from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from users.api.serializers import RegistrationSerializer

@api_view(['POST',])
def register_user(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            user_token = Token.objects.get(user=account)
            print(user_token)
        else:
            return Response(serializer.errors)
        return Response(serializer.errors)

