class Solution {
    public int solution(int[][] sizes) {
        int w = 0;
        int h = 0;
        for (int i=0; i<sizes.length; i++){
            int posW = Math.max(sizes[i][0], sizes[i][1]);
            int posH = Math.min(sizes[i][0], sizes[i][1]);
            w = Math.max(posW, w);
            h = Math.max(posH, h);
            // System.out.println(w);
            // System.out.println(h);
            
        }
        return w*h;
    }
}