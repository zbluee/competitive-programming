class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        operations_value = {"--X" : -1, "X--" : -1, "++X" : 1, "X++" : 1}
        x = 0

        for operation in operations:
            x += operations_value[operation]

        return x

        
