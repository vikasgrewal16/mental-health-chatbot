
from typing import List
from transformers import DistilBertTokenizer
import re

# Load the tokenizer
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")

def normalize_text(text: str) -> str:
    """
    Normalize the text by converting to lowercase, removing special characters, and replacing multiple spaces.

    Args:
        text (str): The input text.

    Returns:
        str: Normalized text.
    """
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    return text

def tokenize_text(text: str) -> List[int]:
    """
    Tokenize the text using DistilBERT tokenizer.

    Args:
        text (str): The input text.

    Returns:
        List[int]: Token IDs.
    """
    tokens = tokenizer.encode(text, add_special_tokens=True)
    return tokens

def pad_truncate(tokens: List[int], max_length: int) -> List[int]:
    """
    Pad or truncate tokens to a fixed length.

    Args:
        tokens (List[int]): List of token IDs.
        max_length (int): Desired length of the token list.

    Returns:
        List[int]: Padded or truncated list of token IDs.
    """
    if len(tokens) > max_length:
        return tokens[:max_length]
    return tokens + [0] * (max_length - len(tokens))

def clean_text(text: str) -> str:
    """
    Clean text by removing digits and extra spaces.

    Args:
        text (str): The input text.

    Returns:
        str: Cleaned text.
    """
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # Remove digits
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    return text
