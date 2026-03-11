n = int(input())
votes = {}

for _ in range(n):
    name, count = input().split()
    count = int(count)
    votes[name] = votes.get(name, 0) + count

for name in sorted(votes.keys()):
    print(name, votes[name])