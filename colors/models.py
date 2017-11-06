from django.db import models


class Color(models.Model):
    value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.value


class ColorCase(models.Model):
    colors = models.ManyToManyField('Color', related_name='colorcase')
    slug = models.SlugField(blank=True, null=True)
    name = models.TextField(blank=True)
    name_abbreviation = models.CharField(max_length=255, blank=True)
    decision_date = models.DateField(null=True, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.slug


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
