class Tokenizer():
  """
  Класс "Токенизатор":
  normalize(text) - нормализация кодировок по методу NFC, text (str)
  clean(text, pattern) - чистка по заданному паттерну с помощью RegEx, text(str), pattern (паттерн вида r'...')
  to_lower(text) - приведение к нижнему регистру, text (str)
  segmentation(text, setting) - сегментация, text (str), setting ("symbol" для посимвольной, "word" для пословной, n (int) для n-граммной, "subword" для подсловной)
  """
  def __init__(self):
    pass

  def normalize(self, text):
    return unicodedata.normalize('NFC', text)

  def clean(self, text, pattern):
    return re.sub(pattern, '', text)

  def to_lower(self, text):
    return text.lower()

  def segmentation(self, text, setting):
    text = re.sub('([.,!?()])', r' \1 ', text)
    text = re.sub('\s{2,}', ' ', text)

    # посимвольная
    if setting == 'symbol':
      return [*text]

    # пословная
    elif setting == 'word':
      return text.split()

    # n-граммная
    elif isinstance(setting, int):
      ngrams = []
      text = text.split()
      for i in range(len(text) - setting+1):
        ngrams.append(' '.join(text[i:i + setting]))
      return ngrams

    # подсловная
    else:
      tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-uncased")
      return tokenizer.tokenize(text)
