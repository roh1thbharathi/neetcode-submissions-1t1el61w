class Solution {
public:
    bool isAnagram(string s, string t) 
    {
        unordered_map<int , int> val;
        if(s.size()!=t.size())
        {
            return false;
        }
        for (auto i : s)
        {
            val[i]++;
        }
        for(auto i : t)
        {
            val[i]--;
        }
        for (auto i :val)
        {
            if(i.second)
            {
                return false;
            }
        }
        return true;
    }
};
