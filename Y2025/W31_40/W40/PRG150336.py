def solution(commands):
    answer = []
    SIZE = 50
    grid_value = [""] * (SIZE * SIZE)
    group = [i for i in range(SIZE * SIZE)]

    def find_root(v):
        while v != group[v]:
            v = group[v]
        return v

    def union(v1, v2):
        r1, r2 = find_root(v1), find_root(v2)
        if grid_value[r1] == "" and grid_value[r2]:
            grid_value[r1] = grid_value[r2]
        group[r2] = r1

    for command in commands:
        comm = list(command.split())
        if comm[0] == "UPDATE":
            if len(comm) == 4:
                r, c, value = int(comm[1]) - 1, int(comm[2]) - 1, comm[3]
                grid_value[find_root(r * SIZE + c)] = value
            elif len(comm) == 3:
                value1, value2 = comm[1], comm[2]
                for i in range(len(grid_value)):
                    if grid_value[i] == value1:
                        grid_value[i] = value2
        elif comm[0] == "MERGE":
            r1, c1, r2, c2 = int(comm[1]) - 1, int(comm[2]) - 1, int(comm[3]) - 1, int(comm[4]) - 1
            union(r1 * SIZE + c1, r2 * SIZE + c2)
        elif comm[0] == "UNMERGE":
            r, c = int(comm[1]) - 1, int(comm[2]) - 1
            root = find_root(r * SIZE + c)
            tmp = []
            original_val = grid_value[root]
            for i in range(SIZE * SIZE):
                if find_root(i) == root:
                    tmp.append(i)
            for i in tmp:
                grid_value[i] = ""
                group[i] = i
            grid_value[r * SIZE + c] = original_val

        elif comm[0] == "PRINT":
            r, c = int(comm[1]) - 1, int(comm[2]) - 1
            answer.append(grid_value[find_root(r * SIZE + c)])

    for i in range(len(answer)):
        if answer[i] == "":
            answer[i] = "EMPTY"
    return answer
