# aqui se esta importando response para que se visualize como json
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person = {'name':'mike', 'age':31}
    return Response(person)