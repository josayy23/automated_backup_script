from backup_utils import create_backup, restore_backup

def main():
    print("Automated Backup Script")
    while True:
        print("\nOptions:")
        print("1. Create a backup")
        print("2. Restore a backup")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            source = input("Source: ")
            destination = input("Destination: ")
            create_backup(source, destination)
        elif choice == '2':
            backup_path = input("Backup directory: ")
            restore_to = input("Enter the directory to restore to: ")
            restore_backup(backup_path, restore_to)
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
