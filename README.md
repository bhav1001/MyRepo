-> The WaterJug problem include 2 Jugs of different capacities(given) trying to acheive a "Desired capacity"(given) in one of the two Jugs, where there's unlimited supply of water.
-> The solution is only Possible if either one of the capacities of the two jugs are less than the desired and the remainder of desired capacity when divided with gcd of the two jug capacities is ZERO 

In this ALgorithm, We start from the first Jug 
-> **ALGORITHM** :
      Initialise Step to 0, increment it every time you pour water in or out the Jugs (you can print the Steps)
	
      step 1 : Take the inputs Jug1 capacity(j1) Jug2 capacity(j2) and desired quantity(d)
                Check whether the problem is Solvzable or not if yes _continue_ else print 'No Solution'
      step 2: Operations to be Performed
              (i) Fill the J2 litre jug and empty it into J1 liter jug.
              (ii)  Whenever the J2 liter jug becomes empty fill it.
              (iii) Whenever the J1 liter jug becomes full empty it.
                  Repeat steps 1,2,3 till either J1 liter jug or the J2 liter jug contains d litres of water.
        step 3: Use a Loop and perform the steps until Desired Output is available in either of the two Jugs.

There are other approaches also available.
# MyRepo
