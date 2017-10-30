from django.db import models


# These models correspond to the four types of documents Professor Rawson gave us
class NewspaperCitation(models.Model):
    title = models.CharField(max_length=200)
    num_variants = models.IntegerField()
    pdf_location=models.FilePathField(path="~/PycharmProjects/VPDB/static/journal_citations")

    def __str__(self):
        return "Citation: " + self.title


class NewspaperHistory(models.Model):
    pdf_location = models.FilePathField(path="~/PycharmProjects/VPDB/static/journal_histories")
    newspaper_citation = models.ForeignKey(NewspaperCitation, on_delete=models.CASCADE)

    def __str__(self):
        return "History: " + self.newspaper_citation.title


class Biography(models.Model):
    name = models.CharField(max_length=200)
    pdf_location = models.FilePathField(path="~/PycharmProjects/VPDB/static/biographies")

    def __str__(self):
        return self.name


class ImprintRecord(models.Model):
    year = models.IntegerField()
    sequence_number = models.IntegerField()
    short_title = models.CharField(max_length=200)
    pdf_location = models.FilePathField(path="~/PycharmProjects/VPDB/static/imprints")

    def __str__(self):
        return self.imprint_number() + ": " + self.short_title

    def imprint_number(self):
        return str(self.year) + "." + str(self.sequence_number)