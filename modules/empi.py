class Search():
  """
  Поиск по графу для реализации двух сценариев
  1. Шифрование данных: поиск данных, уязвимых для хакеров, с помощью графа знаний
  - ищет указание на персональные данные пользователя с помощью поиска по базе знаний и шифрует их
  - возвращает исходный текст с зашифрованными данными
  2. Извлечение информации для генерации информативного ответа
  - ищет по графу релевантную информацию и извлекает текст
  - текст можно использовать для обусловленной генерации с помощью LLM
  """
  def __init__(self):
    self.path = set()

  def graph_search(self, data, query):
    """
    Рекурсивная функция для поиска совпадений (query) по графу (data):
    - функция проходит по трем измерениям графа
    - ищет точные совпадения или наличие поискового запроса внутри последовательности
    """
    for k in data:
      if query in k.split() or query == k:
        self.path.add(data[k]) if isinstance(data[k], dict) == False else self.path.add(str(data[k]))
      if isinstance(data[k], dict):
        self.graph_search(data=data[k], query=query)
      else:
        if isinstance(data[k], str):
          if query in data[k].split() or query == data[k]:
            self.path.add(data[k]) if isinstance(data[k], dict) == False else self.path.add(str(data[k]))
        else:
          for elem in data[k]:
            if query in elem.split() or query == elem:
              self.path.add(data[k]) if isinstance(data[k], dict) == False else self.path.add(str(data[k]))
    return self.path

class Tokenizer:
    """
    Класс "Токенизатор":
    normalize(text) - нормализация кодировок по методу NFC, text (str)
    clean(text, pattern) - чистка по заданному паттерну с помощью RegEx, text(str), pattern (паттерн вида r'...')
    to_lower(text) - приведение к нижнему регистру, text (str)
    segmentation(text, setting) - сегментация, text (str), setting ("symbol" для посимвольной, "word" для пословной, n (int) для n-граммной, "subword" для подсловной)
    """
    def normalize(self, text):
        """
        Нормализация текста по методу NFC.
        """
        return unicodedata.normalize('NFC', text)

    def clean(self, text, pattern):
        """
        Очистка текста по заданному паттерну с помощью RegEx.
        """
        return re.sub(pattern, '', text)

    def to_lower(self, text):
        """
        Приведение текста к нижнему регистру.
        """
        return text.lower()

    def segmentation(self, text, setting):
        """
        Сегментация текста.
        """
        text = re.sub('([.,!?()])', r' \1 ', text)
        text = re.sub('\s{2,}', ' ', text)

        # посимвольная
        if setting == 'symbol':
            return list(text)

        # пословная
        elif setting == 'word':
            return text.split()

        # n-граммная
        elif isinstance(setting, int):
            ngrams = []
            text = text.split()
            for i in range(len(text) - setting + 1):
                ngrams.append(' '.join(text[i:i + setting]))
            return ngrams

        # подсловная
        else:
            tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-uncased")
            return tokenizer.tokenize(text)

  def tokenize(self, text, patttern=None, setting):
    text = self.normalize(text)
    if pattern is not None:
      text = self.clean(text, pattern)
    text = self.to_lower(text)
    tokens = self.segmentation(text, setting)
    return tokens
