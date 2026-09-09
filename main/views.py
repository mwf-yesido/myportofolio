from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Wildan",
        "npm": "2506595985",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "From the, as they say, doomed study of Computer Science at Universitas Indonesia, I rise with nothing but a bit of excitement, curiosity, and determination to fight my inner demon, laziness."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Wildan",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)