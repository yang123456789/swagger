from rest_framework import serializers, viewsets
from api.models import Customer
from rest_framework.response import Response


class GroupSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=30, required=True, help_text='qeqwewwrw', allow_blank=True
    )
    age = serializers.IntegerField(
        required=True, help_text='qeqwewwrw'
    )
    class Meta:
        model = Customer
        fields = '__all__'


class UserViewSet(viewsets.ModelViewSet):
    """
    create:
         创建

        {
        "code": 200
        }
    """
    serializer_class = GroupSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        return Response([{'qweewew': 123323232}, {'qweewew': 123323232}])

    def retrieve(self, request, *args, **kwargs):
        return Response([{'qweewew': 123323232}, {'qweewew': 123323232}])

    def update(self, request, *args, **kwargs):
        return Response([{'qweewew': 123323232}, {'qweewew': 123323232}])

    def destroy(self, request, *args, **kwargs):
        return Response([{'qweewew': 123323232}, {'qweewew': 123323232}])
