// 출처

/*
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 */
// 개선 중
class Solution {
    public int lengthOfLongestSubstring(String s) {

    if(s.isEmpty()){
            return 0;
        }
        // S list로 쪼개기
        ArrayDeque<String> SDeque = new ArrayDeque<>(List.of(s.split("")));
        // System.out.println(SDeque.size());
        // 현재값 저장 
        ArrayDeque<String> now = new ArrayDeque<>();
        
        //검색
        Set<String> SearchSet = new HashSet<>();

        // 결과
        int result = 0;

        for(String i: SDeque){
            // System.out.println(i);

            if(SearchSet.contains(i)){
                int idx = new ArrayList<>(now).indexOf(i);
                int end  = now.size();
                int half = end/2;
                
                if(idx < half){
                    for (int k = 0; k < idx+1; k++){
                        String NowString = now.peekFirst();
                        now.pollFirst();
                        SearchSet.remove(NowString);

                        // System.out.println("제대로 나오나"+now.size());
                    }
                    now.addLast(i);
                    SearchSet.add(i);
                }

                else{

                ArrayDeque<String> nowNew = new ArrayDeque<>();
                Set<String> NewSearchSet = new HashSet<>();
                // 새로운 리스트를 만든 후 주소 바꾼 후 비교 
                for (int t = idx+1; t < end; t++){
                    String nowStr = new ArrayList<>(now).get(t);
                    // System.out.println("제대로 나오나"+now.size());
                    nowNew.addLast(nowStr);
                    NewSearchSet.add(nowStr);
                
                // 리스트 주소 변경
                now = nowNew;
                SearchSet = NewSearchSet;

                now.addLast(i);
                SearchSet.add(i);
                result = Math.max(result,now.size());

                }
            }
            
         }

            else {
                
                // System.out.println("이거");
                now.addLast(i);
                SearchSet.add(i);
                result = Math.max(result,now.size());
                // System.out.println(result);
            }
            System.out.println(now);
        }

        return result;
    }
}


//개선 중 
import java.util.ArrayDeque;
import java.util.List;
import java.util.Set;
import java.util.HashSet;

class Solution {
    public int lengthOfLongestSubstring(String s) {
    
     if(s.isEmpty()){
        return 0;
     }
      // S list로 쪼개기
      ArrayDeque<String> SDeque = new ArrayDeque<>(List.of(s.split("")));
      System.out.println(SDeque.size());
      // 현재값 저장 
      ArrayDeque<String> now = new ArrayDeque<>();
      
      //검색
      Set<String> SearchSet = new HashSet<>();

      // 결과
      int result = 0;

      for(String i: SDeque){
        // System.out.println(i);

        if(SearchSet.contains(i)){
            int idx = new ArrayList<>(now).indexOf(i);
            int end  = now.size();
            int half = end/2;
            
            if(idx < half){
            for (int k = 0; k < idx+1; k++){
                String NowString = now.peekFirst();
                now.pollFirst();
                SearchSet.remove(NowString);

                // System.out.println("제대로 나오나"+now.size());
            }
            now.addLast(i);
            SearchSet.add(i);
            }

            else{

            for (int t = idx+1; t < end+1; t=++){
                int idx = new ArrayList<>(now).get(i);
                // System.out.println("제대로 나오나"+now.size());
            }
            now.addLast(i);
            SearchSet.add(i);
            }

            }
        }
        else {
            System.out.println("이거");
            now.addLast(i);
            SearchSet.add(i);
            result = Math.max(result,now.size());
            System.out.println(result);
        }
        
      }

      return result;
    }
}

//개선 중 
import java.util.ArrayDeque;
import java.util.List;

class Solution {
    public int lengthOfLongestSubstring(String s) {
    
     if(s.isEmpty()){
        return 0;
     }
      // S list로 쪼개기
      ArrayDeque<String> SDeque = new ArrayDeque<>(List.of(s.split("")));
      System.out.println(SDeque.size());
      // 현재값 저장 
      ArrayDeque<String> now = new ArrayDeque<>();

      // 결과
      int result = 0;

      for(String i: SDeque){
        System.out.println(i);

        if(now.contains(i)){
            int idx = new ArrayList<>(now).indexOf(i);
            int end  = now.size();

            for (int k = 0; k < idx+1; k++){
                now.pollFirst();
                System.out.println("제대로 나오나"+now.size());
            }
            now.addLast(i);
        }
        else {
            System.out.println("이거");
            now.addLast(i);
            result = Math.max(result,now.size());
            System.out.println(result);
        }
        
      }

      return result;
    }
}


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
