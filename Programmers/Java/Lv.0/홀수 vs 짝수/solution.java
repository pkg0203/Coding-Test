// https://school.programmers.co.kr/learn/courses/30/lessons/181887?language=java

class Solution {
    public int solution(int[] num_list) {
        int even = 0;
        int odd = 0;
        
        for (int i=0;i<num_list.length;i++){
            if (i % 2 ==0){
                even += num_list[i];
            }
            else{
                odd += num_list[i];
            }
        }
        return (even > odd) ? even : odd;
    }
}