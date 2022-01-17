# Algorithm s = 1/1 + 1/2 + 1/3 + 1/4 + ... + 1 / N


number = int(input('Please enter your nubmer'))

sum , The_first_sentence_ofthe_sequence = 0 , 1 

while The_first_sentence_ofthe_sequence <= number : 
    
    sum += (1/The_first_sentence_ofthe_sequence)
    
    The_first_sentence_ofthe_sequence += 1 
    
print(f'Sum : {sum}')