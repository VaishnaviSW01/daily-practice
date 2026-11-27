class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        dp = [0]*(budget + 1)
        min_price = float('inf')

        for factor, price in items:
            min_price = min(min_price, price)
            count = 0
            
            for factor_j , _ in items:
                if factor_j % factor ==0:
                    count +=1
                
            for j in range (budget, price -1, -1):
                dp[j] = max(dp[j],dp[j - price]+ count)

        answer = 0

        for j in range(budget + 1):
            extra = (budget - j) // min_price
            answer = max(answer , dp[j] + extra)
        return answer
