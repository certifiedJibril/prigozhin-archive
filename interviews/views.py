from django.shortcuts import render
from .models import Interview
from django.db.models import Q
from django.http import HttpResponse


def test_view(request):
    return HttpResponse("Hello from test view!")


def home_view(request):
    return render(request, "home.html")


def search_view(request):
    query = request.GET.get("q", "")
    language = request.GET.get("lang", "both")
    date_from = request.GET.get("from")
    date_to = request.GET.get("to")

    interviews = Interview.objects.all()

    if query:
        if language == "ru":
            interviews = interviews.filter(original_text_ru__icontains=query)
        elif language == "en":
            interviews = interviews.filter(translation_en__icontains=query)
        else:
            interviews = interviews.filter(
                Q(original_text_ru__icontains=query) | Q(
                    translation_en__icontains=query)
            )

    if date_from:
        interviews = interviews.filter(date__gte=date_from)
    if date_to:
        interviews = interviews.filter(date__lte=date_to)

    return render(request, "search_results.html", {"interviews": interviews, "query": query})
