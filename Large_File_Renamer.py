# -*- coding: utf-8 -*-

import os
import fnmatch

def bulk_rename(directory, file_pattern, new_name_pattern, start_index=1):
    """
    Rename files in a directory matching a pattern.

    :param directory: Path to the folder
    :param file_pattern: Pattern to match files (e.g., '*.txt')
    :param new_name_pattern: New name format (e.g., 'file_{:03d}.txt')
    :param start_index: Starting index for numbering
    """
    
    try:
        files = os.listdir(directory)
        matched_files = sorted(fnmatch.filter(files, file_pattern))
        
        if not matched_files:
            print("No files matched the pattern.")
            return
        
        for i, filename in enumerate(matched_files, start=start_index):
            old_path = os.path.join(directory, filename)
            
            # Extract file extension
            _, ext = os.path.splitext(filename)
            
            # Create new filename
            new_filename = new_name_pattern.format(i)
            new_path = os.path.join(directory, new_filename)
            
            print(f"{filename} → {new_filename}")
            confirm = input("Proceed? (y/n): ")
            if confirm.lower() != 'y':
                return
            
            # Rename file
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_filename}")
        
        print("\nRenaming completed successfully.")
    
    except Exception as e:
        print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    directory_path = input("Enter directory path: ")
    pattern = input("Enter file pattern (e.g., *.txt): ")
    new_pattern = input("Enter new naming pattern (e.g., file_{:03d}.txt): ")
    
    bulk_rename(directory_path, pattern, new_pattern)
    
