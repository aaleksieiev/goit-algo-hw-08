import heapq

def main():
    cable_parts = [3 ,10, 20, 30, 40, 25, 28, 27, 1, 2]

    heapq.heapify(cable_parts)

    print(cable_parts)
    
    smallest_part_to_concat = heapq.nsmallest(2, cable_parts)
    while len(smallest_part_to_concat) > 1:
        new_cheap_part = sum(smallest_part_to_concat)
        print(f"{smallest_part_to_concat[0]}+{smallest_part_to_concat[1]}={sum(smallest_part_to_concat)}\n")
        heapq.heappop(cable_parts)
        heapq.heappop(cable_parts)
        heapq.heappush(cable_parts, new_cheap_part)
        print(cable_parts)
        smallest_part_to_concat = heapq.nsmallest(2, cable_parts)

    print(f"result: {heapq.heappop(cable_parts)}")

if __name__ == "__main__":
    main()