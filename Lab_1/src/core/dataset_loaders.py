# Import necessary libraries.
from io import StringIO
import requests
from typing import List

def download_text(url: str) -> str:
    """ 
    Download text content from a URL.
    @param url (str): URL to download.
    @return (str): Text content of the response. 
    """
    resp = requests.get(url, timeout = 30)
    resp.raise_for_status()
    return resp.text

def extract_sentences_from_conllu(conllu_text: str) -> List[str]:
    """ 
    Extract sentence texts from a ".conllu" file content.
    @param conllu_text (str): Raw ".conllu" file content.
    @return (List[str]): List of sentence strings extracted from '# text = ' lines. 
    """
    sentences = []
    for line in StringIO(conllu_text):
        line = line.strip()
        if line.startswith("# text ="):
            # Format: "# text = This is a sentence."
            parts = line.split("=", 1)
            if len(parts) == 2:
                sentence = parts[1].strip()
                if sentence:
                    sentences.append(sentence)
    return sentences

def load_raw_text_data(dataset_path: str = None) -> str:
    """ 
    Download UD_English-EWT train/dev/test ".conllu" files from the official Github repository and return concatenated raw text.
    @param dataset_path (str): Optional path parameter (ignored). Kept for API compatibility. 
    """
    # Official Universal Dependencies repository raw URLs for UD_English-EWT.
    base = "https://raw.githubusercontent.com/UniversalDependencies/UD_English-EWT/master/"
    files = [
        "en_ewt-ud-train.conllu",
        "en_ewt-ud-dev.conllu",
        "en_ewt-ud-test.conllu"
    ]
    all_sentences = []
    for file_name in files:
        url = base + file_name
        try:
            content = download_text(url)
            sentences = extract_sentences_from_conllu(content)
            all_sentences.extend(sentences)
        except Exception:
            # If any download fails, continue with what we have.
            continue
    # Join sentences with a single space to form a raw text blob.
    return " ".join(all_sentences)