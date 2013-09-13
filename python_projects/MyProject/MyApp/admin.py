from django.contrib import admin
from orm_app.models import Poll, PollAnswer



class PollAnswerAdmin(admin.ModelAdmin):
	fields = []
	readonly_fields = ("vote_count",)

	# exclude, readonly or fields[include], depending on the amount of typing you want to do

admin.site.register(Poll)
admin.site.register(PollAnswer, PollAnswerAdmin)
