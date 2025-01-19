import jieba
import re

def clean_text(text):
    """
    Cleans text by removing special characters and extra whitespace.
    """
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
    return text.strip()

def tokenize_text(text):
    """
    Tokenizes Chinese text using Jieba.
    """
    return list(jieba.cut(text))

if __name__ == "__main__":
    raw_text = "Yao的加密电路实现了隐私保护计算。"
    cleaned_text = clean_text(raw_text)
    tokens = tokenize_text(cleaned_text)
    print("Cleaned Text:", cleaned_text)
    print("Tokens:", tokens)
