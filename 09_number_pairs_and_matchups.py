# ************************* Printing Pairs of Numbers *************************

# Loop through numbers 0 to 6 for the left side of the pair
for left in range(7):
    # Loop through numbers starting from the current left number to 6 for the right side of the pair
    for right in range(left, 7):
        # Print the pair [left|right] and stay on the same line
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    # After printing all pairs for the current left, move to the next line
    print()



# ************************* Printing Matchups Between Teams *************************
# Define a list of team names
teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']

# Loop through each team as the home team
for home_team in teams:
    # Loop through each team as the away team
    for away_team in teams:
        # Check if the home team and away team are different
        if home_team != away_team:
            # Print the matchup between the home team and the away team
            print(home_team + " vs " + away_team)
