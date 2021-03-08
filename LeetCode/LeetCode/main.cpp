#include <vector>
#include <string>
#include "iostream"
#include <sstream>

using namespace std;


class Solution {
public:
    int longestOnes(vector<int>& A, int K) {
        int zero_cnt=0;
        int left=0,right=0;
        int max=INT_MIN;
        while(right<A.size()){
            int c=A[right];
            right++;
            if(c==0){
                zero_cnt++;
            }
            while(zero_cnt>K){
                int d=A[left];
                if(d==0) zero_cnt--;
                left++;
            }
            if(right-left>max)
                max=right-left;
        }
        return max;
    }
};
    
int main() {
    int K = 2;
    vector<int> A = {0,1,1,1,0,0,0,1,1,1,1,0};
    int ret = Solution().longestOnes(A, K);

    string out = to_string(ret);
    cout << out << endl;
    return 0;
}
