from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return self.question

class PollAnswer(models.Model):
    poll = models.ForeignKey(Poll, related_name="answers")
    answer = models.CharField(max_length=255)
    vote_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.answer

class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    poll = models.ForeignKey(Poll)


