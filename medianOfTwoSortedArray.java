package TIL_Today_I_Leared;

import java.util.List;
import java.util.stream.Stream;



class medianOfTwoSortedArray{
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // List<String> list = new ArrayList<>(Arrays.asList(arr));
        // List<Integer> nums1List = Arrays.stream(nums1).boxed().toList();
        // 컴파일 에러 발생
        // Integer[] nums1 = nums1
        
        List<Integer> nums1List = new Array.stream(nums1).boxed().toList();
        List<Integer> nums2List = new ArrayList<>(Arrays.asList(nums2));

        List<Integer> combined = Stream.concat(nums1List.stream(),nums2List.stream()).toList();
        System.out.println(combined);
             
    }
}

