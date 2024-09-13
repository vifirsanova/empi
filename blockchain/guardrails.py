import json

with open('aggressive.json') as f:
  data = json.load(f)

# Parse the JSON and structure it into required string format
parsed_strings = []

for rule, details in data["rules"].items():
  aggressive_samples = details.get("aggressive", [])
  neutral_samples = details.get("neutral", [])

  if isinstance(aggressive_samples, list) and isinstance(neutral_samples, list):
    for aggressive, neutral in zip(aggressive_samples, neutral_samples):
      parsed_strings.append(f"rule: {rule}; aggressive: {aggressive}; neutral: {neutral}")

  # Special handling for sub-categories like "professional", "descriptive", "personal" under "connotation" and "implicature"
  for subcategory, subdetails in details.items():
    if isinstance(subdetails, dict):
      aggressive_samples = subdetails.get("aggressive", [])
      neutral_samples = subdetails.get("neutral", [])

      for aggressive, neutral in zip(aggressive_samples, neutral_samples):
        parsed_strings.append(f"rule: {rule} ({subcategory}); aggressive: {aggressive}; neutral: {neutral}")

print(parsed_strings)