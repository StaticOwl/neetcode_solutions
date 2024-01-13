class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> dict = {};
        for (int i=0; i<nums.size(); i++){
            if(auto search = dict.find(nums[i]); search == dict.end()){
                dict.insert(make_pair(target-nums[i], i));
            }
            else{
                return {search->second, i};
            }
        }
        return {};
    }
};