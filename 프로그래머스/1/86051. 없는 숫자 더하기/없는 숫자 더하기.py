def solution(numbers):
    full_set={0,1,2,3,4,5,6,7,8,9}
    numbers=set(numbers)
    answer_set=full_set-numbers
    ans=sum(answer_set)
    return ans