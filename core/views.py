from django.views.generic import FormView
from django.urls import reverse_lazy
from .models import Servico, Funcionario, Feature
from .forms import ContatoForm
from django.contrib import messages


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)  # Recuperando o contexto da página
        context['servicos'] = Servico.objects.order_by(
            '?').all()  # Recuperando todos os serviços no BD e ordenando de forma aleatória os dados
        context['funcionarios'] = Funcionario.objects.order_by('?').all()  # Recuperando todos os funcionários no BD
        context['features'] = Feature.objects.all()[3:6]
        context['features1'] = Feature.objects.all()[:3]
        print(Feature.objects.all()[3:7])
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail!')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

