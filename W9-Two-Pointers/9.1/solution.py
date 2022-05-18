class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        prev = None
        i = 0
        dom = list(dominoes)
        for j in range(len(dom)):
            if dom[j] == 'L':
                if not prev:
                    while i <= j:
                        dom[i] = 'L'
                        i += 1
                else:
                    k = j
                    while i < k:
                        dom[i], dom[k] = 'R', 'L'
                        i += 1
                        k -= 1
                    i = j+1
                    prev = None
            elif dom[j] == 'R':
                if not prev:
                    i = j
                    prev = 'R'
                else:
                    while i < j:
                        dom[i] = 'R'
                        i += 1
        if prev:
            j = len(dom)-1
            while dom[j] == '.':
                dom[j] = 'R'
                j -= 1

        return ''.join(dom)
