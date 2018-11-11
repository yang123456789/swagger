from .models import Customer
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializer import GroupSerializer
from rest_framework import generics


class GroupViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a user instance.
    list:
        Return all users, ordered by most recently joined.
    create:
        Create a new user.
    delete:
        Remove an existing user.
    partial_update:
        Update one or more fields on an existing user.
    update:
    """
    get_view_description = '<p style="background: red">yerereuyreu</p>'
    queryset = Customer
    serializer_class = GroupSerializer
    # print(help(viewsets.ModelViewSet.get_view_description))
    http_method_names = ['get', 'post', 'put', 'delete']


    def create(self, request, *args, **kwargs):
        # "create"
        pass

    def list(self, request, *args, **kwargs):
        return Response([{'qweewew': 123323232}, {'qweewew': 123323232}])

    def retrieve(self, request, *args, **kwargs):
        return Response([{'qweewew': 123323232}, {'qweewew': 123323232}])

    def update(self, request, *args, **kwargs):
        return Response([{'qweewew': 123323232}, {'qweewew': 123323232}])

    def destroy(self, request, *args, **kwargs):
        return Response([{'qweewew': 123323232}, {'qweewew': 123323232}])

    def post(self, *args, **kwargs):
        """
            Create a MyModel
            ---
            parameters:
                - name: source
                  description: file
                  required: True
                  type: file
            responseMessages:
                - code: 201
                  message: Created
        """
        return super(GroupViewSet, self).post(self, *args, **kwargs)


from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
from .serializer import GroupSerializer

class MyModelView(generics.CreateAPIView):
    serializer_class = GroupSerializer
    parser_classes = (FormParser, MultiPartParser)

    def post(self, *args, **kwargs):
        """
            Create a MyModel
            ---
            parameters:
                - name: source
                  description: file
                  required: True
                  type: file
            responseMessages:
                - code: 201
                  message: Created
        """
        return super(MyModelView, self).post(self, *args, **kwargs)
