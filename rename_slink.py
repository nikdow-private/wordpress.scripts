import os
import re
from pathlib import Path

# Configuration
search_dir = Path(".")
old_pattern = "/old/path"
new_pattern = "/new/path"


def update_symlinks(directory, old_p, new_p):
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
            break
        break

if __name__ == "__main__":
    update_symlinks(search_dir, old_pattern, new_pattern)
    print("Symbolic link modification complete.")

