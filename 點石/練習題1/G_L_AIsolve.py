n = int(input())
v = [0] + list(map(int, input().split()))

parent = [0] * (n + 1)
children = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    parent[b] = a
    children[a].append(b)

root = parent.index(0, 1)

child_count = [len(children[i]) for i in range(n + 1)]
alive = [True] * (n + 1)
days = 0

while True:
    fallen = []

    # 找出今天會掉落的葉節點
    for i in range(1, n + 1):
        if alive[i] and i != root and child_count[i] == 0:
            if v[i] < v[parent[i]]:
                fallen.append(i)

    if not fallen:
        break

    days += 1
    total = [0] * (n + 1)
    count = [0] * (n + 1)

    # 統計每個父節點今天接收到的葉子
    for i in fallen:
        p = parent[i]
        total[p] += v[i]
        count[p] += 1

    # 一起更新父節點的值
    for i in range(1, n + 1):
        if count[i] > 0:
            v[i] = (v[i] + total[i]) // (count[i] + 1)

    # 移除掉落的葉節點
    for i in fallen:
        alive[i] = False
        child_count[parent[i]] -= 1

# 依照層數找出剩餘節點
layers = []
queue = [(root, 0)]

for node, depth in queue:
    while len(layers) <= depth:
        layers.append([])

    layers[depth].append(node)

    for child in children[node]:
        if alive[child]:
            queue.append((child, depth + 1))

print(days)

for layer in layers:
    layer.sort()  # 依節點編號排序
    print(*(v[node] for node in layer))