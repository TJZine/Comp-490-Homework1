# Comp-490-Homework1 Tristan Zine

My production function is called cart_total, and takes a list of the dataclass CartItem, and a state. It first checks for 
a valid state as input, the runs through all the items in the cart tallying the total, and total for clothing purchased from
MA to account for the 175 limit for nontaxable clothing purchases. It then uses several helper functions to calculate the tax
for the items based on the type of item, and the state input. The tests can all be run individually within pycharm with the pytest
package installed or I have it set up to run everytime code is pushed to github and can also run the tests that way.
