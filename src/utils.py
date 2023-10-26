"""Utility functions.

Functions:
    save_dict_as_json(data: dict, file_path: str) -> None:
        Save a dictionary as a JSON file. 
        If a file already exists, prompts for confirmation before overwriting.

Imports:
    os: Module to interact with the operating system, used to check file existence.
    json: Module to handle JSON data operations.
"""
import os
import json

def save_dict_as_json(data, file_path):
    """
    Save a dictionary as a JSON file. This enables ease of reference during development

    Parameters:
    - data (dict): Data in dictionary format to save.
    - file_path (str): Absolute path to save the JSON file to.

    Returns:
    - None
    """
    # Function to save the data as a JSON file with pretty printing
    def save_json():
        with open(file_path, 'w+', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    if not os.path.exists(file_path):
        save_json()
    else:
        ques = "A file by that name already exists. Would you like to replace it? (yes/no): "
        user_input = input(ques).strip().lower()

        if user_input in ('yes', 'y', 'YES'):
            save_json()
            print("File has been overwritten.")
        else:
            print("Exiting without saving.")
