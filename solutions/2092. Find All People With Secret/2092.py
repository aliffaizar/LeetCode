class UnionFind:
  def __init__(self, n: int):
    self.id = list(range(n))

  def union(self, u: int, v: int) -> None:
    self.id[self.find(u)] = self.find(v)

  def connected(self, u: int, v: int) -> bool:
    return self.find(self.id[u]) == self.find(self.id[v])

  def reset(self, u: int):
    self.id[u] = u

  def find(self, u: int) -> int:
    if self.id[u] != u:
      self.id[u] = self.find(self.id[u])
    return self.id[u]


class Solution:
  def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
    uf = UnionFind(n)
    timeToPairs = defaultdict(list)

    uf.union(0, firstPerson)

    for x, y, time in meetings:
      timeToPairs[time].append((x, y))

    for _, pairs in sorted(timeToPairs.items(), key=lambda x: x[0]):
      peopleUnioned = set()
      for x, y in pairs:
        uf.union(x, y)
        peopleUnioned.append(x)
        peopleUnioned.append(y)
      for person in peopleUnioned:
        if not uf.connected(person, 0):
          uf.reset(person)

    return [i for i in range(n) if uf.connected(i, 0)]
