from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from jira_lab.models.caretaker import Caretaker
from jira_lab.serializers.caretaker_serializer import CaretakerSerializer


class CaretakerListCreateAPIView(ListCreateAPIView):
    serializer_class = CaretakerSerializer
    queryset = Caretaker.objects.all()


class CaretakerRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CaretakerSerializer
    queryset = Caretaker.objects.all()
