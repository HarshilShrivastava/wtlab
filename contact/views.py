from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view,permission_classes
from .serializers import queryserializer
from rest_framework.response import Response
from .models import     Contactus
from rest_framework.permissions import AllowAny



@permission_classes((AllowAny,))
@api_view(['POST',])
def Createmessage(request):
    data={}
    if request.method=="POST":
        serializer=queryserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data['status']=200
            data['message']="sucessfully sent "

            return Response(data)
        else:
            data['status']=400
            data['message']=serializer.error
            return Response(data)