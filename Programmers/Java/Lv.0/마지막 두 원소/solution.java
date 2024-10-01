// https://school.programmers.co.kr/learn/courses/30/lessons/181927?language=java

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length+1];
        
        for (int i=0;i<num_list.length;i++){
            answer[i] = num_list[i];
        }
        
        int LastEle = num_list[num_list.length-1];
        int PreEle = num_list[num_list.length-2];
        
        if (PreEle<LastEle){
            answer[num_list.length] = LastEle - PreEle;
        }
        else {
            answer[num_list.length]=2*LastEle;
        }
        return answer;
    }
}