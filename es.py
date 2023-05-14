import sys
# To Check if a filename argument was provided
if len(sys.argv) < 2:
    print("Error: Please provide the filename as an argument.")
    sys.exit(1)
# Read in the text file and count the number of e's
filename = sys.argv[1]
try:
    with open(filename, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
    sys.exit(1)

count = 0
for char in text:
    if char.lower() == 'e':
        count += 1
# Output the number of e's in the text file
print(f"The file '{filename}' contains {count} occurrences of the letter 'e'.")


