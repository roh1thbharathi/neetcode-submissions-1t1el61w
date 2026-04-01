class Solution {
public:
    bool hasDuplicate(vector<int>& nums) 
    {   
        unordered_map<int , int> val;
        for(auto i :nums)
        {
            val[i]++;
        }
        for(auto i : val)
        {
            if(i.second>1)
            {
                return true;
            }
        }
        return false;
    }
};
