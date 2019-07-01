def fizzBuzz(self, n: int) -> List[str]:
    answer = []
    
    for current_num in range(1, n+1):
        temp = ''
        
        if current_num % 3 == 0:
            temp += 'Fizz'
        if current_num % 5 == 0:
            temp += 'Buzz'
        if temp == '':
            temp += str(current_num)
            
        answer.append(temp)
        
    return answer