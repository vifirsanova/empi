# Tokenizer

Tokenizer class for pre-processing. The class provides methods for text normalizing text, cleaning text using regular expressions, converting text to lowercase, segmenting text based on different settings, and tokenizing text.

## Methods

### normalize(text: str) -> str

Normalize the input text using the NFC (Normalization Form C) method.

Args:

- text (str): The input text to be normalized.

Returns:

- str: The normalized text.
        
### clean(text: str, pattern: str) -> str

Clean the input text using a specified regular expression pattern.

Args:

- text (str): The input text to be cleaned.
- pattern (str): The regular expression pattern for cleaning.

Returns:

- str: The cleaned text.

### to_lower(text: str) -> str

Convert the input text to lowercase.

Args:

- text (str): The input text to be converted to lowercase.

Returns:

- str: The text converted to lowercase.

### segmentation(text: str, setting: Union[str, int]) -> List[str]

Segment the input text based on the specified setting.

Args:

- text (str): The input text to be segmented.
- setting (Union[str, int]): The segmentation setting. Available settings:
    - setting='symbol' enables charater-based segmentation;
    - setting='word' enables word-based segmentation;
    - setting=n (int) enables n-gram segmentation;
    - setting='subword' enables byte-pair encoding (BPE) subword segmentation
  
Returns:
- List[str]: The segmented text as a list of strings.

### tokenize(text: str, setting: Union[str, int], pattern: str = None, lower: Bool = True) -> List[str]

Tokenize the input text.

Args:

- text (str): The input text to be tokenized.
- pattern (str, optional): The regular expression pattern for cleaning. Default is None.
- setting (Union[str, int]): The segmentation setting. Refer to segmentation method for details.
- lower (Bool): Enables (True) or disables (False) converting to lowercase. Default is True.

Returns:

- List[str]: The list of tokens.

## Example

```
Tokenizer().tokenize('This is a sample test for bigram tokenization without cleaning.', setting=2)

['this is',
 'is a',
 'a sample',
 'sample test',
 'test for',
 'for bigram',
 'bigram tokenization',
 'tokenization without',
 'without cleaning',
 'cleaning .']

Tokenizer().tokenize('This # is a sample $%^ test for word based tokenization with cleaning.',
                      pattern=r'[^\w\s]', setting='word')

['this',
 'is',
 'a',
 'sample',
 'test',
 'for',
 'word',
 'based',
 'tokenization',
 'with',
 'cleaning']
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
                
