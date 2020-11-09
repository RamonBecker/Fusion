from django.views.generic import FormView
from django.urls import reverse_lazy
from .models import Servico, Funcionario, Feature

from .forms import ContatoForm
from django.contrib import messages
from django.utils.translation import gettext as _
from django.utils import translation


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)  # Recuperando o contexto da página
        lang = translation.get_language() #pegando a lingua do navegador
        context['servicos'] = Servico.objects.order_by(
            '?').all()  # Recuperando todos os serviços no BD e ordenando de forma aleatória os dados
        context['funcionarios'] = Funcionario.objects.order_by('?').all()  # Recuperando todos os funcionários no BD
        context['features'] = Feature.objects.all()[3:6]
        context['features1'] = Feature.objects.all()[:3]
        context['lang'] = lang
        translation.activate(lang)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _('E-mail com sucesso!')) #traduzindo mensagem
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Erro ao enviar e-mail!')) #traduzindo mensagem
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

