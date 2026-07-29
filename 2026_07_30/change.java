import java.util.List;
import java.util.ArrayList;

class change {
    public int[] solution(int[] num_list, int n) {
        int[] answer = new int[n];
        int length = num_list.length;
            
        List<Integer> result = new ArrayList<>();
        
        
        for(int i = n; i< length; i++){
            result.add(num_list[i]);
        }
        
        for (int j=0; j<n; j++){
            result.add(num_list[j]);
        }
        
        
        for(int k=0; k<n; k++){
            answer[k] = result.get(k);
            
        }
        
        return answer;
    }
}