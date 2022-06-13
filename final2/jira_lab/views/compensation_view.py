from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)
from rest_framework.response import Response

from jira_lab.models.compensation import Compensation
from jira_lab.serializers.compensation_serializer import CompensationSerializer


class CompensationListCreateAPIView(ListCreateAPIView):
    serializer_class = CompensationSerializer
    queryset = Compensation.objects.all()

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        request_serializer = self.get_serializer(data=request_data)
        request_serializer.is_valid(raise_exception=True)
        request_obj = request_serializer.save()
        print(request_data)
        board_name = request_data.pop('name')[0]
        print(board_name)
        request_obj.name= f'Compensation name : {board_name}'  # Property Injection

        updated_status = f'Updated by : {request_obj.status}'
        request_obj.set_status(updated_status)  # Interface Injection
        request_obj.save()
        return Response(request_serializer.data, status=status.HTTP_201_CREATED)


class CompensationRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CompensationSerializer
    queryset = Compensation.objects.all()
