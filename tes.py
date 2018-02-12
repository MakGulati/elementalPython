    results= [None, None, None, None, None]
    i=0
    while(i<len(results)):
        if my_answers[i] == answers[i]:
            results[i] = True
        elif my_answers[i] != answers[i]:
            results[i] = False
        i+=1
    

        
        