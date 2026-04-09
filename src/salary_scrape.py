import pandas as pd

def scrape_salary(init_year, end_year):
    if (type(init_year) is not int and type(end_year) is not int):
        print("Invalid year type. ")

    for year in range(init_year, end_year + 1):
        url = f"https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html"
        try:
            df = pd.read_html(url)[0]
            df.to_csv(f"./data/raw/nba_{year}_stats_per_game.csv", index=False)

            print("'nba_{year}_stats_per_game.csv' was added ")
        except ValueError:
            print(f"ERROR: No table found in {url}.")
        except Exception as e:
            print(f"Unexpected error {e} has occurred.")

scrape_salary(2001, 2010)
