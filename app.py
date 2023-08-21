class Solution(object):
    def reduce_to_zero(num: int) -> int:
        print(f'Input: num = {num}')

        explanation = []
        steps = 0

        while num > 0:
            if num % 2 == 0:
                explanation.append(f'Step {steps}) {num} is even; divide by 2 and obtain {num//2}.') 
                num //= 2
                
            else:
                explanation.append(f'Step {steps}) {num} is odd;  subtract 1 and obtain {num-1}.') 
                num -= 1
            steps += 1

        print(f'Output: {steps}')
        print(f'Explanation: ')
        for i in explanation:
            print(i)
        return steps


if __name__ == "__main__":
    Solution.reduce_to_zero(22)