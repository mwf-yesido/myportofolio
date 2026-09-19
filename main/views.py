from django.shortcuts import render

from main.models import Experience, Education

from main.forms import EducationForm, ExperienceForm
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

def show_main(request):
    context = {
        "name": "Wildan",
        "full_name": "Muhammad Wildan Firdaus",
        "npm": "2506595985",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "From the, as they say, doomed study of Computer Science at Universitas Indonesia, I rise with nothing but a bit of excitement, curiosity, and determination to fight my inner demon, laziness."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    json_response = get_experience_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Wildan",
        "project_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def show_education(request):
    json_response = get_education_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [education.object for education in educations]
    school_name_query = request.GET.get("title", "").strip()

    context = {
        "name": "Burhan",
        "education_list": educations,
        "school_name_query": school_name_query,
    }
    return render(request, "education.html", context)

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat pendidikan baru berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Wildan",
        "form": form,
    }
    return render(request, "education_form.html", context)

def get_education_json(request):
    school_name_query = request.GET.get("school_name", "").strip()
    educations = Education.objects.all()

    if school_name_query:
        educations = educations.filter(school_name__icontains=school_name_query)

    educations_json = serializers.serialize("json", educations)
    return HttpResponse(educations_json, content_type="application/json")

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Riwayat pendidikan berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experiences")

    context = {
        "name": "Wildan",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.all()

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    experience_json = serializers.serialize("json", experience)
    return HttpResponse(experience_json, content_type="application/json")

def delete_experience(request, project_id):
    experience = get_object_or_404(Experience, pk=project_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")