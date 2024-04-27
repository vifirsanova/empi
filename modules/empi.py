!pip install transformers

from transformers import AutoTokenizer
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
    def normalize(self, text):
        """
        Normalize the input text using the NFC (Normalization Form C) method.
        """
        return unicodedata.normalize('NFC', text)

    def clean(self, text, pattern):
        """
        Clean the input text using a specified regular expression pattern.
        """
        return re.sub(pattern, '', text)

    def to_lower(self, text):
        """
        Convert the input text to lowercase.
        """
        return text.lower()

    def segmentation(self, text, setting):
        """
        Segment the input text based on the specified setting.
        Available settings:
          setting='symbol' enables charater-based segmentation;
          setting='word' enables word-based segmentation;
          setting=n (int) enables n-gram segmentation;
          setting='subword' enables byte-pair encoding (BPE) subword segmentation
        """
        text = re.sub('([.,!?()])', r' \1 ', text)
        text = re.sub('\s{2,}', ' ', text)

        # charater-based segmentation
        if setting == 'symbol':
            return list(text)

        # word-based segmentation
        elif setting == 'word':
            return text.split()

        # n-gram segmentation
        elif isinstance(setting, int):
            ngrams = []
            text = text.split()
            for i in range(len(text) - setting + 1):
                ngrams.append(' '.join(text[i:i + setting]))
            return ngrams

        # byte-pair encoding (BPE) subword segmentation
        else:
            tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-uncased")
            return tokenizer.tokenize(text)
          
    def tokenize(self, text, setting, pattern=None, lower=True):
      """
      Tokenize the input text.

      Args:
        text (str): The input text to be tokenized.
        pattern (str, optional): The regular expression pattern for cleaning. Default is None.
        setting (Union[str, int]): The segmentation setting. Refer to segmentation method for details.
        lower (Bool): Enables (True) or disables (False) converting to lowercase. Default is True.
      
      Returns: list of tokens.
      """
      text = self.normalize(text)
      if pattern is not None:
        text = self.clean(text, pattern)
      if lower == True:
        text = self.to_lower(text)
      tokens = self.segmentation(text, setting)
      return tokens
