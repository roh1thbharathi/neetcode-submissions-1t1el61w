class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> mp ;
        vector<int> sol;
        for(int i= 0;i<nums.size();i++)
        {
            int diff=target-nums[i];
            if(mp.find(diff)!=mp.end())
            {
                // sol.push_back(i);
                sol.push_back(mp[diff]);
                sol.push_back(i);
                return sol;
            }
            else
            {
                mp[nums[i]]=i;
            }
        }
        return sol;
    }
};
