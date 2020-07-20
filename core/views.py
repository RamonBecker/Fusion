from django.views.generic import TemplateView
from .models import Servico, Funcionario, Feature


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs) #Recuperando o contexto da página
        context['servicos'] = Servico.objects.order_by('?').all() #Recuperando todos os serviços no BD e ordenando de forma aleatória os dados
        context['funcionarios'] = Funcionario.objects.order_by('?').all() #Recuperando todos os funcionários no BD
        context['features'] = Feature.objects.all()[3:6]
        context['features1'] = Feature.objects.all()[:3]
        print(Feature.objects.all()[3:7])
        return context



