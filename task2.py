import heapq

def merge_k_lists(lists):
    merged_list = []
    for list in lists:
        merged_list = merged_list + list 
    
    heapq.heapify(merged_list)

    return [heapq.heappop(merged_list) for _ in range(len(merged_list))]

    


def main():
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)

if __name__ == "__main__":
    main()