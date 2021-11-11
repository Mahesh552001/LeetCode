class Solution {
    public boolean isValidSudoku(char[][] board) {
        for(int i=0;i<9;i++){
            HashSet<Character> h=new HashSet<>();
            for(int j=0;j<9;j++){
                if(h.contains(board[i][j])){
                    return false;
                }
                if (board[i][j]!='.'){
                    h.add(board[i][j]);
                }
            }
        }
        for(int i=0;i<9;i++){
            HashSet<Character> h=new HashSet<>();
            for(int j=0;j<9;j++){
                if(h.contains(board[j][i])){
                    return false;
                }
                if (board[j][i]!='.'){
                    h.add(board[j][i]);
                }
            }
        }
        for(int i=0;i<9;i+=3){
            for(int j=0;j<9;j+=3){
                HashSet<Character> h=new HashSet<>();
                for(int r=i;r<i+3;r++){
                    for(int c=j;c<j+3;c++){
                        if(h.contains(board[r][c])){
                            return false;
                        }
                        if (board[r][c]!='.'){
                            h.add(board[r][c]);
                        }
                    }
                }
            }
        }
        return true;
    }
}