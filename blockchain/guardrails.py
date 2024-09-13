from langchain_community.document_loaders import JSONLoader

"""RULE 1: TONE"""

def load_words(keyword):
  return JSONLoader(file_path='aggressive.json', jq_schema=f'.{keyword}[]').load()

aggressive_words, neutral_words = load_words('aggressive'), load_words('neutral')

template = f"Помечать слова, использующиеся для выражения враждебности или агрессии.\n\
Заменять агрессивные слова на нейтральные слова с эквивалентным значением. \n\
Дан образец агрессивных слов: {[x.page_content for x in aggressive_words]}. \n\
Дан образец нейтральных замен: {[x.page_content for x in neutral_words]}."

print(template)
