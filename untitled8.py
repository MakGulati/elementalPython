def create_cast_list(filename):
    cast_list = []
    with open(filename,"r+") as f:
        for line in f:
            line.split()
            line=line.split()[0]+" "+line.split()[1]
            line=line.strip()
            cast_list.append(line.strip(","))
            
        
        #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list

    return cast_list
    
    
print(create_cast_list("flying_circus.txt"))