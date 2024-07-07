from django import forms

from apps.subjects.models import Subject


class SubjectCreateForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['price', 'name', 'slug', 'published_at', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
