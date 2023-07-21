import os
import glob

source_dir = r"D:\Josefina\YoRHa No.2B\renamed"
target_dir = r"D:\Josefina\YoRHa No.2B\sorted"

os.makedirs(target_dir, exist_ok=True)

file_extensions = ["*.jpg", "*.jpeg", "*.png", "*.gif"]

for index, extension in enumerate(file_extensions, start=1):
    files = sorted(glob.glob(os.path.join(source_dir, extension)))
    
    for oldfile in files:
        filename = os.path.basename(oldfile)
        newfile = os.path.join(target_dir, '{}{}'.format(index, os.path.splitext(filename)[1]))
        index_counter = 1
        
        while os.path.exists(newfile):
            newfile = os.path.join(target_dir, '{}_{}{}'.format(index, index_counter, os.path.splitext(filename)[1]))
            index_counter += 1
        
        os.rename(oldfile, newfile)





# import os
# import glob

# source_dir = r"D:\Josefina\YoRHa No.2B\asd"
# target_dir = r"D:\Josefina\YoRHa No.2B\renamed"

# os.makedirs(target_dir, exist_ok=True)

# file_extensions = ["*.jpg", "*.jpeg", "*.png", "*.gif"]

# index = 1

# for extension in file_extensions:
#     files = sorted(glob.glob(os.path.join(source_dir, extension)))

#     for oldfile in files:
#         filename = os.path.basename(oldfile)
#         newfile = os.path.join(target_dir, '{}{}'.format(index, os.path.splitext(filename)[1]))
        
#         while os.path.exists(newfile):
#             index += 1
#             newfile = os.path.join(target_dir, '{}{}'.format(index, os.path.splitext(filename)[1]))
        
#         os.rename(oldfile, newfile)
#         index += 1





# import os
# import glob

# def rename_files(directory):
#     file_list = glob.glob(os.path.join(directory, "*.[jJ][pP][gG]")) + glob.glob(os.path.join(directory, "*.[jJ][pP][eE][gG]")) + glob.glob(os.path.join(directory, "*.[pP][nN][gG]"))

#     num_files = len(file_list)
    
#     # Rename files in the range from 0 to num_files
#     for i in range(num_files):
#         file_path = file_list[i]
#         file_name = os.path.basename(file_path)
#         file_ext = os.path.splitext(file_name)[1]
#         new_name = f"{i}{file_ext}"
#         new_path = os.path.join(directory, new_name)
#         os.rename(file_path, new_path)
#         print(f"Renamed {file_name} to {new_name}")

# # Provide the directory path where the files are located
# directory_path = r"D:\Josefina\YoRHa No.2B\asd"
