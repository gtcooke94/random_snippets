#include <vector>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int start = 0;
        int len_nums = nums.size();
        int total_counted = 0;
        int cur_idx = start;
        int next_idx = (cur_idx + k) % len_nums;
        int hold = nums[cur_idx];
        while (total_counted < len_nums) {
            while (true) {
                next_idx = (cur_idx + k) % len_nums;

                int temp_hold = nums[next_idx];
                nums[next_idx] = hold;
                hold = temp_hold;
                cur_idx = next_idx;
                total_counted++;
                /*
                for (auto i : nums) {
                    std::cout << i << " ";   
                }
                std:: cout << "\n";*/
                if (start == next_idx) {
                    break;   
                }
            }
            start++;
            cur_idx = start;
            hold = nums[cur_idx];
        }
    }
};
