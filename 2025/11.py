import sys
graph = {'out': []}
inputs = {'out': 0}
for line in sys.stdin:
    l = line.strip().split()
    graph[l[0][:-1]] = l[1:]
    inputs[l[0][:-1]] = 0


def is_dac_after_fft():
    stack = ['fft']
    while len(stack) > 0:
        node = stack.pop()
        if node == 'dac':
            return True
        stack.extend(graph[node])
    return False

def get_num_paths(A, B):
    print(A, B, len(graph), len(inputs))
    stack = [A]
    for n in graph:
        inputs[n] = 0
    while len(stack) > 0:
        node = stack.pop()
        #print(len(stack), node, inputs[node])
        if node in graph[B]:
            continue
        for n in graph[node]:
            if n in graph:
                inputs[n] = inputs[n] + 1
                stack.append(n)
        #print(stack)
    return inputs[B]

def part1():
    print(get_num_paths('you', 'out'))

def part2():
    key_nodes = []
    if  is_dac_after_fft():
        key_nodes = ['out', 'dac', 'fft', 'svr']
    else:
        key_nodes = ['out', 'fft', 'dac', 'svr']

    print(key_nodes)
    ans = 1
    for i in range(len(key_nodes) - 1):
        ans *= get_num_paths(key_nodes[i + 1], key_nodes[i])
        ni = []
        for j in inputs:
            if inputs[j] > 0:
                ni.append(j)
        for j in ni:
            graph.pop(j)
            inputs.pop(j)
        print(i, ans)
    print(ans)

"""
dac out 645 645
0 4800
fft dac 505 505
1 27256344000
svr fft 211 211
2 490695961032000
490695961032000
"""
part2()