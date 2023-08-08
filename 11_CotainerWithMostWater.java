class Solution {
    public int maxArea(int[] height) {

        int l = 0;
        int r = height.length - 1;
        int maxArea = Integer.MIN_VALUE;
        int areaHeight = 0;

        while (l <= r) {
            areaHeight = Math.min(height[l], height[r]);
            if (areaHeight * (r - l) > maxArea) {
                maxArea = areaHeight * (r - l);
            }
            if (height[l] > height[r]) {
                r--;
            } else {
                l++;
            }
        }

        return maxArea;
    }
}