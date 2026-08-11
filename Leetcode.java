// 개선 중 

import java.util.ArrayDeque;
import java.util.List;

class Solution {
    public int lengthOfLongestSubstring(String s) {
      // S list로 쪼개기
      ArrayDeque<String> SDeque = new ArrayDeque<>(List.of(s.split("")));
      
      // 현재값 저장 
      ArrayDeque<String> now = new ArrayDeque<>();

      // 결과
      int result = 0;

      for(String i: SDeque){
        if(now.contains(i)){
            int idx = new ArrayList<>(now).indexOf(i);
            
        }
        
      }

      return 0;
    }
}

// 8_12
import java.util.ArrayDeque;
import java.util.List;
// import java.util.Deque;

class Leetcode {
  public static void main(String[] args) {
    System.out.println( lengthOfLongestSubstring("s") ) ;
  }
  
  public static int lengthOfLongestSubstring(String s) {
    
      // int result;

      // Deque<Integer> dq = new ArrayDeque<>();

      // 한 줄로 ArrayDeque 생성
      //ArrayDeque<String> deque = new ArrayDeque<>(List.of(str.split("")));
      
      // S list로 쪼개기
      ArrayDeque<String> SDeque = new ArrayDeque<>(List.of(s.split("")));


      for(String i: SDeque){
        System.out.println(i);
        
      }


      return 0;

      }
  }
