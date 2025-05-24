from rest_framework.decorators import api_view
from rest_framework.response import Response
from levelupapi.models import Gamer


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated Gamer

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']
    gamer = Gamer.objects.filter(uid=uid).first()

    if gamer is not None:
        data = {
            'id': gamer.id,
            'uid': gamer.uid,
            'bio': gamer.bio
        }
        return Response(data)
    else:
        data = {'valid': False}
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new gamer for authentication

    Method arguments:
      request -- The full HTTP request object
      '''

    gamer = Gamer.objects.create(
        bio=request.data['bio'],
        uid=request.data['uid']
    )

    data = {
        'id': gamer.id,
        'uid': gamer.uid,
        'bio': gamer.bio
    }
    return Response(data)
