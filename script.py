from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        solution = ""
        resL = 0
    
        for i in range(len(s)):
            # Odd length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resL:
                    solution = s[l:r+1]
                    resL = r - l + 1
                
                l -= 1
                r += 1
            # Even length palindrome
            l, r = i, i + 1 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resL:
                    solution = s[l:r+1]
                    resL = r - l + 1
                
                l -= 1
                r += 1
            
        return solution 

def main():
    """Проверка алгоритма"""
    input = "cbbd"
    S = Solution()
    print(S.longestPalindrome(input))

    input = "babad"

    S = Solution()
    print(S.longestPalindrome(input))

    input = "aba"

    S = Solution()
    print(S.longestPalindrome(input))


if __name__ == "__main__":
    main()