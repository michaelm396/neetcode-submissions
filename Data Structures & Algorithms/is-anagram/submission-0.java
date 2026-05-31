
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        Map<Character,Integer> s1 = new HashMap<>();
        Map<Character,Integer> t1 = new HashMap<>();

        for (char x : s.toCharArray()){
            s1.put(x, s1.getOrDefault(x, 0) + 1);
        }
        for (char x : t.toCharArray()){
            t1.put(x, t1.getOrDefault(x, 0) + 1);
        }
        if (s1.equals(t1)){
            return true;
        }
        else{
            return false;
        }
    
    }
}

        
        
