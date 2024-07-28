import os
import shutil
from datetime import datetime

def  create_backup(source, destination):
    """
        Create a backup of the source directory in the destination directory.
        """
    if not os.path.exists(source):
        raise ValueError("source directory does not exist")

    if not os.path.exists(destination):
        os.makedirs(destination)

    current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    backup_name = f"backup_{current_time}"
    backup_path = os.path.join(destination, backup_name)

    try:
        shutil.copytree(source, backup_path)
        print(f"Backup created at {backup_path}")
    except Exception as e:
        print(f"Error creating backup: {e}")

def restore_backup(backup_path, restore_to):
    """
        Restore a backup from the backup_path to the restore_to directory.
        """
    if not os.path.exists(backup_path):
        raise ValueError("backup_path does not exist")

    if not os.path.exists(restore_to):
        os.makedirs(restore_to)

    try:
        shutil.copytree(backup_path, restore_to)
        print(f"Restored backup at {restore_to}")
    except Exception as e:
        print(f"Error restoring backup: {e}")


