#!/bin/bash

# Directory to iterate over
DIRECTORY="./tests"

# Check if the directory exists
if [ -d "$DIRECTORY" ]; then
    # Iterate through each file in the directory
    for file in "$DIRECTORY"/*.c; do
        # Check if it is a file (not a subdirectory)
        if [ -f "$file" ]; then
            # Print the file name
            echo "Testing file: $file"
            clang-18 -fpass-plugin=`echo build/findfloats/FindFloats.*` "tests/$(basename "$file")" &> tests/$(basename "$file" .c).result
            echo
        fi
    done
else
    echo "Directory does not exist."
fi

# clang-18 -fpass-plugin=`echo build/findfloats/FindFloats.*` hello.c -o hello


