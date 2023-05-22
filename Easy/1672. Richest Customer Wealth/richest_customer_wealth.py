class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_money = 0
        for account in accounts:
            max_money = max(sum(account), max_money)
        
        return max_money 
