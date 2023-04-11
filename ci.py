import wandb

print(f"The version of wand is: {wandb.__version__}")
assert wandb.__version__ == '0.14.2', f'Expected version 0.14.2, but got {wandb.__version__}'
