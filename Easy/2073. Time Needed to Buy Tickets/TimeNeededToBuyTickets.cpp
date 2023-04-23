class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {

        cout <<tickets.size();

        bool all_zero = 0;
        int result = 0;

        while (!all_zero){
            all_zero = true;
            for (int i = 0; i < tickets.size(); i++){
                if (tickets[i] > 0){
                    result++;
                    tickets[i]--;
                    all_zero = false;
                }
                if (tickets[i] == 0 and i == k){
                    return result;
                }
            }
        }

        return result;
    }
};