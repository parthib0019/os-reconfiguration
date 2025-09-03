#!/bin/bash

 # File to save user commands
 OUTPUT_FILE="UserCommand.txt"

 # Get the user's history file (default: ~/.bash_history)
HIST_FILE="${HOME}/.bash_history"

# Copy all commands from history file to OUTPUT_FILE
cp "$HIST_FILE" "$OUTPUT_FILE"

echo "User command history saved to $OUTPUT_FILE"
