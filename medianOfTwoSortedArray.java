// 출처:출처: https://leetcode.com/problems/median-of-two-sorted-arrays/
package TIL_Today_I_Leared;

import java.util.List;
import java.util.stream.Stream;
import java.util.List;
import java.util.stream.Stream;



class medianOfTwoSortedArray {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // List<String> list = new ArrayList<>(Arrays.asList(arr));
        // List<Integer> nums1List = Arrays.stream(nums1).boxed().toList();

        List<Integer> nums1List = new ArrayList<>(Arrays.stream(nums1).boxed().toList());
        // List<Integer> nums1List = new ArrayList<>(Arrays.asList(nums1));
        List<Integer> nums2List = new ArrayList<>(Arrays.stream(nums2).boxed().toList());

        List<Integer> combined = new ArrayList<>(Stream.concat(nums1List.stream(),nums2List.stream()).toList());
        System.out.println(combined);
        System.out.println( combined.size() );
        combined.sort(null);


        if(combined.size()%2==1){
            int num = combined.size()/2;
            return combined.get(num);
        }
        else{
            // System.out.println("여기");
            int num2 = combined.size()/2;
            double result = (double)( combined.get(num2-1)+combined.get(num2) ) /2;
            System.out.println(combined.get(num2));
            return result;
        }
        
    }
}

