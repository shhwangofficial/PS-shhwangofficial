N, M, S = 100, 2, 33
with open("python_input.txt", "w", encoding="utf-8") as file:
    file.write(f"{N} {M} {S}\n")

    boxes = [0] * 101
    tail = 0
    for head in range(3, 100, 3):
        boxes[head] = 1
        while True:
            tail += 1
            if boxes[tail] == 0:
                file.write(f"{head} {tail}\n")
                boxes[tail] = 1
                break
