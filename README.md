## Customer Updates - Assignment

### Programming Language:
- Python

### Project Objective
- The objective of this assignment was to filter json data (Customer Updates) based on three types of Customers:
    - FunBet
    - CrazyBet
    - LuckyBet

### Project Breakdown
- The FunBet criteria was to retrieve all customer updates for this contract and exclude any updates related to the PlayerProps update type.
- The CrazyBet criteria was to retrieve only customer updates related to the SerieA competition
- The LuckyBet criteria was to retrieve all updates that would exclude any updates related to the Premier League competition and only include updates that had a probability greater than 0.25.

- First I loaded the data containing all customer updates and printed the loaded data to the console to test if I could access this data and that all the necessary data was available.
- I then created three functions, one for each Customer type and used a for loop to iterate through the updates data. Then, using an if statement I was able to filter the relevant data for each customer based on the contract criteria.
- When all the relevant data was retrieved for each customer type, the resulting data was written to a json file, one file for each customer type. This file only contains the update messages relevant to each customer.
- When I attempted to write the output to a json file, I encountered an issue, it was only writing the last iteration of the loop to the json file. I did some research to identify the problem, and figured out that it was overwriting after each iteration. To resolve this issue I decided to declare a variable as a list and then append the iteration update values to this list. The resulting data was then written to the json file. This solved the issue, and I was able to create a separate json file for each customer that included all the updates relevant to the customer based on the contract criteria provided.
