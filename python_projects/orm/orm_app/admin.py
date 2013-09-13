from django.contrib import admin
from orm_app.models import Poll, PollAnswer, Comment

class PollAnswerAdmin(admin.ModelAdmin):
	readonly_fields = ("vote_count",)

class CommentInlineAdmin(admin.TabularInline):
    model = Comment
    max_num = 1
    extra = 1

class PollAnswerInlineAdmin(admin.StackedInline):
    model = PollAnswer
    readonly_fields = ("vote_count",)

class PollAdmin(admin.ModelAdmin):
    inlines = [CommentInlineAdmin, PollAnswerInlineAdmin]

admin.site.register(Poll, PollAdmin)
admin.site.register(PollAnswer, PollAnswerAdmin)

