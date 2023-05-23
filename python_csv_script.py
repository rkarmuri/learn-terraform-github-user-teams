import csv
import glob

# Read and process team member CSV files
def process_team_members():
    team_members_path = "team-members"

    # Iterate over CSV files in the team-members directory
    for file_name in glob.glob(f"{team_members_path}/*.csv"):
        with open(file_name, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                # Process each row in the CSV file
                username = row["username"]
                role = row["role"]
                
                # Perform the desired operations with the data from the CSV file
                # Example: Print the username and role
                print(f"Username: {username}, Role: {role}")


# Read and process repository team membership CSV files
def process_repo_teams():
    repo_teams_path = "repos-team"

    # Iterate over CSV files in the repos-team directory
    for file_name in glob.glob(f"{repo_teams_path}/*.csv"):
        with open(file_name, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                # Process each row in the CSV file
                team_name = row["team_name"]
                permission = row["permission"]
                
                # Perform the desired operations with the data from the CSV file
                # Example: Print the team name and permission
                print(f"Team Name: {team_name}, Permission: {permission}")


# Main function to call the CSV processing functions
def main():
    process_team_members()
    process_repo_teams()


if __name__ == "__main__":
    main()
