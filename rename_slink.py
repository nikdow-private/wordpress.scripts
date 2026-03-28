#!/usr/bin/env python3
#
# change slink to wp-composer in /wp-content/plugins
#

import os
import re
from pathlib import Path

# Configuration
search_dir = Path(".")

def update_symlinks(directory):
    """Recursively finds and updates symbolic links."""
    for root, dirs, files in os.walk(directory):
        for name in files + dirs:
            full_path = Path(root) / name
            if full_path.is_symlink():
                current_target = os.readlink(full_path)
                # Perform string replacement
                new_target = re.sub(r"..\/..\/..", "../..", current_target)

                if new_target != current_target:
                    print(f"Updating symlink: {full_path}")
                    print(f"Old target: {current_target}")
                    print(f"New target: {new_target}")

                    # Remove the old symlink and create the new one
                    # This approach is not atomic, but generally safe for batch operations
                    try:
                        os.unlink(full_path)
                        os.symlink(new_target, full_path)
                        print("Update successful.")
                    except OSError as e:
                        print(f"Error updating link {full_path}: {e}")

if __name__ == "__main__":
    update_symlinks(search_dir)
    print("Symbolic link modification complete.")

