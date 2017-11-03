from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    '''
    Used sepcifically for editing posts.
    Only post owner can edit her post.
    '''
    def has_object_permission(self, request, view, obj):
        # can view but cannot edit
        if request.method in SAFE_METHODS:
            return True

        # the obj profile id matches logged in user id
        return obj.user.id == request.user.id


class IsOwnerOrAdmin(BasePermission):
    '''
    Used sepcifically for post deletion.
    Only post owner or admin can delete a post.
    '''
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        # the obj profile id matches logged in user id
        return obj.user.id == request.user.id
