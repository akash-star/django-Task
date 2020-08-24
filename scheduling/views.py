from django.shortcuts import render,redirect
from django.http import JsonResponse
import datetime

from rest_framework import permissions
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SchedulingCallSerializers
from .models import Scheduler
generics.GenericAPIView

# Create your views here.

class CallingViewScheduler(viewsets.ModelViewSet):
    
    """ Creating and Listing Scheduler class objects.
    """

    serializer_class = SchedulingCallSerializers

    def get_queryset(self, *args, **kwargs):
        query = Scheduler.objects.all()
        for obj in query:
            print(obj)
            print(datetime.datetime.now(), obj.timestamp)
            if datetime.datetime.now() == obj.timestamp:

            	return redirect(obj.site_url)

        return Scheduler.objects.all()


    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params)
        try: 
            params_list = params['pk'].split('-')
            obj = Scheduler.objects.filter(timestamp=params_list[0], site_url=params_list[1])
        except Exception as e:
            obj = Scheduler.objects.filter(site_url=params)
        print(obj)
        serializer = SchedulingCallSerializers(obj, many=True)
        return Response(serializer.data)


class ServerStateView(APIView):
	def get(self,reuest, *args, **kwargs):
		state= {"status":"OK"}
		return Response(state)


	"""To send response to the endpoint '/ping' which return a response
     of 'status': 'OK' to make sure that the server is alive
     """