from pathlib import Path

# Create a path object
file_path = Path("example.txt")

# Create the file if it doesn't exist
if not file_path.exists():
    file_path.touch()
    print(f"{file_path} created.")

# Check if file exists
if file_path.exists():
    print(f"{file_path} exists.")

# Write text to file
file_path.write_text("Hello, pathlib!\n")

# Append more text
with file_path.open("a") as f:
    f.write("Appending more text.\n")

# Read file content
content = file_path.read_text()
print("File Content:\n", content)

# File properties
print("File Name:", file_path.name)
print("File Suffix:", file_path.suffix)
print("Parent Directory:", file_path.parent)
