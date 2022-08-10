""" Reads json file data and filters this data
    for each customer type based on contract criteria.
    Saves filtered data as new json files.
"""
import json

# Open and load json forwarder_updates file
with open('forwarder_updates.json', encoding='utf-8') as f:
    updates = json.load(f)


def fun_bet():
    """ Function that filters data from updates file
    based on the FunBet customer contract.
    Saves the filtered data to a new json file.
    """
    fun_bet_updates = []
    # Loop through all updates in forwarder_updates data.
    for update in updates:
        # Exclude all updates for the 'PlayerProps' update type.
        if update['UpdateType'] != 'PlayerProps':
            # Append each matching update to the fun_bet_updates list
            fun_bet_updates.append(update)
            # Write filtered data list to new json file
            with open("fun_bet.json", "w", encoding='utf-8') as file:
                json.dump(fun_bet_updates, file, indent=4)


fun_bet()


def crazy_bet():
    """ Function that filters data from updates file
    based on the CrazyBet customer contract.
    Saves the filtered data to a new json file.
    """
    crazy_bet_updates = []
    # Loop through all updates in forwarder_updates data.
    for update in updates:
        # Find updates from the SerieA competition only.
        if update['Competition'] == 'SerieA':
            # Append each matching update to the crazy_bet_updates list
            crazy_bet_updates.append(update)
            # Write filtered data list to new json file
            with open("crazy_bet.json", "w", encoding='utf-8') as file:
                json.dump(crazy_bet_updates, file, indent=4)


crazy_bet()


def lucky_bet():
    """ Function that filters data from updates file
    based on the LuckyBet customer contract.
    Saves the filtered data to a new json file.
    """
    lucky_bet_updates = []
    # Loop through all updates in forwarder_updates data.
    for update in updates:
        # Exclude all Premier League competition updates.
        if update['Competition'] != 'PremierLeague':
            # Find updates within the filtered data
            # Where probability is higher than 0.25
            if update['Probability'] >= 0.25:
                # Append each matching update to the lucky_bet_updates list.
                lucky_bet_updates.append(update)
                # Write filtered data list to new json file
                with open("lucky_bet.json", "w", encoding='utf-8') as file:
                    json.dump(lucky_bet_updates, file, indent=4)


lucky_bet()
