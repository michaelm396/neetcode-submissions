class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> prevMap = new HashMap<>();
        int index = 0;
        for (int num : nums){
            int diff = target - num;
            if (prevMap.containsKey(diff)){
                return new int[] { prevMap.get(diff), index };
            }
            prevMap.put(num,index);
            index ++;
        }
        //System.out.println(prevMap);
        return new int[] {};
    }
}
