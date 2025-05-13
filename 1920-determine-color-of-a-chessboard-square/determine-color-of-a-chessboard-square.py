class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col = coordinates[0]
        row = coordinates[1]

        col_index = ord(col) - ord('a')
        row_index = int(row)

        if(col_index+row_index) %2 == 0:
            return True
        else:
            return False
    
