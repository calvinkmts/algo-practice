import java.util.Arrays;
import java.util.HashMap;
import java.util.Hashtable;

public class TwoSum {

    public static int[] twoSum(int[] nums, int target) {

        int[] result = new int[2];
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        for (int i=0; i<nums.length; i++) {
            if (hashMap.get(nums[i]) == null) {
                hashMap.put(target - nums[i], i);
            } else {
                result[0] = hashMap.get(nums[i]);
                result[1] = i;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(twoSum(new int[] {2, 7, 11, 15}, 9)));
    }
}
