from django import forms
from django.http import Http404
from django.forms.utils import ErrorList


class OwnerPostMixin(object):
    def form_valid(self, form):
        '''only the posts owner can edit them, not even the admin'''
        if form.instance.user == self.request.user:
            return super(UserOwnerMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(
            ["This user is not allowed to change this data."]
            )
            return self.form_invalid(form)


class OwnerOrAdminMixin(object):
    '''
    Ensure that post deletion can be performed
    either by the post owner or an admin
    '''
    def get_object(self, queryset=None):
        obj = super(OwnerDeleteMixin, self).get_object()
        if self.request.user.is_staff or self.request.user.is_superuser:
            return obj

        if not obj.user == self.request.user:
            raise Http404
        return obj
