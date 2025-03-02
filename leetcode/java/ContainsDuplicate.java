import java.util.HashSet;

public class ContainsDuplicate {

    public static boolean containsDuplicate(int[] nums) {

        boolean isAllNumberUnique = true;
        HashSet<Integer> uniqueNumbers = new HashSet<Integer>();
        for (int i=0; i<nums.length; i++) {
            if (uniqueNumbers.contains(nums[i])) {
                isAllNumberUnique = false;
                break;
            }

            uniqueNumbers.add(nums[i]);
        }

        return !isAllNumberUnique;
    }

    public static void main(String[] args) {
        System.out.println(containsDuplicate(new int[]{1, 2, 3, 1}));
    }
}
