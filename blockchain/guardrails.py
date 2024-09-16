import json


def process_rule(rule_name, rule_data):
  """
  Process a single rule entry from the data, handling special cases for 'connotation' and 'implicature'.
  """
  rule_text = rule_data['rule']
  substitutions = []

  if rule_name not in ['connotation', 'implicature']:
    aggressive_phrases = rule_data['aggressive']
    neutral_phrases = rule_data['neutral']
    for i in range(len(aggressive_phrases)):
      substitutions.append(f'{aggressive_phrases[i]} -> {neutral_phrases[i]}')
  else:
    for context, context_data in rule_data.items():
      if context != 'rule':
        aggressive_phrases = [f'context = {context}; {x}' for x in context_data['aggressive']]
        neutral_phrases = [f'context = {context}; {x}' for x in context_data['neutral']]
        for i in range(len(aggressive_phrases)):
          substitutions.append(f'{aggressive_phrases[i]} -> {neutral_phrases[i]}')

  return rule_text, substitutions

with open('aggressive.json') as f:
  data = json.load(f)

for rule_name, rule_data in data['rules'].items():
  rule_text, substitutions = process_rule(rule_name, rule_data)
  print(rule_text, substitutions)
