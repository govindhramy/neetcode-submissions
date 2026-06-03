class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqrs = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                el = board[r][c]
                if el == ".":
                    continue
                if el in rows[r] or el in cols[c] or el in sqrs[(r//3)*3+c//3]:
                    return False
                rows[r].add(el)
                cols[c].add(el)
                sqrs[(r//3)*3+c//3].add(el)
        return True