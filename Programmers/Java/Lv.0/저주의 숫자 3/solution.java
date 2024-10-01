// https://school.programmers.co.kr/learn/courses/30/lessons/120871?language=java

class Solution {
    public int solution(int n) {
        int answer = 1;
        int walker = 1;
        while (walker <= n){
            if (answer % 3 == 0 | contain_3 (answer)){
                answer+=1;
                continue;
            }
            else{
                answer+=1;
            }
            walker++;
        }
        return answer-1;
    }
    
    public boolean contain_3(int n){
        String string_num = String.valueOf(n);
        if (string_num.contains("3")){
            return true;
        }
        return false;
    }
}