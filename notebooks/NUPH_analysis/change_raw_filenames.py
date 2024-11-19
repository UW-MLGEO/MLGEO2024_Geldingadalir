import os

def rename_files(directory):
    for filename in os.listdir(directory):
        old_file = os.path.join(directory, filename)
        if os.path.isfile(old_file):
            new_filename = filename.split('_', 1)[-1]
            new_file = os.path.join(directory, new_filename)
            os.rename(old_file, new_file)
            print(f"Renamed: {old_file} to {new_file}")

directory = 'notebooks/NUPH_analysis/data/raw'
rename_files(directory)