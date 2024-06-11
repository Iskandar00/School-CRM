from modeltranslation.translator import TranslationOptions, register

from apps.groups.models import Subject


@register(Subject)
class SubjectTranslationOptions(TranslationOptions):
    fields = ('name',)
