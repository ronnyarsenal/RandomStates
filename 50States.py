__author__ = 'ron'
import random as randomnumber 
#imports random module functions as an object

#the states are in the order of joining the states
UnitedStates = {1:"Delaware",2:"Pennsylvania",3:"New Jersey",4:"Georgia",
                5:"Connecticut",6:"Massachusetts",7:"Maryland",8:"South Carolina",
                9:"New Hampshire",10:"Virginia",11:"New York",12:"North Carolina",
                13:"Rhode Island",14:"Vermont",15:"Kentucky",16:"Tennessee",
                17:"Ohio",18:"Louisiana",19:"Indiana",20:"Mississippi",
                21:"Illinois",22:"Alabama",23:"Maine",24:"Missouri",
                25:"Arkansas",26:"Michigan",27:"Florida",28:"Texas",
                29:"Iowa",30:"Wisconsin",31:"California",32:"Minnesota",
                33:"Oregon",34:"Kansas",35:"West Virginia",36:"Nevada",
                37:"Nebraska",38:"Colorado",39:"North Dakota",40:"South Dakota",
                41:"Montana",42:"Washington",43:"Idaho",44:"Wyoming",
                45:"Utah",46:"Oklahoma",47:"New Mexico",48:"Arizona",
                49:"Alaska",50:"Hawaii"}

FindStates = randomnumber.randint(1,50)
#sets generated value with the range of 1 to 50 to FindStates.

print("Your random state is: " + UnitedStates[FindStates]) 
# prints state that has the key value
