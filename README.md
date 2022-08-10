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

- First the json file data was loaded containing all customer updates and then printed to the console to test if I could access this data and that all the necessary data was available.
- To solve the problem, three functions were created, one for each Customer type. Within each function a for loop was used to iterate through the updates data. Then, using an if statement the data was filtered to access the relevant data for each customer based on the contract criteria.
- When all the relevant data was retrieved for each customer type, the resulting data was written to a json file, one file for each customer type. This file only contains the update messages relevant to each customer.
- When attempting to write the output to a json file, an issue was encountered where only the last iteration of the loop was being written to the json file. After conducting some research, the problem was identified, the json file was being overwritten after each iteration. To resolve this issue, a variable was declared as a list and then each iteration update value was appended to this list. The resulting data was then written to the json file. This solved the issue, and a separate json file for each customer was created. These json files include the updates relevant to each customer type based on the contract criteria provided.
- The testing for this application was done using manual testing. The code was printed to the console to check if the correct data was being displayed.

### Future Improements
- A database could be created using MongoDb to store the Customer updates data. As there could be a high number of customer types and related updates, a database would allow for a higher amount of data to be stored, managed and queried easily, while also allowing for any sensitive data to be stored securely.
- Implement some automated tests using the Python built in unit testing framework unittest to test each function.