import json
import sys

def extract_sequences(json_file, txt_file, num_sequences, output_json, output_txt):
    # Load JSON file
    with open(json_file, 'r', encoding='utf-8') as f:
        sequences = json.load(f)
    
    # Load TXT file
    with open(txt_file, 'r', encoding='utf-8') as f:
        ids = f.read().splitlines()
    
    # Ensure the number of sequences to extract is not greater than the available data
    if num_sequences > len(sequences) or num_sequences > len(ids):
        print("Error: Requested number of sequences exceeds available data.")
        return
    
    # Extract the required number of sequences
    extracted_sequences = sequences[:num_sequences]
    extracted_ids = ids[:num_sequences]
    
    # Save extracted data into new files
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(extracted_sequences, f, indent=4)
    
    with open(output_txt, 'w', encoding='utf-8') as f:
        f.write('\n'.join(extracted_ids) + '\n')
    
    # Remove extracted sequences from master files
    remaining_sequences = sequences[num_sequences:]
    remaining_ids = ids[num_sequences:]
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(remaining_sequences, f, indent=4)
    
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(remaining_ids) + '\n')
    
    print(f"Successfully extracted {num_sequences} sequences to {output_json} and {output_txt}")
    print(f"Remaining sequences in master files: {len(remaining_sequences)}")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <master_json> <master_txt> <output_json> <output_txt>")
        sys.exit(1)
    
    master_json = sys.argv[1]
    master_txt = sys.argv[2]
    #num_sequences = int(sys.argv[3])
    output_json = sys.argv[3]
    output_txt = sys.argv[4]
    
    
    # Load JSON file to check its size
    with open(master_json, 'r', encoding='utf-8') as f:
        sequences = json.load(f)
    
    total_sequences = len(sequences)
    print(f"Total sequences available: {total_sequences}")
    
    while True:
        try:
            num_sequences = int(input("Enter the number of sequences to extract: "))
            if num_sequences > total_sequences or num_sequences <= 0:
                print("Invalid input. Please enter a number between 1 and", total_sequences)
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    extract_sequences(master_json, master_txt, num_sequences, output_json, output_txt)
