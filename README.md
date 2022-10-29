# TDC
A beta version of a python program for generating TDC (Tour De Chambre) room pairings and room order.

## How it works.
The program starts by creating pairs of newbies and oldies while there are rooms left to create.  
After this have been done:  
  If there are still oldies left, and no newbies, and rooms left to create, it creates pairs of oldies.  
  If there are still newbies left, and no oldies,and rooms left to create it creates pairs of oldies.
  
 When all the rooms have been created, it randomly, and evenly, assigns the remaining oldies and newbies to said rooms.
 
 ## Program requirements
 The program creates minimum pairings of two, and therefore requires that: nbrOfParticipants >= self.nbrOfRooms*2
 
 ## Testing
 The program has been tested for different variants of the test lists that are included in the file.
 There may be edge cases that haven't been caught but the program seems to be working according to desired functionality.
 
## Installation and how to use.
1. Install python
2. Clone the repo
3. open tdcGenerator.py with an editor
4. Create a list of oldies and newbies (see test lists for inspiration) and set number of rooms.
5. write: <python3 tdcGenerator.py> in terminal while being in folder where the repo was cloned.
