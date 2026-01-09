# Import necessary libraries.
import re
from src.core.interfaces import Tokenizer
from typing import List

class RegexTokenizer(Tokenizer):
    """ 
    A tokenizer that uses a single regular expression to extract tokens robustly.
    
    Attributes:
    - token_pattern (re.Pattern): Compiled regular expression pattern for token extraction.
    """
    def __init__(self) -> None:
        """ 
        Initialize the RegexTokenizer class. 
        """
        # Pattern explanation:
        # - [A-Za-z0-9]+(?:'[A-Za-z0-9]+)*: Words and contractions like don't, isn't.
        # - |[^\s\w]: Any single punctuation character (non-space, non-word).
        self.token_pattern = re.compile(r"[A-Za-z0-9]+(?:'[A-Za-z0-9]+)*|[^\s\w]", re.UNICODE)

    def tokenize(self, text: str) -> List[str]:
        """ 
        Tokenize input text using a single regular expression to extract tokens.
        @param text (str): Input text to tokenize.
        @return (List[str]): List of tokens extracted by regular expression. 
        """
        if text is None:
            return []
        # Lowercase for normalization.
        lowered = text.lower()
        tokens = self.token_pattern.findall(lowered)
        return tokens