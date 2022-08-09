## Customer Updates - Assignment

- The objective of this assignment was to filter json data (Customer Updates) based on three types of Customer Contracts:
    - FunBet
    - CrazyBet
    - LuckyBet

- The FunBet criteria was to retrieve all customer updates for this contract and exclude any updates related to the SerieA competition.
- The CrazyBet criteria was to retrieve only customer updates related to the SerieA competition
- The LuckyBet criteria was to retrieve all updates that would exclude any updates related to the Premier League competition and only include updates that had a probability greater than 0.25.

- First I loaded the data containing all customer updates and tested to see if I could access this data.
- I then created 3 functions, one for each Customer type and filtered the relevant data.
- When all the relevant data was retrieved for each customer type, I then created a separate json file for each customer that included all the updates relevant to their customer contract.