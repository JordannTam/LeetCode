import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        int arr[] = new int[2];
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++) {
            Integer mapIndex = map.get(target - nums[i]);
            if (mapIndex != null && mapIndex != i) {
                arr[0] = i;
                arr[1] = map.get(target - nums[i]);
                break;
            }
        }
        return arr;
    }
}