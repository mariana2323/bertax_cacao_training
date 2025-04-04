import json
import sys

def combine_files(json_file1, txt_file1, json_file2, txt_file2, output_json, output_txt):
    # Load first JSON file
    with open(json_file1, 'r', encoding='utf-8') as f:
        sequences1 = json.load(f)
    
    # Load first TXT file
    with open(txt_file1, 'r', encoding='utf-8') as f:
        ids1 = f.read().splitlines()
    
    # Load second JSON file
    with open(json_file2, 'r', encoding='utf-8') as f:
        sequences2 = json.load(f)
    
    # Load second TXT file
    with open(txt_file2, 'r', encoding='utf-8') as f:
        ids2 = f.read().splitlines()
    
    # Ensure both pairs have matching counts
    if len(sequences1) != len(ids1) or len(sequences2) != len(ids2):
        print("Error: JSON and TXT files do not have matching numbers of items.")
        return
    
    # Combine sequences and ids
    combined_sequences = sequences1 + sequences2
    combined_ids = ids1 + ids2
    
    # Save combined JSON file
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(combined_sequences, f, indent=4)
    
    # Save combined TXT file
    with open(output_txt, 'w', encoding='utf-8') as f:
        f.write('\n'.join(combined_ids) + '\n')
    
    print(f"Successfully combined files into {output_json} and {output_txt}")
    print(f"Total sequences in combined file: {len(combined_sequences)}")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: python script.py <json_file1> <txt_file1> <json_file2> <txt_file2> <output_json> <output_txt>")
        sys.exit(1)
    
    json_file1 = sys.argv[1]
    txt_file1 = sys.argv[2]
    json_file2 = sys.argv[3]
    txt_file2 = sys.argv[4]
    output_json = sys.argv[5]
    output_txt = sys.argv[6]
    
    combine_files(json_file1, txt_file1, json_file2, txt_file2, output_json, output_txt)
