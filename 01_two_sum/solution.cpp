class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> maps;
        for( int i = 0; i<= nums.size(); i++) {
            int checker = target - nums[i];
            if(maps.find(checker) != maps.end()) {
                return {maps[checker], i};
            }
            maps[nums[i]] = i;
        }
        return {};
    }
};