#Course: CSCI 4140
#Name: Huan-Yun Chen
#Date: 2/6/2018
#Tabs: 8

'''
1:[a-zA-Z]+ : range of lower case a to z and capital A to Z, at least one or more
2:[A-Z][a-z]* : range of captial A to Z and other set of lower case a to z
3:p[aeiou]{,2}t : a character p, with one of the character in set[aeiou], at least 2 characters repeat, and last character t
4:\d+(\.\d+)? : any decimal digits a period after and other any decimal digits
5:([^aeiou][aeiou][^aeiou])* :match a pattern either none or more that other than one of the character in the set[aeiou] and match with the other [aeiou] and another patter that other than the same set of character
6:\w+|[^\w\s]+ : a pattern that has either one or more that start with any alphanumeric character with either another set of alphanumeric character of whitespace character
'''
