from django.db import models


class UserPost(models.Model):
    text = models.TextField(max_length=500)
    date_added = models.DateTimeField(
        auto_now_add=True)
    author = models.CharField(default='Eau de Web',
                              max_length=20)

    def __unicode__(self):
        return u'{} @ {}'.format(self.author,
                                 self.date_added)