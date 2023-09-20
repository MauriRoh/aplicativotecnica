from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.shortcuts import render


<<<<<<< HEAD
class DashboardView(LoginRequiredMixin, TemplateView):
=======
class DashboardView(TemplateView):
>>>>>>> 4a1072f9275fe6614ea2334a2d772d86181835c3
    template_name = 'dashboard.html'

    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)
    #
    # def get(self, request, *args, **kwargs):
    #     request.user.get_group_session()
    #     return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# Paginas de ERRORES
def page_not_found404(request, exception):
    return render(request,'404.html')