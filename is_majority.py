def is_majority(bools: list )-> bool:
    
    Tru = "True"
    True_sum = 0
    False_sum = 0

    for Tru in bools:
        if Tru:
            True_sum += 1
        else:
            False_sum += 1
#Right above we use this for loop to analyze each element in the list and if it's true it will add 1 score to the true otherwise,
  #it'll add to false score and the one with the highest score will have either True or Returned based on which score is greater.
    if True_sum > False_sum:
        return True
    else:
        return False
