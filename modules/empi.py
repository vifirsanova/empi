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

        # Byte-pair encoding (BPE) subword segmentation using HuggingFace Transformers
        else:
            tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-uncased")
            return tokenizer.tokenize(text)
          
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
