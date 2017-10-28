from django.db import models


# These models correspond to the four types of documents Professor Rawson gave us
class NewspaperCitation(models.Model):
    title = models.CharField(max_length=200)
    num_variants = models.IntegerField()
    pdf_location=models.FilePathField()


class NewspaperHistory(models.Model):
    pdf_location = models.FilePathField()
    newspaper_citation = models.ForeignKey(NewspaperCitation, on_delete=models.CASCADE)


class Biography(models.Model):
    name = models.CharField(max_length=200)
    pdf_location = models.FilePathField()


class ImprintRecord(models.Model):
    year = models.IntegerField()
    sequence_number = models.IntegerField()
    short_title = models.CharField(max_length=200)
    pdf_location = models.FilePathField()