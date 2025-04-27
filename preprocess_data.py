import csv
import os
import re
import random
import unicodedata

# Paths
csv_file = 'ata-eng-sentence-pair.csv'
output_dir = 'data'
os.makedirs(output_dir, exist_ok=True)

# Settings
validation_split = 0.125  # 12.5% for validation

# Clean function
def clean_text(text):
    # Remove any non-UTF-8 characters
    text = ''.join(c for c in text if unicodedata.category(c) != 'Cn')  # Remove control characters
    text = re.sub(r'[^\w\s\.\,\?\!\-\"]', '', text)  # Remove weird symbols except basic punctuation
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces/tabs with single space
    return text.strip()

# Read and clean
pairs = []
with open(csv_file, newline='', encoding='utf-8', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)  # Use DictReader for easier column referencing
    for row in reader:
        src = clean_text(row['Verse Text (Ata Manobo)'])  # Source column by header
        tgt = clean_text(row['Verse Text (English)'])  # Target column by header
        if src and tgt:
            pairs.append((src, tgt))

# Shuffle and split (just training and validation)
random.shuffle(pairs)
val_size = int(len(pairs) * validation_split)

val_pairs = pairs[:val_size]
train_pairs = pairs[val_size:]

# Write files
def write_pairs(pairs, src_file, tgt_file):
    with open(src_file, 'w', encoding='utf-8') as src_out, open(tgt_file, 'w', encoding='utf-8') as tgt_out:
        for src, tgt in pairs:
            src_out.write(src + '\n')
            tgt_out.write(tgt + '\n')

write_pairs(train_pairs, os.path.join(output_dir, 'train.src'), os.path.join(output_dir, 'train.tgt'))
write_pairs(val_pairs, os.path.join(output_dir, 'val.src'), os.path.join(output_dir, 'val.tgt'))

print("✅ Done! Files saved in 'data/' folder.")
