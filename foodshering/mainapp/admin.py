from django.contrib import admin
from .models import Question, Result, Answer


class QuestionsInline(admin.TabularInline):
    model = Answer


@admin.register(Question)
class BookAdmin(admin.ModelAdmin):
    inlines = [QuestionsInline]


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display=("ProfileId", "DateTime", "UserName", "Rating")

    def has_add_permission(self, request):
        return False
