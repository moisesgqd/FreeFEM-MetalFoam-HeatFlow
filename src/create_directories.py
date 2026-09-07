import argparse
from pathlib import Path
import sys

def create_directory_from_args(path_str):
    """Creates the specified directory from a command-line argument."""
    directory_path = Path(path_str)
    try:
        # parents=True creates missing parent directories
        # exist_ok=True avoids an error if the directory already exists
        directory_path.mkdir(parents=True, exist_ok=True)
        print(f"Successfully ensured directory exists at: {directory_path.resolve()}")
    except OSError as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a directory specified by a path argument.")
    parser.add_argument(
        "directory_path",
        type=str,
        help="The path of the directory to create (e.g., 'logs/new_run')"
    )
    args = parser.parse_args()
    create_directory_from_args(args.directory_path)
