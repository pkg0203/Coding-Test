//https://school.programmers.co.kr/learn/courses/30/lessons/120883?language=java

class Solution {
    public String solution(String[] id_pw, String[][] db) {
        for(String[] data : db){
            if(id_pw[0].equals(data[0]) && id_pw[1].equals(data[1])){
                return "login";
            }
            else if (id_pw[0].equals(data[0]) && !(id_pw[1].equals(data[1]))){
                return "wrong pw";
            }
        }
        return "fail";
    }
}