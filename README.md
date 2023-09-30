# Identifying colonial traces in early modern travelogues (GLAMhack23 challenge)

With the help of @Ibrahim-Halil-Kuray and @guenterh

This repository contains scripts for processing the dataset [Early modern travel literature](https://opendata.swiss/en/dataset/gedruckte-reiseberichte-des-16-bis-19-jh) with OCR text from early modern prints provided by Zentralbibliothek Zürich.

split_titles.py takes the [large JSON file](https://opendata.swiss/en/dataset/gedruckte-reiseberichte-des-16-bis-19-jh/resource/21d83a08-363c-442f-8fee-b87af8dc76e8) containing all the titles, splits it, and saves the JSON for one title to a new file. 

get_entities.py processes the JSON title files and enriches them with Named entities suggested by Named Entity Recognition tool [SBB-NER-Tagger](https://github.com/qurator-spk/sbb_ner). SBB-NER-Tagger can be locally installed and run - get_entities.py makes queries against its API. data/example_title_with_entities_per_page.json contains some example content to illustrate the document structure.

The resulting data, i.e. Named Entities found per text page, is the basis for this [prototypical frontend](https://github.com/Ibrahim-Halil-Kuray/Glam-Hack-2023) which makes it possible to discover the text pages of a printed travelogue side by side with the entities suggested per page.

For a reference of the entity categories used, please see the [BERT documentation](https://huggingface.co/dslim/bert-base-NER).

The next step could be to link the identified entities to Wikidata objects using [SBB-NED](https://github.com/qurator-spk/sbb_ned).
