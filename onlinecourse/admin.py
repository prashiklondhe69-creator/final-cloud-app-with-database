from django.contrib import admin
# Task 2 requires importing these 7 classes
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'grade']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    inlines = [QuestionInline]


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class InstructorAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_learners')


class LearnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'occupation')


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('enrollment',)


# Register all models with their custom Admin views
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Learner, LearnerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission, SubmissionAdmin)
