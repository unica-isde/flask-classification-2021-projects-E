import os


def create_folder_if_not_found(full_path):
    """
    This function creates a directory if it doesn't exist.
    """
    if not os.path.exists(full_path):
        os.makedirs(full_path)
