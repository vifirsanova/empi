# Tokenizer

Tokenizer class for pre-processing.

The class provides methods for text normalizing text, cleaning text using regular expressions, converting text to lowercase, segmenting text based on different settings, and tokenizing text.

## Methods:

normalize(text: str) -> str:
Normalize the input text using the NFC (Normalization Form C) method.
Args:
    text (str): The input text to be normalized.
Returns:
    str: The normalized text.

clean(text: str, pattern: str) -> str:
Clean the input text using a specified regular expression pattern.
Args:
    text (str): The input text to be cleaned.
    pattern (str): The regular expression pattern for cleaning.
Returns:
    str: The cleaned text.

to_lower(text: str) -> str:
Convert the input text to lowercase.
Args:
    text (str): The input text to be converted to lowercase.
Returns:
    str: The text converted to lowercase.

segmentation(text: str, setting: Union[str, int]) -> List[str]:
Segment the input text based on the specified setting.
Args:
    text (str): The input text to be segmented.
    setting (Union[str, int]): The segmentation setting. Possible values are:
        - 'symbol': Segment the text into individual characters.
        - 'word': Segment the text into words.
        - n (int): Segment the text into n-grams, where n is an integer.
        - 'subword': Segment the text into subwords using a pretrained tokenizer.
Returns:
    List[str]: The segmented text as a list of strings.

tokenize(text: str, setting: Union[str, int], cleaning_pattern: str = None, lower: Bool = True) -> List[str]:
Tokenize the input text.
Args:
    text (str): The input text to be tokenized.
    cleaning_pattern (str, optional): The regular expression pattern for cleaning. Default is None.
    setting (Union[str, int]): The segmentation setting. Refer to segmentation method for details.
    lower (Bool): Enables (True) or disables (False) converting to lowercase; default is True 
Returns:
    List[str]: The list of tokens.

# Search

    This class facilitates two scenarios:
    1. Data Encryption: Searching for data vulnerable to hackers using a knowledge graph.
       - Searches for indications of user's personal data in the knowledge base and encrypts them.
       - Returns the original text with encrypted data.
    2. Information Extraction for Generating Informative Responses:
       - Searches the graph for relevant information and extracts text.
       - The extracted text can be used for conditioned generation using LLM.

    Attributes:
        path (set): A set to store the path of matched nodes during the graph search.

    Methods:
        graph_search(data: dict, query: str) -> set:
            Recursively search for matches (query) in the graph (data).
            This function traverses three dimensions of the graph:
            - Searches for exact matches or presence of the search query within the sequence.
            Args:
                data (dict): The graph data to be searched.
                query (str): The search query.
            Returns:
                set: A set containing the path of matched nodes.
