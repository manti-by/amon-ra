from rest_framework.generics import CreateAPIView

from amon_ra.api.permissions import KeyPermission


class HashedDataView(CreateAPIView):
    permission_classes = (KeyPermission,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return serializer.serialize()
