from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'question_text',
            ],
        }),
        (
            'Date information',
            {'fields': [
                'pub_date'
            ]}
        )
    ]

    inlines = [ChoiceInLine]

# Register your models here.
admin.site.register(Question, QuestionAdmin)
