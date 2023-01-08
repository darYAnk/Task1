class Levinstein():

    def __init__(self):
        self.A = []
        self.len_f1 = 0
        self.len_f2 = 0
        self.outp = open('scores.txt', 'w+')

    def start(self, file1, file2):
        self.f1 = open(file1, 'r')
        self.f2 = open(file2, 'r')
        self.f1 = ' ' + self.f1.read()
        self.f2 = ' ' + self.f2.read()
        self.len_f1 = len(self.f1)
        self.len_f2 = len(self.f2)
        self.A = [[0] * self.len_f1 for i in range(self.len_f2)]
        self.dinamic()
        self.output()

    def dinamic(self):
        for i in range(self.len_f2):
            for j in range(self.len_f1):
                if i == 0 or j == 0:
                    self.A[i][j] = i + j
                else:
                    self.A[i][j] = 0

        for i in range(1, self.len_f2):
            for j in range(1, self.len_f1):
                if self.f1[j] == self.f2[i]:
                    self.A[i][j] = min(self.A[i-1][j-1], self.A[i- 1][j] + 1, self.A[i][j-1] + 1)
                else:
                    self.A[i][j] = min(self.A[i-1][j-1], self.A[i- 1][j], self.A[i][j-1]) + 1

    def output(self):
        self.outp.write(f'{self.A[len(self.f2) - 1][len(self.f1) - 1]/self.len_f2}\n')


inp = open('input.txt', 'r')
Win = Levinstein()

for i in inp.readlines():
    Win.start(i.split())
