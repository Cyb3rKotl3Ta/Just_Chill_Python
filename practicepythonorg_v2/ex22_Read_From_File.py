file_path = 'practicepythonorg_v2/files_for_ex/ex22_categories.txt' # .../ex22_categories.txt from SUN db
category_counts = {}

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split('/')
        category = parts[2]
        
        category_counts[category] = category_counts.get(category, 0) + 1

for category, count in category_counts.items():
    print(f"{category}: {count} images")
