# Tokenizer
    Methods:
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

        tokenize(text: str, pattern: str = None, setting: Union[str, int]) -> List[str]:
            Tokenize the input text.
            Args:
                text (str): The input text to be tokenized.
                pattern (str, optional): The regular expression pattern for cleaning. Default is None.
                setting (Union[str, int]): The segmentation setting. Refer to segmentation method for details.
            Returns:
                List[str]: The list of tokens.
