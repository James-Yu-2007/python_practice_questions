class testing:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

JamesClass = [testing('James', 90), testing('Steven', 92), testing('Michael', 88)]

totalMark = 0
for i in range(0, len(JamesClass)):
    totalMark += JamesClass[i].mark
averageMark = totalMark/len(JamesClass)
print(averageMark)