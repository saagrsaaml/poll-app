from django.contrib import admin

from .models import Question, Choice, Category


# shows choice form in line
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

# shows choice form in table
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class CategoryAdmin(admin.TabularInline):
    model = Category


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']

    list_display = ('get_categories', 'question_text', 'pub_date', 'was_published_recently', 'created_by')
    list_filter = ['pub_date']

    fieldsets = [
        ('Text Information', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
        ('Created By', {'fields': ['created_by']})
    ]
    inlines = [ChoiceInline,CategoryAdmin]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Category,CategoryAdmin)





