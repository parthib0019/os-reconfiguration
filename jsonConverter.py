import re
import json

# Input file (bash history or collected commands)
history_file = "UserCommand.txt"

# Define regex patterns for useful commands
patterns = {
    "package_install": r"(apt|apt-get|yum|dnf|pacman)\s+(install|remove|update|upgrade)",
    "python_package": r"(pip|pip3)\s+install",
    "node_package": r"(npm|yarn)\s+(install|add)",
    "git_clone": r"git\s+clone",
    "build": r"(make|cmake|configure)",
    "config_edit": r"(vim|nano|echo).*~\/\..*",
    "systemctl": r"systemctl\s+(enable|start|stop|restart)"
}

structured_commands = []

with open(history_file, "r") as f:
    for line in f:
        command = line.strip()
        if not command or command in ["ls", "cd", "pwd", "clear", "exit"]:
            continue  # skip noise
        
        matched_category = None
        for category, regex in patterns.items():
            if re.search(regex, command):
                matched_category = category
                break
        
        if matched_category:
            structured_commands.append({
                "command": command,
                "category": matched_category
            })

# Save to JSON
with open("structured_history.json", "w") as f:
    json.dump(structured_commands, f, indent=4)

print(f"Extracted {len(structured_commands)} useful commands.")
