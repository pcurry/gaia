import os

def scan_sectors_and_count_lines():
    csv_files_info = []
    sectors_path = "sector_output"
    if not os.path.isdir(sectors_path):
        print(f"Error: The subfolder '{sectors_path}' does not exist in the current directory.")
        return []
    for filename in os.listdir(sectors_path):
        if filename.endswith(".csv"):
            filepath = os.path.join(sectors_path, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    line_count = sum(1 for line in f)
                csv_files_info.append((filename, line_count))
            except Exception as e:
                print(f"Error reading file {filename}: {e}")
    return csv_files_info

if __name__ == "__main__":
    csv_info = scan_sectors_and_count_lines()
    if csv_info:
        print("CSV files found in 'sectors' subfolder and their line counts:")
        for filename, line_count in csv_info:
            print(f"- {filename}: {line_count} lines")
    else:
        print("No CSV files found in the 'sectors' subfolder or the subfolder does not exist.")