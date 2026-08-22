# This script opens a data file and counts the items inside
def process_lab_file(file_name):
    print(f"Opening file: {file_name}...")
    
    try:
        # Open the text file safely
        with open(file_name, 'r') as file:
            lines = file.readlines()
            
        total_samples = len(lines)
        print(f"Success! Found {total_samples} biological data rows inside.")
        return total_samples
        
    except FileNotFoundError:
        print("Error: The data file could not be found. Check the file name!")
        return 0

# Test the function
if __name__ == "__main__":
    # This looks for a mock data file
    process_lab_file("data_log.txt")
