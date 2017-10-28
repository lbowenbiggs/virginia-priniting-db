from VirginiaPrinting.models import NewspaperCitation, NewspaperHistory, Biography, ImprintRecord

# Create a Newspaper Citation
nc = NewspaperCitation(title="Abingdon", num_variants=1, pdf_location="Abingdon 01.pdf")
# Save it in the Database
nc.save()
# Create a Newspaper History that references the citation just created
nh = NewspaperHistory(pdf_location="Abingdon 01", newspaper_citation=nc)
nh.save()

b = Biography(name="Adams", pdf_location="001 Adams 0.pdf")
b.save()

ir = ImprintRecord(year=1790, sequence_number=1, short_title="Example Imprint Record", pdf_location="textfile.txt")
ir.save()
