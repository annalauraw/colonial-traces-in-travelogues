import json
import os
import requests

# iterate through text files and get entities suggested per text file
# assign directory
directory = 'data/onetitleperfile/text_and_metadata'
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    print(filename)
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        # open the file
        with open(f, mode='rt', encoding='utf-8') as jsonfile:
            # read the text into a variable (is the whole text too big?)
            jsonfile_handle = jsonfile.read()
            file_obj = json.loads(jsonfile_handle)
            # make a copy of the file obj for the target file
            file_obj_copy = file_obj.copy()

        # iterate through the text pages
        for page in file_obj['text_links']:
            # get page label - needed for addressing page objects in the target file
            page_label = page['page_label']
            # get page text
            page_text = page['page_text']
            # make a query to the sbb_ner API
            payload = { 'text' : page_text }
            headers = { 'Content-Type': 'application/json' }
            response = requests.post(
                url='http://localhost:5000/ner/1',
                # ensure_ascii=False triggers error in sbb_ner API :(
                data=json.dumps(payload),
                headers=headers
            )
            all_entities_str = response.text
            all_entities_str_json = '{{ "entities": {entities} }}'.format(entities=all_entities_str)
            all_entities_obj = json.loads(all_entities_str_json)
            # filter out entities with type O
            # for the entity categories, see https://huggingface.co/dslim/bert-base-NER
            page_entities = [entity for entity_list in all_entities_obj["entities"] for entity in entity_list if entity['prediction'] != 'O']
            # write the page entities to the target file object
            # find the page object
            page_matches = [page for page in file_obj_copy['text_links'] if page['page_label'] == page_label]
            # append entities to the page
            page_matches[0]['entities'] = page_entities
            # print(page_matches[0])
            # print(page_entities)

        # write file copy with entities to new JSON file
        with open('data/onetitleperfile/json_with_entities/{filename}'.format(filename=filename), mode='wt', encoding='utf-8') as newfile:
            newfile.write(json.dumps(file_obj_copy, ensure_ascii=False))

# To Do


