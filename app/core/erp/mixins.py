from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages


class ValidatePermissionRequiredMixin(object):
    permission_required = ''
    url_redirect = None

    def get_perms(self):
        # perms = []
        if isinstance(self.permission_required, str):
            perms = (self.permission_required,)
        else:
            perms = (self.permission_required)
        return perms

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('app:dashboard')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'No tienes permisos para ingresar a este Módulo')
        return HttpResponseRedirect(self.get_url_redirect())
