from django.db import models
from django.contrib.postgres.fields import ArrayField


class Color(models.Model):
    value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.value


class Case(models.Model):
    slug = models.SlugField(primary_key=True, unique=True)
    name = models.TextField(blank=True)
    name_abbreviation = models.CharField(max_length=255, blank=True)
    decision_date = models.DateField(null=True, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.slug


class ColorExcerpt(models.Model):
    color = models.ForeignKey('Color', blank=True, null=True)
    context_before = models.TextField()
    original_word = models.CharField(max_length=100, blank=True, null=True)
    context_after = models.TextField()
    votes = ArrayField(models.CharField(max_length=10, blank=True, null=True), size=2)
    is_color = models.BooleanField(default=False)
    to_check = models.BooleanField(default=True)
    case = models.ForeignKey('Case', related_name='colorexcerpt')

    def __str__(self):
        return self.context_before + ' ' + self.original_word + ' ' + self.context_after


class APISettings(models.Model):
    """
    Keeping a log of all the offsets/limits used
    If we have multiple users, potentially makes sense to expand
    would need to add APIToken at least, and maybe a URLField for the query used
    If not, maynbe ought to be moved out, maybe written to disk in a file
    """
    limit = models.IntegerField(default=0)
    offset = models.IntegerField(default=0)
    # times ran
    counter = models.IntegerField(default=0)
    date_created = models.DateField(auto_now_add=True)
    related_to = models.IntegerField(null=True)

    @classmethod
    def create_with_update(cls, old_instance):
        instance = cls(counter=old_instance.counter + 1,
                       offset=old_instance.offset + old_instance.limit,
                       limit=old_instance.limit,
                       related_to=old_instance.id)
        instance.save()

    def __str__(self):
        return str(self.limit)
