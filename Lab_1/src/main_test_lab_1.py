# Import necessary libraries.
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.core.dataset_loaders import load_raw_text_data
from src.preprocessing.regex_tokenizer import RegexTokenizer
from src.preprocessing.simple_tokenizer import SimpleTokenizer
from src.representations.count_vectorizer import CountVectorizer
from typing import List

def demo_tokenizers_on_sentences(sentences: List[str]) -> None:
    """ 
    Demonstrate tokenizers on a list of sentences and print outputs.
    @param sentences (List[str]): Sentences to tokenize. 
    """
    simple_tok = SimpleTokenizer()
    regex_tok = RegexTokenizer()
    print("\n--- Tokenizer demo on sample sentences ---")
    for s in sentences:
        print(f"\nOriginal: {s}")
        st = simple_tok.tokenize(s)
        rt = regex_tok.tokenize(s)
        print(f"SimpleTokenizer: {st}")
        print(f"RegexTokenizer: {rt}")

def demo_tokenizers_on_ud_english_ewt_sample(sample_length: int = 500) -> None:
    """ 
    Load UD_English-EWT dataset, take a sample, and tokenize it.
    @param sample_length (int): Number of characters to take from raw dataset for demo. 
    """
    print("\n--- Loading UD_English-EWT dataset... ---")
    raw_text = load_raw_text_data(None)
    if not raw_text:
        print("Warning: Could not download UD_English-EWT dataset. Skipping dataset demo.")
        return
    sample_text = raw_text[:sample_length]
    print("\n--- Tokenizing sample text from UD_English-EWT ---")
    print(f"Original sample (first 100 chars): {sample_text[:100]}...")
    simple_tok = SimpleTokenizer()
    regex_tok = RegexTokenizer()
    simple_tokens = simple_tok.tokenize(sample_text)
    regex_tokens = regex_tok.tokenize(sample_text)
    print(f"SimpleTokenizer output (first 20 tokens): {simple_tokens[:20]}")
    print(f"RegexTokenizer output (first 20 tokens): {regex_tokens[:20]}")

def demo_count_vectorizer() -> None:
    """ 
    Demonstrate CountVectorizer using RegexTokenizer on a small corpus. 
    """
    corpus = [
        "I love NLP.",
        "I love programming.",
        "NLP is a subfield of AI."
    ]
    tokenizer = RegexTokenizer()
    vectorizer = CountVectorizer(tokenizer)
    document_term_matrix = vectorizer.fit_transform(corpus)
    print("\n--- CountVectorizer demo ---")
    print("Learned vocabulary (token -> index):")
    for token, index in sorted(vectorizer.vocab.items(), key = lambda x: x[1]):
        print(f"    {index}: {token}")
    print("\nDocument-term matrix (rows correspond to documents):")
    for i, vec in enumerate(document_term_matrix):
        print(f"    Document {i}: {vec}")

def main() -> None:
    """ 
    The main method coordinates the program. 
    """
    # Sample sentences from the lab instructions.
    sentences = [
        "Hello, world! This is a test.",
        "NLP is fascinating... isn't it?",
        "Let's see how it handles 123 numbers and punctuation!"
    ]
    demo_tokenizers_on_sentences(sentences)
    demo_tokenizers_on_ud_english_ewt_sample(sample_length = 500)
    demo_count_vectorizer()

if __name__ == "__main__":
    main()