import sys 
import json 
from tqdm import tqdm 
import os 

dir_path = sys.argv[1]

for file in tqdm(os.listdir(dir_path)):
    if not file.endswith(".json"):
        continue
    path = os.path.join(dir_path, file)
    with open(path, "r") as f:
        data = json.load(f)

    data["local"] = True
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

