import os
import shutil

# Function to sort files in a folder
def sort_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder path doesn't exist.")
        return

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    for file in files:
        file_extension = os.path.splitext(file)[1][1:]  # Extract file extension
        
        if file_extension:  # Check if file has an extension
            # Create folder based on file extension if it doesn't exist
            if not os.path.exists(os.path.join(folder_path, file_extension)):
                os.makedirs(os.path.join(folder_path, file_extension))

            # Move the file to the respective folder
            shutil.move(
                os.path.join(folder_path, file),
                os.path.join(folder_path, file_extension, file)
            )

# Function to display license.txt and prompt user to accept or reject
def display_license():
    license_path = os.path.join(os.path.dirname(__file__), "license", "license.txt")
    with open(license_path, 'r') as file:
        license_content = file.read()
        print(license_content)
        
        while True:
            choice = input("Do you accept the license? (y/n): ").lower()
            if choice == 'y':
                return True
            elif choice == 'n':
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")

# Ask user for the folder path
folder_path = input("Enter the path to the folder containing files to be sorted: ")

accepted_license = display_license()

if not accepted_license:
    print("Exiting the program.")
    exit()

sort_files(folder_path)
