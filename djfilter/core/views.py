from django.shortcuts import render
from .models import Journal
def BootstrapFilterView(request):
    qs = Journal.objects.all()
    title_contains_query = request.GET.get('tittle_contains')
    title_exact_query = request.GET.get('tittle_exact')
    title_or_author_query = request.GET.get('tittle_or_author')
    context = {
        'queryset': qs,

    }
    return render(request, "bootstrap_form.html" ,{})

