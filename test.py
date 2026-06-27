import torch

print("CUDA available:", torch.cuda.is_available())
print("CUDA device count:", torch.cuda.device_count())


if torch.cuda.is_available():
    print("Current CUDA device:", torch.cuda.current_device())
    print("CUDA device name:", torch.cuda.get_device_name(0))
    print("CUDA device version:", torch.version.cuda)
    
else:
    print("CUDA is not available")
    
# 生成 requirement.txt  pip freeze > requirement.txt