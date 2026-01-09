# Import necessary libraries.
import re
from src.core.interfaces import Tokenizer
from typing import List

class SimpleTokenizer(Tokenizer):
    """ 
    A simple tokenizer that lowercases text, splits on whitespace, and separates basic punctuation characters from words.

    Attributes:
    - punctuation_pattern (re.Pattern): Regular pattern used to separate punctuation.
    """
    def __init__(self) -> None:
        """ 
        Initialize the SimpleTokenizer class. 
        """
        # Pattern finds punctuation characters and ensures they are seperated by spaces.
        self.punctuation_pattern = re.compile(r'([.,!?;:()\[\]"\'])')

    def separate_punctuation(self, text: str) -> str:
        """ 
        Insert spaces around punctuation so that splitting on whitespace yields punctuatuon as separate tokens.
        @param text (str): Input text.
        @return (str): Text with spaces around punctuation. 
        """
        # Surround punctuation with spaces.
        return self.punctuation_pattern.sub(r' \1 ', text)
    
    def split_whitespace(self, text: str) -> List[str]:
        """ 
        Split text on whitespace and filter out empty tokens.
        @param text (str): Input text.
        @return (List[str]): List of non-empty tokens.
        """
        return [t for t in text.split() if t != ""]
    
    def tokenize(self, text: str) -> List[str]:
        """ 
        Tokenize the input text using simple rules.
        @param text (str): Input text to tokenize.
        @return (List[str]): List of tokens. 
        """
        if text is None:
            return []
        # Lowercase.
        lowered = text.lower()
        # Separate punctuation.
        separated = self.separate_punctuation(lowered)
        # Split on whitespace.
        tokens = self.split_whitespace(separated)
        return tokens