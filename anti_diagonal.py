class AntiDiagonals:
    def sum(self, array, rows):
        res=[]

        for k in range(rows):
            i = 0
            j = k
            new_array = [0] * rows
            c = 0
            while i < rows and j >= 0:
                new_array[c] = array[i][j]
                c += 1
                i += 1
                j -= 1

            res.append(new_array)

        for x in range(rows):
            i = x
            j = rows - 1
            c = 0
            new_array = [0]*rows
            while i < rows and j >= 0:
                new_array[c] = array[i][j]
                c += 1
                i += 1
                j -= 1
            res.append(new_array)

        return res



rows = int(input())
array = []
for h in range(rows):
    a = list(map(int, input().split()))
    array.append(a)

object = AntiDiagonals()
print(object.sum(array, rows))