class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int left = 1;
        vector<int>res;
        for (auto& num : nums){
            res.push_back(left);
            left *= num;
        }
        int right = 1;
        for (int i = nums.size()-1; i>=0; i--){
            res[i] *= right;
            right *= nums[i];
        }

        return res;
    }
};