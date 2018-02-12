 # Define the remove_duplicates function
def remove_duplicates(countries):
    final_countries=[]
    for country in countries:
        if country not in final_countries:
            
            final_countries.append(country)
            
    return (final_countries)   

f=["dnwjdn","wdniw","diwew","abc","abc","wdniw"]

print(remove_duplicates(f))
f_set=set(f)   #remove repetitations without order pop and add works but not append
print(f_set)  
f_set.pop()    # random element delection
print(f_set)
f_set.add("abcd")
print(f_set)