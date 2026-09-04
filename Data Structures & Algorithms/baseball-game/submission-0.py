class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        current = 0
        for operation in operations:
            if operation == "+":
                record.append(record[current-1] + record[current-2])
                current += 1
            elif operation == "D":
                record.append(2 * record[current-1])
                current += 1
            elif operation == "C":
                record.pop()
                current -= 1
            else: 
                record.append(int(operation))
                current += 1
        return sum(record)