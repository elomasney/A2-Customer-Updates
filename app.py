import json

# Open json updates file
with open('forwarder_updates.json', encoding='utf-8') as f:
    updates = json.load(f)


# Function to filter updates data for FunBet customers
def fun_bet():
    fun_bet_updates = []
    # Loop through updates to find all updates for Fun Bet Customer.
    # Excluding all updates for the 'PlayerProps' update type.
    for update in updates:
        if update['UpdateType'] != 'PlayerProps':
            fun_bet_updates.append(update)
            with open("fun_bet.json", "w", encoding='utf-8') as file:
                json.dump(fun_bet_updates, file, indent=4)


fun_bet()


# Function to filter updates to find all updates in the 'SerieA' competition
def crazy_bet():
    crazy_bet_updates = []
    # Loop through updates to find updates from the SerieA competition only.
    for update in updates:
        if update['Competition'] == 'SerieA':
            crazy_bet_updates.append(update)
            with open("crazy_bet.json", "w", encoding='utf-8') as file:
                json.dump(crazy_bet_updates, file, indent=4)


crazy_bet()


# Function to find the updates for the Lucky Bet customer
def lucky_bet():
    lucky_bet_updates = []
    # Loop through updates to exclude all Premier League competition updates.
    for update in updates:
        if update['Competition'] != 'PremierLeague':
            # Find updates within the filtered data
            # Where probability is higher than 0.25
            if update['Probability'] >= 0.25:
                lucky_bet_updates.append(update)
                with open("lucky_bet.json", "w", encoding='utf-8') as file:
                    json.dump(lucky_bet_updates, file, indent=4)


lucky_bet()
