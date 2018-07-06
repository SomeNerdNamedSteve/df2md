import json
from os import listdir
from os.path import isfile, join
from pprint import pprint

path = os.getcwd() + '\\chatbot-intents'

intent_files = ["%s\\%s" % (path, f) for f in listdir(path) if isfile("%s\\%s" % (path, f))]

file_count = 0

intent_info = []

while file_count != len(intent_files):
    intent_json = intent_files[file_count]
    utterance_json = intent_files[file_count+1]

    # read from the intent file
    with open(intent_json, encoding="utf8") as f:
        json_info = json.loads(f.read())
        intent_name = json_info['name']

        messages = json_info['responses'][0]['messages']

        text_responses = [message['speech'] for message in messages if message['type'] == 0]

    # read from utterance file
    with open(utterance_json, encoding="utf8") as f:
        utterance_info = json.loads(f.read())
        utterances = [point['data'][0]['text'] for point in utterance_info]
    
    intent_info.append({
        'intent_name': intent_name,
        'responses': text_responses,
        'utterances': utterances
    })

    file_count += 2

with open('intent.md', 'w+', encoding='utf8') as f:
    for intent in intent_info:
        utterances = ['- {}'.format(utterance) for utterance in intent['utterances']]
        responses = ['- {}'.format(response) for response in intent['responses'] if type(response) == type(str())]
        f.write('# Intent: {}\n'.format(intent['intent_name']))
        f.write('## Utterances:\n{}\n'.format('\n'.join(utterances)))
        f.write('\n\n')
        f.write('## Responses:\n{}\n'.format('\n'.join(responses)))
        f.write('\n\n')
