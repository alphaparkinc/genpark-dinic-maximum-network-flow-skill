import sys
import json
from client import DinicMaxFlow

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "max_flow":
        n = params.get("num_vertices", 4)
        d = DinicMaxFlow(n)
        for e in params.get("edges", []):
            d.add_edge(e["u"], e["v"], e["cap"])
        return d.compute_max_flow(params.get("source", 0), params.get("sink", n - 1))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
