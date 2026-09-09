from client import DinicMaxFlow

def main():
    print("=== Dinic's Maximum Network Flow ===")
    d = DinicMaxFlow(4)
    d.add_edge(0, 1, 10)
    d.add_edge(0, 2, 10)
    d.add_edge(1, 2, 2)
    d.add_edge(1, 3, 4)
    d.add_edge(2, 3, 9)

    res = d.compute_max_flow(0, 3)
    print("Max Flow Output:", res)
    assert res["max_flow"] == 13

    print("Dinic Max Flow verified successfully!")

if __name__ == "__main__":
    main()
