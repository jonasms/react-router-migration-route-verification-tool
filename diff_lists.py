from collections import Counter

def extract_values(raw_text):
    """Extracts values from a newline-separated string, ignoring leading numbers."""
    return [line.split('. ', 1)[1] for line in raw_text.strip().split('\n') if '. ' in line]

def compute_diff(v3_list, v6_list):
    """Computes the diff between two lists."""
    v3_counts = Counter(v3_list)
    v6_counts = Counter(v6_list)
    
    v3_diff = {item for item in v3_counts if v3_counts[item] > v6_counts[item]}
    v6_diff = {item for item in v6_counts if v6_counts[item] > v3_counts[item]}
    
    return sorted(v3_diff), sorted(v6_diff)

def print_diff(v3_diff, v6_diff):
    """Prints the differences in the required format."""
    if v3_diff:
        print("v3\n- - - - - - - - - - - -")
        for item in v3_diff:
            print(f"* {item}")
    
    if v6_diff:
        print("\nv6\n- - - - - - - - - - - -")
        for item in v6_diff:
            print(f"* {item}")

def main():
    print("Enter the v3 list (each item on a new line, then press Enter twice when done):")
    v3_raw = []
    while True:
        line = input()
        if line == "":
            break
        v3_raw.append(line)
    
    print("Enter the v6 list (each item on a new line, then press Enter twice when done):")
    v6_raw = []
    while True:
        line = input()
        if line == "":
            break
        v6_raw.append(line)
    
    v3_list = extract_values("\n".join(v3_raw))
    v6_list = extract_values("\n".join(v6_raw))
    
    v3_diff, v6_diff = compute_diff(v3_list, v6_list)
    print_diff(v3_diff, v6_diff)

if __name__ == "__main__":
    main()
