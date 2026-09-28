from django.forms import ModelForm, TextInput, DateInput, URLInput, Textarea, Select

from main.models import Education, Experience
import datetime

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "school_name", 
            "grade",
            "started_at",
            "ended_at",
        ]

        labels = {
            "school_name": "Nama Sekolah/Institusi", 
            "grade": "Tingkat Sekolah/Institusi",
            "started_at": "Dimulai pada",
            "ended_at": "Lulus pada",
        }

        widgets = {
            "school_name": TextInput(
                attrs={
                    "placeholder": "Masukkan nama sekolah/universitas/institusi",
                    "maxlength": 255,
                }
            ),
            "grade": Select(
                choices=[
                    ('elementary', 'Elementary School'),
                    ('junior', 'Junior High School'),
                    ('senior', 'Senior High School'),
                    ('college', 'College'),
                ]
            ),
            "started_at": DateInput(
                format='%Y-%m-%d',
                attrs={
                    "type": "date",
                    "min": datetime.date.today().strftime('%y-%m-%d'),
                }
            ),
            "ended_at": DateInput(
                format='%Y-%m-%d',
                attrs={
                    "type": "date",
                    "min": datetime.date.today().strftime('%y-%m-%d'),
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title", 
            "description",
            "category",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Judul pengalaman", 
            "description": "Deskripsi pengalaman",
            "category": "Kategori pengalaman",
            "thumbnail": "Thumbnail pengalaman",
            "started_at": "Dimulai pada",
            "ended_at": "Lulus pada",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Masukkan judul pengalaman",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "category": Select(
                choices= [
                    ('internship', 'Internship'),
                    ('research', 'Research'),
                    ('volunteer', 'Volunteer'),
                    ('part-time', 'Part-Time'),
                    ('full-time', 'Full-Time'),
                    ('freelance', 'Freelance'),
                ]
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "started_at": DateInput(
                format='%Y-%m-%d',
                attrs={
                    "type": "date",
                    "min": datetime.date.today().strftime('%y-%m-%d'),
                }
            ),
            "ended_at": DateInput(
                format='%Y-%m-%d',
                attrs={
                    "type": "date",
                    "min": datetime.date.today().strftime('%y-%m-%d'),
                }
            ),
        }