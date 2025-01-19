import re
import csv


def extract_triples(text):
    """
    Extract Subject-Predicate-Object triples from text.
    """
    # Placeholder: Use NLP libraries like spaCy or Stanford NLP for robust extraction.
    triples = []
    sentences = text.split('.')
    for sentence in sentences:
        match = re.search(r'(.+?) (implements|requires|involves) (.+)', sentence)
        if match:
            subject, predicate, obj = match.groups()
            triples.append((subject.strip(), predicate.strip(), obj.strip()))
    return triples


def save_triples_to_csv(triples, output_file):
    import os
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Predicate", "Object"])
        writer.writerows(triples)



if __name__ == "__main__":
    text = ("Yao's Garbled Circuits implements privacy-preserving computations. Secure auctions involve multiple "
            "participants.")
    triples = extract_triples(text)
    save_triples_to_csv(triples, "data/processed/entities.csv")
