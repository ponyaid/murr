from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from work_card.forms import WorkCardForm
from .models import WorkCard, Rubric


def index(request):
    all_murrs = WorkCard.objects.all()
    rubrics = Rubric.objects.all()
    context = {'all_murrs': all_murrs, 'rubrics': rubrics}
    return render(request, 'work_card/all_murrs.html', context)


def by_rubric(request, rubric_id):
    murr_list_by_rubric_id = WorkCard.objects.filter(rubric=rubric_id)
    all_rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'murr_list_by_rubric_id': murr_list_by_rubric_id,
        'all_rubrics': all_rubrics,
        'current_rubric': current_rubric
    }
    return render(request, 'work_card/by_rubric.html', context)


class WorkCardCreateView(CreateView):
    template_name = 'work_card/create_murr.html'
    form_class = WorkCardForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
