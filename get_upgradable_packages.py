
import subprocess
import re
from tabulate import tabulate

def get_upgradable_packages():
    """Returns a list of upgradable packages and their target versions."""
    try:
        result = subprocess.run(['apt', 'list', '--upgradable'], capture_output=True, text=True, check=True)
        output_lines = result.stdout.splitlines()

        upgradable_packages = []
        # Skip the first line which is usually 'Listing... Done'
        for line in output_lines[1:]:
            # Regex to capture package name and target version
            match = re.match(r'^(\S+)/\S+\s+(\S+)\s+.*$', line)
            if match:
                package_name = match.group(1)
                target_version = match.group(2)
                upgradable_packages.append({'package': package_name, 'target_version': target_version})
        return upgradable_packages
    except subprocess.CalledProcessError as e:
        return f"Error checking for updates: {e.stderr}"
    except FileNotFoundError:
        return "'apt' command not found. This script is intended for Debian/Ubuntu-based systems."

if __name__ == "__main__":
    updates = get_upgradable_packages()
    if isinstance(updates, list):
        if updates:
            headers = ["Package", "Target Version"]
            table = [[update['package'], update['target_version']] for update in updates]
            print("Required updates:")
            print(tabulate(table, headers=headers, tablefmt="grid"))
        else:
            print("No required updates found.")
    else:
        print(updates)
