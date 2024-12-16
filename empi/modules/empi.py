import re
import unicodedata

class Search:
    """
    Search class for graph-based search.
    """
    def __init__(self):
        self.path = set()

    def graph_search(self, data, query):
        """
        Recursively search for matches (query) in the graph (data).

        The function traverses three dimensions of the graph:
        searches for exact matches or presence of the search query within the sequence.
        
        Args:
          data (dict): The graph data to be searched.
          query (str): The search query.

        Returns: a set containing the path of matched nodes.
        """
        for k in data:
            if query in k.split() or query == k:
                self.path.add(data[k]) if not isinstance(data[k], dict) else self.path.add(str(data[k]))
            if isinstance(data[k], dict):
                self.graph_search(data=data[k], query=query)
            else:
                if isinstance(data[k], str):
                    if query in data[k].split() or query == data[k]:
                        self.path.add(data[k]) if not isinstance(data[k], dict) else self.path.add(str(data[k]))
                else:
                    for elem in data[k]:
                        if query in elem.split() or query == elem:
                            self.path.add(data[k]) if not isinstance(data[k], dict) else self.path.add(str(data[k]))
        return self.path

class Tokenizer:
    """
    Tokenizer class for pre-processing.

    The class provides methods for text normalizing text, cleaning text using regular expressions,
    converting text to lowercase, segmenting text based on different settings, and tokenizing text.
    """
    def __init__(self, normalization_type='NFC', pattern=None, lower=True, segmentation_type='subword'):
        """
        Args:  
            normalization_type(str): The normalization form compatible to unicodedata.normalize().
            Example:
                normalization_type='NFC' normalizes the input text using the Normalization Form C method.

            pattern (str): The regular expression pattern for cleaning. 
            Example:
                pattern='[^\w\s]' cleans anything that's not a digit, letter or whitespace

            lower(Bool): Convert the input text to lowercase.
            Options:
                lower=True converts the input text to lowercase;
                lower=False does not change the input text.

            setting (Union[str, int]): The segmentation setting. 
            Options:
                setting='char' (str) enables charater-based segmentation;
                setting='word' (str) enables word-based segmentation;
                setting=n (int) enables n-gram segmentation;
                setting='subword' (str) enables byte-pair encoding (BPE) subword segmentation.
        """
        self.normalization_type = normalization_type
        self.pattern = pattern
        self.lower = lower
        self.setting = segmentation_type
        self.subwords = {'презид', 'США', 'ко', 'х', 'ь', 'ы,</w>', 'ства</w>', 'по', 'a', 'про', 'из', 'ств', 'И', 'Бара', 'A', 'S', 'З', 'ать</w>', 'G', 'ент', 'го</w>', 'ка', 'х</w>', 'с', 'не', 'у', 'Б', 'r', '(', 'ий</w>', '5', 'М', 'o', 'су', 'р', 'ност', 'g', 'энерг', 'энергет', '2', 'се', 'ав', 'з', 'пер', 'e', 'Т', 'американ', ',', 'н', 'V', 'я', 'ам', 'м', 'м</w>', 'со', ':', 'n', 'ин', 'президента</w>', '1', 'ие</w>', 'IT-', 'ор', 'т', 'А', 'ш', 'кото', 'ения</w>', 'm', '0', '%', 'ре', 'бы', 'во', 'ро', 'о', 'ю</w>', 'Обама</w>', 't', 'й</w>', 'а</w>', 'вы', 'R', 'д', 'h', 'к</w>', 'с</w>', 'пол', '«', 'их</w>', 'F', 'W', 'по</w>', 'p', 'пре', 'те', 'пр', 'P', 'то', 'I', '»</w>', 'ны', 'П', 'ци', 'п', 'c', 'нол', '</w>', 'l', ')', 'ел', 'ис', ',</w>', 'пред', 'США</w>', 'до', 'ог', 'ал', 'ер', 'Ч', 'К', 'ц', 'ь</w>', 'M', 'ара', 'я</w>', 'итель', 'к', 'ы</w>', 'ерикан', 'ф', 'Ш', 's', 'Г', 'го', '8', 'и', 'v', 'за', 'президент', 'в</w>', 'иче', 'ы', 'об', '-', 'ит', 'на</w>', 'ый</w>', 'ск', 'd', 'i', 'f', 'ч', 'ж', 'но', 'Обам', '—</w>', 'ных</w>', 'л', 'ст', 'энер', 'ич', 'й', 'г', 'ции</w>', 'В', 'ет', 'ил', 'од', 'ик', 'u', 'ть', 'е', 'ат', 'прав', 'ван', 'Э', 'то</w>', 'Y', 'щ', 'сл', 'э', 'k', 'ист', 'y', 'в', 'H', 'у</w>', 'O', 'е</w>', 'и</w>', 'пере', 'уж', 'T', 'С', 'w', 'от', 'b', 'Д', 'C', 'ть</w>', 'E', 'ид', 'б', 'ра', 'Н', 'ель', 'ия</w>', 'ю', 'ет</w>', 'а', 'сам', 'технолог', 'ен', 'на', 'ной</w>', 'пост', 'ан'}
        
    def normalize(self, text):
        """
        The input text normalization with the method specified in self.normalization_type.
        """
        return unicodedata.normalize(self.normalization_type, text)

    def clean(self, text):
        """
        Cleans the input text using a regular expression pattern specified in self.pattern.
        """
        return re.sub(self.pattern, '', text)

    def to_lower(self, text):
        """
        Converts the input text to lowercase  if self.lower is True.
        """
        return text.lower()

    def segmentation(self, text):
        """
        Segments the input text based on the setting specified in self.segmentation_type.
        """
        # Adds a whitespace before punctuation for fine-grained segmentation 
        text = re.sub('([.,!?()])', r' \1 ', text)
        text = re.sub('\s{2,}', ' ', text)

        # Charater-based segmentation
        if self.setting == 'char':
            return list(text)

        # Word-based segmentation
        elif self.setting == 'word':
            return text.split()

        # N-gram segmentation
        elif isinstance(self.setting, int):
            ngrams = []
            text = text.split()
            for i in range(len(text) - self.setting + 1):
                ngrams.append(' '.join(text[i:i + self.setting]))
            return ngrams

        # Byte-pair encoding (BPE) subword segmentation using pre-trained subwords stored in self.subwords
        else:
          tokens = []
          while text:
              match = False
              for subword in sorted(self.subwords, key=len, reverse=True):
                  if text.startswith(subword):
                      tokens.append(subword)
                      text = text[len(subword):]
                      match = True
                      break
              if not match:
                  tokens.append(text[0])
                  text = text[1:]
          return tokens

    def tokenize(self, text):
      """
      Tokenize the input text.

      Args:
        text (str): The input text to be tokenized.
      
      Returns: list of tokens.
      """
      text = self.normalize(text)
      if self.pattern is not None:
        text = self.clean(text)
      if self.lower == True:
        text = self.to_lower(text)
      tokens = self.segmentation(text)
      return tokens
