import sys

# Check if the file path is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python script.py <file_path>")
    sys.exit(1)

# The file path is the first argument after the script name
file_path = sys.argv[1]

# Keywords to search for
keywords = ["fdiv", "fadd", "fmul", "fsub"]

# Open and read the file
with open(file_path, 'r') as file:
    # Iterate over each line
    for line in file:
        # Check if any keyword is in the line
        if any(keyword in line for keyword in keywords):
            # Print the line
            print("  " + line.strip())
