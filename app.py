import json

# Open json updates file
with open('forwarder_updates.json', encoding='utf-8') as f:
    updates = json.load(f)


# Function to filter updates data for FunBet customers
def fun_bet():
    # Loop through updates to find all updates for Fun Bet Customer.
    # Excluding all updates for the 'SerieA' competition.
    for update in updates:
        if update['Competition'] != 'SerieA':
            print(update)


# fun_bet()


# Function to filter updates to find all updates in the 'SerieA' competition
def crazy_bet():
    # Loop through updates to find updates from the SerieA competition only.
    for update in updates:
        if update['Competition'] == 'SerieA':
            print(update)


# crazy_bet()


# Function to find the updates for the Lucky Bet customer
def lucky_bet():
    # Loop through updates to exclude all Premier League competition updates.
    for update in updates:
        if update['Competition'] != 'PremierLeague':
            # Find updates within the filtered data
            # Where probability is higher than 0.25
            if update['Probability'] >= 0.25:
                print(update)


lucky_bet()
