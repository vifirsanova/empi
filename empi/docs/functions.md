Contents:

- [Tokenizer](https://github.com/vifirsanova/empi/blob/main/docs/functions.md#tokenizer)
- Search
  
# Tokenizer

Tokenizer class for pre-processing. The class provides methods for text normalizing text, cleaning text using regular expressions, converting text to lowercase, segmenting text based on different settings, and tokenizing text.

## Initialization

```python
Tokenizer(normalization_type='NFC', pattern=None, lower=True, segmentation_type='subword')
```

**Parameters**

- `normalization_type` (str): The normalization form compatible with unicodedata.normalize().

    - Example: `normalization_type='NFC'` normalizes the input text using the Normalization Form C method.

- `pattern` (str): The regular expression pattern for cleaning.

    - Example: `pattern='[^\w\s]'` cleans anything that's not a digit, letter, or whitespace.

- `lower` (bool): Convert the input text to lowercase.

    - Options: `lower=True` converts the input text to lowercase; `lower=False` does not change the input text.

- `segmentation_type` (Union[str, int]): The segmentation setting.

    - Options:
        - `segmentation_type='char'` enables character-based segmentation.
        - `segmentation_type='word'` enables word-based segmentation.
        - `segmentation_type=n` (int) enables n-gram segmentation.
        - `segmentation_type='subword'` enables byte-pair encoding (BPE) subword segmentation.
## Methods

**`normalize(text: str)`** -> str

Normalizes the input text using the method specified in `self.normalization_type`.

- Parameters:
    - `text (str)`: The input text to be normalized.
    - Returns: The normalized text.
 
  
**`clean(text: str)`** -> str

Cleans the input text using a regular expression pattern specified in `self.pattern`.

- Parameters:
    - `text (str)`: The input text to be cleaned.
    - Returns: The cleaned text.
        
**`to_lower(text: str)`** -> str

Converts the input text to lowercase if `self.lower` is `True`.

- Parameters:
    - `text (str)`: The input text to be converted to lowercas.
    - Returns: The lowecase text.

**`segmentation(text: str)`** -> List[str]

Segments the input text based on the setting specified in `self.segmentation_type`.

- Parameters:
    - `text (str)`: The input text to be segmented.
    - Returns: A list of segments based on the segmentation setting.

**`tokenize(text: str)`** -> List[str]

Tokenizes the input text.

- Parameters:
    - `text (str)`: The input text to be tokenized.
    - Returns: A list of tokens.

## Example

```python
tokenizer = Tokenizer(segmentation_type='word', lower=False)
text = "Что означает аббревиатура РАС?"
tokens = tokenizer.tokenize(text)
print(tokens)
```

This example initializes a **`Tokenizer`** instance with specified parameters, tokenizes the input text, and prints the resulting tokens.

```
['Что', 'означает', 'аббревиатура', 'РАС', '?']
```

# Search

Search class for graph-based search.

This class facilitates two scenarios:

1. Data Encryption:

- Search for personal data indications in the knowledge base to encrypt them
- Return the original text with encrypted data

2. Information Extraction for RAG:

- Search the graph for relevant information and extract it
- Use the extracted data to condition LLM

## Methods

### graph_search(data: dict, query: str) -> set

Recursively search for matches (query) in the graph (data). The function traverses three dimensions of the graph: searches for exact matches or presence of the search query within the sequence.
        
Args:

- data (dict): The graph data to be searched.
- query (str): The search query.

Returns:

- set: The path of matched nodes.

## Example

```
for test_query in ['номер телефона', 'iphone']:
  print(f'Search results for <{test_query}>')
  print(Search().graph_search(data, test_query))

Search results for <номер телефона>
{'зашифровано'}

Search results for <iphone>
{'технология автоматического воспроизведения текста, например, функция “прямая речь” в iphone'}
```
                
