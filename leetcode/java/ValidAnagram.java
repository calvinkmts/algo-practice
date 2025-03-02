import java.util.HashMap;

public class ValidAnagram {

    public static boolean isAnagram(String s, String t) {

        HashMap<Character, Integer> hashMapS = new HashMap<Character, Integer>();
        for (int i=0; i<s.length(); i++) {
            if (hashMapS.get(s.charAt(i)) == null) {
                hashMapS.put(s.charAt(i), 1);
            } else {
                hashMapS.put(s.charAt(i), hashMapS.get(s.charAt(i))+1);
            }
        }

        HashMap<Character, Integer> hashMapT = new HashMap<Character, Integer>();
        for (int i=0; i<t.length(); i++) {
            if (hashMapT.get(t.charAt(i)) == null) {
                hashMapT.put(t.charAt(i), 1);
            } else {
                hashMapT.put(t.charAt(i), hashMapT.get(t.charAt(i))+1);
            }
        }

        return hashMapS.equals(hashMapT);

    }

    public static void main(String[] args) {

        System.out.println(isAnagram("car", "cat"));
    }
}
