import json

from langchain_community.llms.llamacpp import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from llama_cpp import Llama

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

system_rule = str()

i=1

for rule_name, rule_data in data['rules'].items():
  rule_text, substitutions = process_rule(rule_name, rule_data)
  system_rule += f'ПРАВИЛО №{i}\n'
  system_rule += f'{rule_text}\n'
  system_rule += 'ОБРАЗЦЫ ЗАМЕН\n'
  system_rule += f'{substitutions}\n\n'
  i += 1

llm = Llama(
      model_path="/home/missvector/Meta-Llama-3-8B-Instruct.Q4_K_M.gguf",
      n_ctx=2048, # context window
)

prompt_template = f"""{system_rule}
Дан образец <Всего лишь 10% участников.>
Определить, какое правило нарушено в текущем образце. Произвести необходимую замену согласно правилу.
"""

print(prompt_template)

output = llm(
  f"Q: {prompt_template} A: ",  # Prompt
  max_tokens=64,  # Generate up to 64 tokens, set to None to generate up to the end of the context window
  stop=["Q:", "\n"],  # Stop generating just before the model would generate a new question
  # echo=True  # Echo the prompt back in the output
)

print(output['choices'][0]['text'])

def build_chain(system_rule):
   """
   Build and execute a Langchain-based chain to process the given data.
   """

   prompt_template = """{system_rule}
   Дан образец <Всего лишь 10% участников.>
   Определить, какое правило нарушено в текущем образце. Произвести необходимую замену согласно правилу.
   """
   prompt = PromptTemplate(template=prompt_template, input_variables=["system_rule"])
   # load LLM
   llm = LlamaCpp(
     model_path="/home/missvector/Meta-Llama-3-8B-Instruct.Q4_K_M.gguf",
     n_ctx=2048,  # context window
   )
   output_parser = StrOutputParser()
   chain = prompt | llm | output_parser
   print(chain)
   response = chain.invoke({"system_rule": system_rule})
   print(response)

build_chain(system_rule)
