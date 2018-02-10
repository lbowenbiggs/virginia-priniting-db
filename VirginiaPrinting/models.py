from django.db import models
from django.urls import reverse

# Generic Model used to hold Search Results
class GenericSearchResult():
    score = models.DecimalField()
    title = models.CharField(max_length=200)
    excerpt = models.TextField(blank=True)
    link = models.URLField()
    record_type = models.Model

    def __init__(self, record, score):
        if isinstance(record, Biography):
            self.title = record.name
            self.excerpt = record.precis
            self.link = record.get_absolute_url()
            self.record_type = "Biography"
        elif isinstance(record, ImprintRecord):
            self.title = record.short_title
            self.excerpt = record.title
            self.link = record.get_absolute_url()
            self.record_type = "Imprint Record"
        elif isinstance(record, NewspaperCitation):
            self.title = record.title
            if hasattr(record, '_lineage_cache'):
                self.excerpt = "Member of " + record.lineage.group_title + " lineage. Published from " + record.start_date + " to " + record.end_date
            else:
                self.excerpt = "Not a member of any lineage. Published from " + record.start_date + " to " + record.end_date
            self.link = record.get_absolute_url()
            self.record_type = "Newspaper Citation"
        elif isinstance(record, NewspaperHistory):
            self.title = record.group_title
            self.excerpt = record.notes[:200] + "..."
            self.link = record.get_absolute_url()
            self.record_type = "Newspaper Lineage"

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

    def get_absolute_url(self):
        return reverse('VPDB:bio_detail', args=[self.id])

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

    def get_absolute_url(self):
        return reverse('VPDB:imprint_detail', args=[str(self.imprint_number)])

    def __str__(self):
        return str(self.imprint_number) + ": " + self.short_title


class NewspaperHistory(models.Model):
    lineage_number = models.CharField(max_length=200)
    group_title = models.CharField(max_length=200, blank=True)

    notes = models.TextField(blank=True)
    pdf_location = models.FilePathField(path="~/PycharmProjects/VPDB/static/journal_histories", blank=True)

    def get_absolute_url(self):
        return reverse('VPDB:news_hist_detail', args=[str(self.pk)])

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

    def get_absolute_url(self):
        return reverse('VPDB:news_cite_detail', args=[str(self.pk)])

    def __str__(self):
        return self.title