URL to Webpage Mapping
======================

summary of `urls.py`; more readable

URLs are given after beta.indexvirginiaprinting.org/. Text in <brackets> indicates a variable.

| Name | URL | Example | View Function Used | Template Used |
|------|-----|---------|--------------------|---------------|
| index | VPDB | -- | `index()` | `index.html` |
| news_cites_index | VPDB/news_cites | -- | `NewsCitesListView.as_view()` | `newspaper_citation_index.html` |
| news_cite_detail | VPDB/news_cite/<citation_id> | VPDB/news_cite/1 | `NewsCiteDetailView.as_view(citation_id)` | `newspaper_citation.html` |
| news_hists_index | VPDB/news_hists | -- | `NewsHistsListView.as_view()` | `newspaper_history_index.html` |
| news_hist_detail | VPDB/news_hist/<history_id> | VPDB/news_hist/1 | `NewsHistDetailView.as_view(history_id)` | `newspaper_history.html`
| bios_index | VPDB/bios | -- | `BiosListView.as_view()` | `biography_index.html` |
| bio_detail | VPDB/bio/<bio_id> | VPDB/bio/1 | `BioDetailView.as_view(bio_id)` | `biography.html` |
| imprints_index | VPDB/imprints | -- | `ImprintsListView.as_view()` | `imprint_record_index.html` |
| imprint_detail | VPDB/imprint/<imprint_id> | VPDB/imprint/1798.001 | `ImprintDetailView.as_view(imprint_id)` | `imprint_record.html` |
