from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)

from jira_lab.models.employee import Employee
from jira_lab.serializers.employee_serializer import EmployeeSerializer


class EmployeeListCreateAPIView(ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
