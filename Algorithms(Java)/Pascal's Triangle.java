class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans=new ArrayList<>();
        List<Integer> temp= new ArrayList<>();
        temp.add(1);
        ans.add(temp);
        if (numRows==1)
            return ans;
        temp=new ArrayList<>();
        temp.add(1);temp.add(1);
        ans.add(temp);
        if (numRows==2)
            return ans;
        for(int n=2;n<numRows;n++){
            List<Integer> row= new ArrayList<>();
            row.add(1);
            for(int j=1;j<=n;j++){
                row.add((row.get(j-1)*(n-(j-1)))/j);
            }
            ans.add(row);
        }
        return ans; 
    }
}