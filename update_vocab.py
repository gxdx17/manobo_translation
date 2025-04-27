import subprocess

# Define the command and arguments
command = [
    "onmt-main", "update_vocab",
    "--model_type", "transformer",
    "--train_src", "data/train.src",
    "--train_tgt", "data/train.tgt",
    "--src_vocab", "vocab/src-vocab.txt",
    "--tgt_vocab", "vocab/tgt-vocab.txt",
    "--data_dir", "data",
    "--output_dir", "data",
    "--config", "config_file.yml"  # Point to the config file here
]

# Run the command
try:
    subprocess.run(command, check=True)
    print("Vocabulary update successful!")
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")
