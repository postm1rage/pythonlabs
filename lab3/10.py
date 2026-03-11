n = int(input())
permissions = {}

for _ in range(n):
    data = input().split()
    filename = data[0]
    rights = set(data[1:])
    permissions[filename] = rights

m = int(input())
for _ in range(m):
    operation, filename = input().split()
    
    op_map = {
        'read': 'R',
        'write': 'W', 
        'execute': 'X'
    }
    
    if op_map[operation] in permissions.get(filename, set()):
        print('OK')
    else:
        print('Access denied')