// https://school.programmers.co.kr/learn/courses/30/lessons/120866

class Solution {
    public int solution(int[][] board) {
        int answer = 0;
        int n = board.length;
        for (int i = 0 ; i < n ; i++){
            for (int j = 0 ; j < n ; j ++){
                if(is_safe(board,i,j,n) && board[i][j]!=1){answer++;}
            }
        }

        return answer;
    }
    public boolean is_safe(int[][] board,int i, int j, int n){
        // 위가 존재
        if (i>0){
            if(board[i-1][j] == 1)return false;
            
            if (j>0){
                if(board[i-1][j-1] == 1)return false;
            }
            if (j<n-1){
                if(board[i-1][j+1] == 1)return false;
            }
        }
        if (j>0){
            if(board[i][j-1] == 1)return false;
        }
        if (j < n-1) {
            if(board[i][j+1] == 1)return false;
        }
        
        if (i < n-1){
            if(board[i+1][j] == 1)return false;
            
            if (j>0) {
                if(board[i+1][j-1] == 1)return false;;
            }
            
            if (j < n-1) {
                if(board[i+1][j+1] == 1)return false;
            }
        }
        return true;
    }
}