
def rabbits_and_recurrence(n, k):

    """
    Given: Positive integers n≤40 and k≤5.
    Return: The total number of rabbit pairs that will be present after n months, 
    if we begin with 1 pair and in each generation, every pair of reproduction-age 
    rabbits produces a litter of krabbit pairs (instead of only 1 pair).
    """

    # Base
    if n == 1:
        return 1
    elif n == 2:
        return 1
    
    #initialize the first two months
    previous = 1
    current = 1

    # For each month 𝑛≥3, the recurrence relation:
    # 𝐹(𝑛)=𝐹(𝑛−1)+𝑘⋅𝐹(𝑛−2)
    for i in range(3, n+1):
        next_value = current + k*previous
        previous = current
        current = next_value
    return current
    

