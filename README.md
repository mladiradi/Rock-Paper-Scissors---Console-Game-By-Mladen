# Rock-Paper-Scissors---Console-Game

**Description and rules of the game:**

      • Project title (should answer the question "What's inside this project) 
      • Project goals (what problem do we solve, e. g. we implement a certain game) 
      • Solution (should describe how we solve the problem → algorithms, technologies, libraries, frameworks, tools, etc.) 
      • Source code link (give a direct link to your source code) 
      • Screenshots (add screenshots from your project in different scenarios of its usage) 
      • Live demo (add a one-click live demo of your code)


## **Implement the Game Logic** 

### Read Player's Move 
Now let's start working on our code. 
Create three variables for our "Rock", "Paper", and "Scissors", which we will use later. They should look like this: 

Next, write on the console what options ("r" for "rock", "p" for "paper", and "s" for "scissors") the player can choose 
from and read his input data. You already know how to do this: 

Now let's run the app in the console and check whether our current code works properly: 

We can see that we have our text written on the console, and we can also write. 

Match Player's Move with Possible Options 
Now it is time to turn the user input into one of our player's moves options. To do this, create an if-else 
statement with the possible moves and change the player_move variable value with the value it represents. 
First, if the user has entered "r", they chose "Rock". Write it like this:

And if they have entered "p" or "s", then they chose "Paper" or "Scissors" accordingly. Write the else-if 
statements by yourself: 

Now we should cover the case, in which the user enters an invalid value. To do this, use else and raise 
SystemExit with a message on the console to stop the program from executing: 

Note: "raise SystemExit" is an exception, for now, all you need to know is that it exits the whole program. 
Now let's run the app in the console and check whether our current code works properly, at the moment we have 
logic only for the incorrect input so the results should be as follows:  

### **Choose Computer's Move**
Create a variable of type Random that will help us choose a random number using the randint method. We will 
use this number so that the computer can randomly select from "rock", "paper", or "scissors": 

Note: "randint()" is a method from the build-in library - "random" in Python (like the "math" library that you 
should know from the "Programming Basics" course). "randint()" accepts two parameters, both inclusive, and 
returns a random number in this range. For more clarification see these examples here. 
We will need a variable of type string to keep track of our computer's movement: 

Choose the computer's random move, to make this happen use the conditional statements if-else.

Think about how you can complete these conditional statements. 


### **Check and Write the Result** 
Write to the console what is the random selection of the computer e.g., "The computer chose 
{computer_move}.". Now we need to compare the choice of the player and the computer, again using 
conditional statements. 

You can use this table for the possible moves:

Consider all the cases where the player loses or the result between them is equal and write down the conditional 
statements. That's all it takes for the game to work.


After you run it, the game should look like this:


### **Modify the Code, Write Your Own Features**

Restart the Game 
You can automatically restart the game after it is finished (or ask the player to play again).


## **Attached source PDF file:**
[01-Rock-Paper-Scissors-Project-Description..pdf](https://github.com/mladiradi/Rock-Paper-Scissors---Console-Game-By-Mladen/files/15485912/01-Rock-Paper-Scissors-Project-Description.pdf)


* *...the readme file is under construction...*
