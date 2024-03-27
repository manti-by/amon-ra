from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView

from amon_ra.api.permissions import KeyPermission


class HashedDataView(CreateAPIView):
    permission_classes = (KeyPermission,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            raise ValidationError
        return serializer.serialize()
