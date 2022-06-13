import csv

from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from jira_lab.models.employee import Employee
from jira_lab.serializers.employee_serializer import EmployeeSerializer


class UploadDataCSVFile(ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def create(self, request, *args, **kwargs):
        file = request.data.get('chapter')
        file_rows = [row.decode("utf-8") for row in file]
        reader = csv.reader(file_rows, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL)
        for chapter in reader:
            if chapter:
                request_data = format_data(chapter)
                create_request_record(request_data)  # method injection
        return Response('Check it', status=status.HTTP_201_CREATED)


def format_data(chapter):

    request_data = {"id": chapter.pop(0),
                    "name": chapter.pop(0),
                    "icon": chapter.pop(0)
                    }

    return request_data


def create_request_record(request_data):
    chapter_serializer = EmployeeSerializer(data=request_data)
    chapter_serializer.is_valid(raise_exception=True)
    request_obj = chapter_serializer.save()

    request_obj.save()

    return True
