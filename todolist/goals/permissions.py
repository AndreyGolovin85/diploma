from rest_framework import permissions

from goals.models import BoardParticipant


class BoardPermissions(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        filters = {"user": request.user, "board": obj}
        if request.method not in permissions.SAFE_METHODS:
            filters["role"] = BoardParticipant.Role.owner

        return BoardParticipant.objects.filter(**filters).exists()
