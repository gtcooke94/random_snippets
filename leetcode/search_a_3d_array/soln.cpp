#include <vector>

using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.size() == 0 || matrix[0].size() == 0) {
            return false;
        }
        vector<int> first_column;
        for (auto row: matrix) {
            first_column.push_back(row[0]);
        }
        auto row_it = std::upper_bound(first_column.begin(), first_column.end(), target);
        if (row_it <= first_column.begin()) {
            return false;
        }
        int row_idx = row_it - first_column.begin() - 1;
        vector<int>& row = matrix[row_idx];
        return std::binary_search(row.begin(), row.end(), target);
    }
};
