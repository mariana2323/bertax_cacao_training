import json
import argparse
import random

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('fragments_json_1')
    parser.add_argument('fragments_json_2')
    args = parser.parse_args()

    # Cargar fragmentos desde ambos archivos JSON
    fragments_1 = json.load(open(args.fragments_json_1))
    fragments_2 = json.load(open(args.fragments_json_2))

    # Combinar todos los fragmentos en una sola lista
    all_fragments = fragments_1 + fragments_2

    # Mezclar aleatoriamente la lista combinada
    random.shuffle(all_fragments)
    with open('output.fasta', 'w', encoding='utf-8') as fasta_file:
        # Imprimir en formato FASTA con identificadores numerados
        for i, fragment in enumerate(all_fragments):
            print(f'>seq_{i}\n{fragment}')