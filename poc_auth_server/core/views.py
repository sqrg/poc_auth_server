from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from fcm_django.models import FCMDevice


class RegisterDevice(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        device_id = request.POST['device_id']

        user = User.objects.get(pk=request.user.pk)
        user.profile.device_id = device_id
        user.save()

        # TODO: Research
        update_session_auth_hash(request, user)

        return Response({
            'ok': True,
            'details': 'The device ID has been registered to the user'
        })
