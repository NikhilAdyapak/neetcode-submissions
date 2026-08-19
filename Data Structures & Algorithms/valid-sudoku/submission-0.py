class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board[0])

        def check_seen(arr):
            seen = []
            for ele in arr:
                if ele == ".":
                    continue
                if int(ele) in seen:
                    return False
                else:
                    seen.append(int(ele))
            return True

        for i in range(n):
            #vertical
            flag = check_seen([x[i] for x in board])
            if not flag:
                return False
            
            #horizontal
            flag = check_seen(board[i])
            if not flag:
                return False
            
            #boxes
            r_base = (i // 3) * 3
            c_base = (i % 3) * 3
            box = [board[r_base + (j // 3)][c_base + (j % 3)] for j in range(9)]

            flag = check_seen(box)
            if not flag:
                return False

        return True