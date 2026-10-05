from django.urls import path

from main.views import (
    show_main,
    show_experience,
    show_education,
    create_education,
    get_education_json,
    delete_education,
    create_experience,
    get_experience_json,
    delete_experience,
    register,
    login_user,
    logout_user,
    toggle_star_edu,
    toggle_star_exp,
    update_education,
    update_experience,
    create_education_ajax,
    create_experience_ajax,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("education/add", create_education, name="create_education"),
    path("api/education/", get_education_json, name="get_education_json"),
    path("education/<uuid:education_id>/delete/",delete_education,name="delete_education"),
    path("experience/add", create_experience, name="create_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("education/<uuid:education_id>/star/", toggle_star_edu, name="toggle_star_edu"),
    path("education/<uuid:education_id>/update/", update_education, name="update_education"),
    path("experience/<uuid:experience_id>/star/", toggle_star_exp, name="toggle_star_exp"),
    path("experience/<uuid:experience_id>/update/", update_experience, name="update_experience"),
    path("education/add-ajax/", create_education_ajax, name="create_education_ajax"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
]