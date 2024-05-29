# Rock-Paper-Scissors---Console-Game-By-Mladen
Mladen's part of console game - Rock Paper Scissors

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

![image](https://github.com/mladiradi/Rock-Paper-Scissors---Console-Game-By-Mladen/assets/100635431/44abe86c-2e1e-4701-b94d-7d5715a4ed61)

Next, write on the console what options ("r" for "rock", "p" for "paper", and "s" for "scissors") the player can choose 
from and read his input data. You already know how to do this: 

![image](https://github.com/mladiradi/Rock-Paper-Scissors---Console-Game-By-Mladen/assets/100635431/f2d2eedf-8a72-4672-a2b7-b84b0d6fc31d)

Now let's run the app in the console and check whether our current code works properly: 

![Екранна снимка 2024-05-29 172137](https://github.com/mladiradi/Rock-Paper-Scissors---Console-Game-By-Mladen/assets/100635431/30866dda-9b38-4fc8-a0c9-7a74485fd669)

We can see that we have our text written on the console, and we can also write. 

Match Player's Move with Possible Options 
Now it is time to turn the user input into one of our player's moves options. To do this, create an if-else 
statement with the possible moves and change the player_move variable value with the value it represents. 
First, if the user has entered "r", they chose "Rock". Write it like this:

![image](https://github.com/mladiradi/Rock-Paper-Scissors---Console-Game-By-Mladen/assets/100635431/0a190d15-6c6a-493f-b47f-408bb9335847)

And if they have entered "p" or "s", then they chose "Paper" or "Scissors" accordingly. Write the else-if 
statements by yourself: 

![image](https://github.com/mladiradi/Rock-Paper-Scissors---Console-Game-By-Mladen/assets/100635431/36b82971-dd00-4fd8-8fd5-c7bc1396b6cc)

Now we should cover the case, in which the user enters an invalid value. To do this, use else and raise 
SystemExit with a message on the console to stop the program from executing: 

![image](https://github.com/mladiradi/Rock-Paper-Scissors---Console-Game-By-Mladen/assets/100635431/36a36369-9c97-472d-9661-eafc2fb0eabd)

Note: "raise SystemExit" is an exception, for now, all you need to know is that it exits the whole program. 
Now let's run the app in the console and check whether our current code works properly, at the moment we have 
logic only for the incorrect input so the results should be as follows:  

![image](https://github.com/mladiradi/Rock-Paper-Scissors---Console-Game-By-Mladen/assets/100635431/2baede38-8357-4514-a221-a3d00b828d15)

### **Choose Computer's Move**
Create a variable of type Random that will help us choose a random number using the randint method. We will 
use this number so that the computer can randomly select from "rock", "paper", or "scissors": 

![image](https://github.com/mladiradi/Rock-Paper-Scissors---Console-Game-By-Mladen/assets/100635431/3ae07590-201b-4b1a-9529-c3743baa494e)

Note: "randint()" is a method from the build-in library - "random" in Python (like the "math" library that you 
should know from the "Programming Basics" course). "randint()" accepts two parameters, both inclusive, and 
returns a random number in this range. For more clarification see these examples here. 
We will need a variable of type string to keep track of our computer's movement: 

![image](https://github.com/mladiradi/Rock-Paper-Scissors---Console-Game-By-Mladen/assets/100635431/330e4fbe-a5c0-455d-9141-8bcafa6b9a1f)

Choose the computer's random move, to make this happen use the conditional statements if-else.

![image](https://github.com/mladiradi/Rock-Paper-Scissors---Console-Game-By-Mladen/assets/100635431/1ff13555-2964-44ac-83c8-d7818e75a0f3)

Think about how you can complete these conditional statements. 


### **Check and Write the Result** 
Write to the console what is the random selection of the computer e.g., "The computer chose 
{computer_move}.". Now we need to compare the choice of the player and the computer, again using 
conditional statements. 

![image](https://github.com/mladiradi/Rock-Paper-Scissors---Console-Game-By-Mladen/assets/100635431/df0245eb-8bd9-48ec-9b89-12a23bf24235)

You can use this table for the possible moves:

![image](https://github.com/mladiradi/Rock-Paper-Scissors---Console-Game-By-Mladen/assets/100635431/2feeb2fa-0b47-478d-8272-0e043edc9090)

Consider all the cases where the player loses or the result between them is equal and write down the conditional 
statements. That's all it takes for the game to work.

![image](https://github.com/mladiradi/Rock-Paper-Scissors---Console-Game-By-Mladen/assets/100635431/c8d281bf-713b-4cae-8b4f-6624e2795a8f)

After you run it, the game should look like this:

![image](https://github.com/mladiradi/Rock-Paper-Scissors---Console-Game-By-Mladen/assets/100635431/1df2ed07-596b-4fd0-b6e9-6bd124e6e072)


### **Modify the Code, Write Your Own Features**

Restart the Game 
You can automatically restart the game after it is finished (or ask the player to play again).

![image](https://github.com/mladiradi/Rock-Paper-Scissors---Console-Game-By-Mladen/assets/100635431/43762c8a-6cdb-4cdb-be57-ba3547efb672)


## **Attached source PDF file:**
[01-Rock-Paper-Scissors-Project-Description..pdf](https://github.com/mladiradi/Rock-Paper-Scissors---Console-Game-By-Mladen/files/15485912/01-Rock-Paper-Scissors-Project-Description.pdf)


* *...the readme file is under construction...* *
