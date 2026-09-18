class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for i in range(len(operations)):
            if operations[i] == "+":
                add = score[-1] + score[-2]
                score.append(add)
            elif operations [i] == "C":
                score.pop()
            elif operations[i] == "D":
                double = 2*score[-1]
                score.append(double)
            else:
                score.append(int(operations[i]))
        
        return sum(score)