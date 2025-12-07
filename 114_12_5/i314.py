T = int(input())  # 讀取測試案例數量

for _ in range(T):
    N, K = list(map(int, input().split()))
    p_list = list(map(int, input().split()))
    M = 4

    class F:
        def __init__(self) -> None:
            self.x = 10**8  # max - min + l
            self.d = [0] * M

        def __repr__(self) -> str:
            s = ' '.join(map(str, self.d))
            return f'{self.x} {s}'

        def update(self, a, b):
            m = min(a.x, b.x)
            self.x = m
            self.d = [0] * M
            for i in range(M):
                if a.x + i - m < M:
                    self.d[a.x + i - m] += a.d[i]
            for i in range(M):
                if b.x + i - m < M:
                    self.d[b.x + i - m] += b.d[i]

    class SegmentTreeL:
        def __init__(self, n):
            self.num = 1 << (n - 1).bit_length()
            self.data = [F() for _ in range(self.num * 2 - 1)]
            self.f = [False] * (self.num * 2 - 1)
            self.p = [0] * (self.num * 2 - 1)

        def _eval(self, k):
            if self.f[k]:
                self.f[k] = False
                y = self.p[k]
                self.p[k] = 0
                self.data[2 * k + 1].x += y
                self.p[2 * k + 1] += y
                self.f[2 * k + 1] = True
                self.data[2 * k + 2].x += y
                self.p[2 * k + 2] += y
                self.f[2 * k + 2] = True

        def replace(self, k, x):
            a, b = k, k + 1
            stack = [(0, 0, self.num)]
            k_list = []
            while stack:
                k, l, r = stack.pop()
                if r <= a or l >= b:
                    continue
                if r - l == 1:
                    self.data[k].x = x
                    self.data[k].d[0] = 1
                    continue
                self._eval(k)
                m = (r - l) // 2
                stack.append((2 * k + 1, l, l + m))
                stack.append((2 * k + 2, l + m, r))
                k_list.append(k)
            for k in reversed(k_list):
                self.data[k].update(self.data[2 * k + 1], self.data[2 * k + 2])

        def update(self, a, b, x):  # a <= i < b
            stack = [(0, 0, self.num)]
            k_list = []
            while stack:
                k, l, r = stack.pop()
                if r <= a or l >= b:
                    continue
                if r - l == 1:
                    self.data[k].x += x
                    continue
                if a <= l and r <= b:
                    self.data[k].x += x
                    self.f[k] = True
                    self.p[k] += x
                    continue
                self._eval(k)
                m = (r - l) // 2
                stack.append((2 * k + 1, l, l + m))
                stack.append((2 * k + 2, l + m, r))
                k_list.append(k)
            for k in reversed(k_list):
                self.data[k].update(self.data[2 * k + 1], self.data[2 * k + 2])

    sgt = SegmentTreeL(N)
    stack_max = []
    stack_min = []
    ans = 0
    for r in range(N):
        sgt.replace(r, r)
        p = p_list[r]
        l = r
        while stack_max and stack_max[-1][0] < p:
            x, ln = stack_max.pop()
            sgt.update(ln, l, -x)
            l = ln
        stack_max.append((p, l))
        sgt.update(l, r + 1, p)
        l = r
        while stack_min and stack_min[-1][0] > p:
            x, ln = stack_min.pop()
            sgt.update(ln, l, x)
            l = ln
        stack_min.append((p, l))
        sgt.update(l, r + 1, -p)
        f = sgt.data[0]
        for i in range(M):
            if f.x + i <= r + K:
                ans += f.d[i]

    print(ans)