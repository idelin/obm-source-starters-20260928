import json
import sys
from engine import run

for line in sys.stdin:
    if line.strip():
        print(json.dumps(run(json.loads(line)), ensure_ascii=False, separators=(",", ":")), flush=True)
