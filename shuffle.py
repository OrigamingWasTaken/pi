import random
import sys

# Get the input and output file names from the command line arguments
if len(sys.argv) < 2:
    print('Usage: python shuffle_lines.py <input_file>')
    sys.exit(1)
input_file_name = sys.argv[1]
output_file_name = input_file_name + '.shuffled'

# Open the input and output files
with open(input_file_name, 'r', encoding='utf-8', errors='ignore', newline='') as input_file, \
     open(output_file_name, 'w', encoding='utf-8', errors='ignore', newline='') as output_file:
    
    # Read the lines from the input file into a list
    lines = input_file.readlines()
    
    # Shuffle the lines randomly
    random.shuffle(lines)
    
    # Write the shuffled lines to the output file
    for line in lines:
        output_file.write(line)
        
# Overwrite the input file with the shuffled lines
import os
os.replace(output_file_name, input_file_name)