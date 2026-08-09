import java.util.ArrayDeque;
import java.util.List;
import java.util.Deque;

class leetcode {  
  public int lengthOfLongestSubstring(String s) {
      
      int result;

      Deque<Integer> dq = new ArrayDeque<>();

      // 한 줄로 ArrayDeque 생성
      //ArrayDeque<String> deque = new ArrayDeque<>(List.of(str.split("")));
      
      // S list로 쪼개기
      ArrayDeque<String> SDeque = new ArrayDeque<>(List.of(s.split("")));

      return result;

    }
}