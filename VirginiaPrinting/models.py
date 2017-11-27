from django.db import models


# Expanded Models
class Biography(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    formal_name = models.CharField(max_length=50, blank=True)
    function = models.CharField(max_length=200, default="Unknown", blank=True)
    locales = models.CharField(max_length=200, default="Virginia", blank=True)
    precis = models.TextField(blank=True)
    first_date = models.IntegerField(blank=True)
    last_date = models.IntegerField(blank=True)

    associates = models.ManyToManyField("self", blank=True)

    notes = models.TextField(blank=True)
    pdf_location = models.FilePathField(path="~/PycharmProjects/VPDB/static/biographies", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "biographies"


class ImprintRecord(models.Model):
    imprint_number = models.DecimalField(primary_key=True, max_digits=7, decimal_places=3)
    year = models.IntegerField()
    sequence_number = models.IntegerField()
    short_title = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200, blank=True)
    title = models.TextField(blank=True)
    place_issued = models.CharField(max_length=200, default="Virginia", blank=True)
    issuing_press = models.CharField(max_length=200, default="Uncertain", blank=True)
    description = models.CharField(max_length=200, default="Unrecorded", blank=True)

    associates = models.ManyToManyField(Biography, blank=True)

    notes = models.TextField(blank=True)
    pdf_location = models.FilePathField(path="static/imprints", blank=True)

    def __str__(self):
        return str(self.imprint_number) + ": " + self.short_title


class NewspaperHistory(models.Model):
    lineage_number = models.CharField(max_length=200)
    group_title = models.CharField(max_length=200, blank=True)

    notes = models.TextField(blank=True)
    pdf_location = models.FilePathField(path="~/PycharmProjects/VPDB/static/journal_histories", blank=True)

    def __str__(self):
        return self.group_title

    class Meta:
        verbose_name_plural = "newspaper histories"


class NewspaperCitation(models.Model):
    variant_number = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True)
    start_date = models.CharField(max_length=200, blank=True)
    end_date = models.CharField(max_length=200, blank=True)
    frequency = models.CharField(max_length=200, blank=True)
    proprietors = models.CharField(max_length=200, default="Unknown", blank=True)

    lineage = models.ForeignKey(NewspaperHistory, blank=True, null=True)
    associates = models.ManyToManyField(Biography, blank=True)

    notes = models.TextField(blank=True)
    pdf_location=models.FilePathField(path="~/PycharmProjects/VPDB/static/journal_citations", blank=True)

    def __str__(self):
        return self.title
