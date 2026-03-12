import json
import os
from collections import defaultdict
from typing import List, Dict, Tuple


def read_corpus(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
    
def process_corpus(corpus_path: str, target_vocab_size: int):
    pass

def save_mode():
    pass


def main():
    corpus_path = '../data/corpus.txt'
    output_path = '../data/corpus.json'

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    if not os.path.exists(corpus_path):
        print(f"Corpus file not found at {corpus_path}")
        return
    
    print("Reading corpus...")

    merges, vocub_map, vocub_size, compression_ratio = process_corpus(
        corpus_path=corpus_path, target_vocab_size=1000)
    
    save_model(merges, vocub_map, vocub_size, compression_ratio, output_path)

    print(f"Model saved to {output_path}")
    print("Training completed successfully.")

if __name__ == "__main__":
    main()