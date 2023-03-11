#!/bin/python3

#LISTS - Have brackets []
#List are changablevdata structures (items)

movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[1]) #returns the second item in the list

print(movies[0]) #returns the first item in the list

print(movies[1:3]) #returns the first indexed number but not the last number indicated. 1st and 2nd only

print(movies[1:]) #start at a certain index and print the rest 

print(movies[:1]) #stops at the index entered

print(movies[-1]) # returns the last in the list

print(len(movies)) #count items in the list

movies.append("JAWS") #adds to the end of the list

print(movies)

movies.insert(2,"Hustle") #adds items in specific location

print(movies)


movies.pop() #remove the last item
print(movies)

movies.pop(0) #remove the first item
print(movies)

#new list to appened with another
amber_movies = ["Just Go With It", "50 FIrst Dates"]

#append 2 list
our_favorite_movies = movies + amber_movies
print(our_favorite_movies)


grades = [["Bob",82], ["Alice",90], ["Jeff",73]]

bobs_grade = grades[0][1] #selects the 0 item on the list but with in the 0 item it will select the 1 item

print(bobs_grade)

grades[0][1] = 83 #modify the list

print(grades)

#.pop, .append, .insert used 

#Thank You TCM Security