class Tokenizer():
  """
  Токенизатор:
  - нормализация кодировок по методу NFC (True, False)
  - чистка по заданному паттерну с помощью RegEx (паттерн вида r'...')
  - приведение к нижнему регистру (True, False)
  - посимвольная, пословная сегментация, n-граммная сегментация или BPE (опции: symbol (str), word (str), n (int), subword (str))
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
    # посимвольная
    if setting == 'symbol':
      return [*text]

    # пословная
    elif setting == 'word':
      return nltk.word_tokenize(text)

    # n-граммная
    elif isinstance(setting, int):
      temp = nltk.word_tokenize(text)
      ngrams = []
      for i in range(len(temp) - setting+1):
        ngrams.append(' '.join(temp[i:i + setting]))
      return ngrams

    # подсловная
    else:
      tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-uncased")
      return tokenizer.tokenize(text)
