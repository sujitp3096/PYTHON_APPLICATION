"""
Duplicate File Finder - Python console application

Scans a folder (recursively) and finds duplicate files by comparing
content hashes (SHA-256), not just filenames. This correctly finds
duplicates even if they have different names, and avoids false positives
from files that merely share a name or size.

Usage: just run the script and follow the prompts.
"""

import os
import hashlib
from collections import defaultdict


def get_file_hash(path, chunk_size=8192):
    """Compute SHA-256 hash of a file's contents, reading in chunks
    so large files don't need to be loaded fully into memory."""
    hasher = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                hasher.update(chunk)
        return hasher.hexdigest()
    except (IOError, OSError) as e:
        print(f"  Could not read {path}: {e}")
        return None


def find_duplicates(root_folder):
    """Groups files by size first (cheap check), then hashes only files
    that share a size with at least one other file (avoids hashing
    every single file when most have unique sizes)."""

    size_map = defaultdict(list)

    print(f"\nScanning {root_folder} ...")
    file_count = 0
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            try:
                size = os.path.getsize(full_path)
                size_map[size].append(full_path)
                file_count += 1
            except OSError:
                continue

    print(f"Found {file_count} file(s). Comparing content of same-size files...")

    hash_map = defaultdict(list)
    candidates = [paths for paths in size_map.values() if len(paths) > 1]

    hashed_count = 0
    for paths in candidates:
        for path in paths:
            file_hash = get_file_hash(path)
            hashed_count += 1
            if file_hash:
                hash_map[file_hash].append(path)

    duplicates = {h: paths for h, paths in hash_map.items() if len(paths) > 1}
    return duplicates, file_count, hashed_count


def format_size(num_bytes):
    for unit in ["B", "KB", "MB", "GB"]:
        if num_bytes < 1024:
            return f"{num_bytes:.1f} {unit}"
        num_bytes /= 1024
    return f"{num_bytes:.1f} TB"


def print_report(duplicates):
    if not duplicates:
        print("\nNo duplicate files found.")
        return

    total_wasted_space = 0
    group_num = 1

    print(f"\nFound {len(duplicates)} group(s) of duplicate files:\n")
    for file_hash, paths in duplicates.items():
        file_size = os.path.getsize(paths[0])
        wasted = file_size * (len(paths) - 1)  # all copies after the first are "wasted"
        total_wasted_space += wasted

        print(f"Group {group_num} - {len(paths)} copies, {format_size(file_size)} each "
              f"(wasting {format_size(wasted)}):")
        for path in paths:
            print(f"    {path}")
        print()
        group_num += 1

    print(f"Total wasted space from duplicates: {format_size(total_wasted_space)}")


def delete_duplicates(duplicates):
    if not duplicates:
        return

    confirm = input("\nDelete duplicate copies, keeping one copy of each file? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("No files deleted.")
        return

    deleted_count = 0
    freed_space = 0

    for paths in duplicates.values():
        # Keep the first file, delete the rest
        keep = paths[0]
        for path in paths[1:]:
            try:
                size = os.path.getsize(path)
                os.remove(path)
                deleted_count += 1
                freed_space += size
                print(f"Deleted: {path}")
            except OSError as e:
                print(f"Could not delete {path}: {e}")

        print(f"Kept: {keep}\n")

    print(f"Deleted {deleted_count} file(s), freed {format_size(freed_space)}.")


def main():
    print("===== Duplicate File Finder =====")

    folder = input("Enter folder path to scan: ").strip()
    if not os.path.isdir(folder):
        print(f"Not a valid folder: {folder}")
        return

    duplicates, total_files, hashed_files = find_duplicates(folder)
    print(f"Hashed {hashed_files} file(s) for comparison.")

    print_report(duplicates)

    if duplicates:
        delete_duplicates(duplicates)


if __name__ == "__main__":
    main()
