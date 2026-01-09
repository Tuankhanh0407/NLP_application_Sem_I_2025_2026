# Import necessary libraries.
from src.core.interfaces import Vectorizer, Tokenizer
from typing import Dict, List

class CountVectorizer(Vectorizer):
    """ 
    A simple count vectorizer that builds a vocabulary from a corpus and transforms documents into count vectors.

    Attributes:
    - tokenizer (Tokenizer): Tokenizer instance used to split documents into tokens.
    - vocab (Dict[str, int]): Mapping from token to index.
    """
    def __init__(self, tokenizer: Tokenizer) -> None:
        """ 
        Initialize the CountVectorizer class. 
        """
        self.tokenizer = tokenizer
        self.vocab: Dict[str, int] = {}

    def fit(self, corpus: List[str]) -> None:
        """ 
        Learn the vocabulary from the provided corpus.
        @param corpus (List[str]): List of documents to learn vocabulary from. 
        """
        unique_tokens = set()
        for doc in corpus:
            tokens = self.tokenizer.tokenize(doc)
            unique_tokens.update(tokens)
        # Sort tokens for deterministic ordering.
        sorted_tokens = sorted(unique_tokens)
        self.vocab = {token: idx for idx, token in enumerate(sorted_tokens)}

    def transform(self, documents: List[str]) -> List[List[int]]:
        """ 
        Transform documents into count vectors using learned vocabulary.
        @param documents (List[str]): Documents to transform.
        @return (List[List[int]]): Document-term count matrix. 
        """
        if not self.vocab:
            raise ValueError("Vocabulary is empty. Call fit() before transform().")
        vocab_size = len(self.vocab)
        result = []
        for doc in documents:
            vector = [0] * vocab_size
            tokens = self.tokenizer.tokenize(doc)
            for t in tokens:
                if t in self.vocab:
                    vector[self.vocab[t]] += 1
            result.append(vector)
        return result
    
    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """ 
        Convenience method to fit and transform the same corpus.
        @param corpus (List[str]): Corpus to fit transform.
        @return (List[List[int]]): Document-term count matrix for the corpus. 
        """
        self.fit(corpus)
        return self.transform(corpus)