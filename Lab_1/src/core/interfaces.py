# Import necessary libraries.
from abc import ABC, abstractmethod
from typing import List

class Tokenizer(ABC):
    """ 
    Abstract interface for tokenizers. 
    """
    @abstractmethod
    def tokenize(self, text: str) -> List[str]:
        """ 
        Tokenize input text into a list of tokens.
        @param text (str): Input text to tokenize.
        @return (List[str]): List of tokens extracted from the text. 
        """
        raise NotImplementedError
    
class Vectorizer(ABC):
    """ 
    Abstract interface for vectorizers.
    """
    @abstractmethod
    def fit(self, corpus: List[str]) -> None:
        """ 
        Learn vocabulary from corpus.
        @param corpus (List[str]): List of documents to learn vocabulary from. 
        """
        raise NotImplementedError
    
    @abstractmethod
    def transform(self, documents: List[str]) -> List[List[int]]:
        """ 
        Transform documents into vectors using learned vocabulary.
        @param documents (List[str]): Documents to transform.
        @return (List[List[int]]): Document-term count matrix. 
        """
        raise NotImplementedError
    
    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """ 
        Convenience method to fit and transform the same corpus.
        @param corpus (List[str]): Corpus to fit and transform.
        @return (List[List[int]]): Document-term count matrix for the corpus. 
        """
        self.fit(corpus)
        return self.transform(corpus)