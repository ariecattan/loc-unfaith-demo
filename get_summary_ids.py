import os
import json 
import sys 

data_path = sys.argv[1] 
output_path = sys.argv[2]

summary_ids = [{"name": file[:-5]} for file in os.listdir(data_path) if file.endswith("json")]

summary_ids = sorted(summary_ids, key=lambda x: (int(x["name"].split("_")[0]), x["name"].split("_")[1]))

with open(output_path, "w") as f:
    json.dump(summary_ids, f, indent=4)
