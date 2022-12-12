# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime

def convert_date(date_str):
    # Parse the date string using the datetime module
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Return the date as a string in the desired format
    return date.strftime("%Y-%m-%d")

def calculate_season_averages(data):
    # Group the data by player and season
    grouped = data.groupby(["PLAYER_ID", "SEASON"])
    
    # Calculate the season averages for each player
    averages = grouped.mean()
    
    # Return the season averages as a DataFrame
    return averages


def main():
    # Load the data into a Pandas DataFrame
    game_data = pd.read_csv("./data/games.csv")
    game_data["GAME_DATE_EST"] = game_data["GAME_DATE_EST"].apply(convert_date)
    player_data = pd.read_csv("./data/games_details.csv")


    game_data = game_data[["GAME_ID", "HOME_TEAM_ID", "VISITOR_TEAM_ID", "SEASON", "GAME_DATE_EST", "HOME_TEAM_WINS"]]
    player_data = player_data[["GAME_ID", "PLAYER_ID", "FG_PCT", "FG3_PCT", "FT_PCT", "PTS", "AST", "OREB", "DREB", "STL", "BLK", "TO", "COMMENT"]]
    player_data["ACTIVE"] = player_data["COMMENT"].apply(lambda x: 0 if pd.notnull(x) else 1)

    games_data_combined = game_data.merge(player_data, on="GAME_ID")
    games_data_combined = games_data_combined[["GAME_ID", "HOME_TEAM_ID", "VISITOR_TEAM_ID", "SEASON", "GAME_DATE_EST", "HOME_TEAM_WINS", "PLAYER_ID", "ACTIVE"]]


    player_game_data = game_data.merge(player_data, on="GAME_ID")

    print("COMBINED", games_data_combined)
    print(game_data)
    print(player_data)
    print(player_game_data)

    player_average_data = calculate_season_averages(player_game_data[["PLAYER_ID", "SEASON", "FG_PCT", "FG3_PCT", "FT_PCT", "PTS", "AST", "OREB", "DREB", "STL", "BLK", "TO"]])
    print(player_average_data)

    data = player_average_data.merge(games_data_combined, on=["PLAYER_ID", "SEASON"])
    print(data)
    data = data.dropna()

    # Select the relevant columns from the data
    X = data[["HOME_TEAM_ID", "VISITOR_TEAM_ID", "SEASON", "PLAYER_ID", 
    "FG_PCT", "FG3_PCT", "FT_PCT", "PTS", "AST", "OREB", "DREB", "STL", "BLK", "TO", "ACTIVE"]]
    

    print("X", data)

    # Define the target variable
    y = data["HOME_TEAM_WINS"]
    print("y", y)

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # Train a Random Forest classifier on the training data
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    # Use the trained model to make predictions on the test set
    predictions = clf.predict(X_test)

    # Evaluate the model's performance on the test set
    accuracy = clf.score(X_test, y_test)
    print("Accuracy:", accuracy)


if __name__ == "__main__":
    main()