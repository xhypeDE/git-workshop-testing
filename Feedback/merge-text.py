import os
import pathlib

print("Starting Feedback Merge...")

# Set the directory containing the .txt files
directory = pathlib.Path(__file__).parent.resolve()

# Set the name of the new file to be created
new_file = 'merged.txt'

counter = 0

# Go through all the .txt files in the directory
for filename in os.listdir(directory):
    # Only process .txt files
    if filename.endswith(".txt"):
        # Open the file
        with open(os.path.join(directory, filename), 'r') as f:
            # Read the contents of the file
            content = f.read()

            # Write the contents to the new file
            with open(new_file, 'a') as fw:
                if counter == 0:
                    fw.write('FEEDBACK MERGE:')
                fw.write(f'{filename}:')
                fw.write('\n')
                fw.write(content)
                fw.write('\n')
                fw.write('\n')
    counter += 1

print("Done!")
