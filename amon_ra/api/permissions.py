from django.utils import timezone
from rest_framework.permissions import BasePermission

from amon_ra.apps.clients.models import Client


class KeyPermission(BasePermission):

    def has_permission(self, request, view) -> bool:
        if request.data.get("key") and (client := Client.objects.filter(key=request.data.get("key")).last()):
            request.api_client = client
            client.last_request_at = timezone.now()
            client.save()
            return True
        return False
