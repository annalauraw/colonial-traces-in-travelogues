import json

with open('data/glamhack23_reiseberichte_nagezh_textseiten.json', mode='rt', encoding='utf-8') as all_docs_file:

    all_documents_object = json.loads(all_docs_file.read())

# split JSON into one file per title
records = all_documents_object['records']

# one JSON file per title
for record in records:
    with open('data/onetitleperfile/text_and_metadata/{oai_id}.json'.format(oai_id=record['_id']), mode='wt', encoding='utf-8') as titlefile:
        titlefile.write(json.dumps(record, ensure_ascii=False))

# one text file per title
for record in records:
    raw_text = "\n".join([page['page_text'] for page in record['text_links']])
    # list_of_page_texts = [page['page_text'] for page in record['text_links']]
    # for page_text in list_of_page_texts:
    #     print(page_text)
    with open('data/onetitleperfile/rawtext/{oai_id}.txt'.format(oai_id=record['_id']), mode='wt', encoding='utf-8') as titlefile:
        titlefile.write(record["doi"])
        titlefile.write("\n\n")
        titlefile.write(raw_text)