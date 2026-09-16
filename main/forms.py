from django.forms import ModelForm, TextInput, DateInput, URLInput

from main.models import Education
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
            "grade": TextInput(
                attrs={
                    "placeholder": "elementary, junior high, senior high, college",
                }
            ),
            "started_at": DateInput(
                attrs={
                    "type": "date",
                    "min": datetime.date.today().strftime('%y-%m-%d'),
                }
            ),
            "ended_at": DateInput(
                attrs={
                    "type": "date",
                    "min": datetime.date.today().strftime('%y-%m-%d'),
                }
            ),
        }