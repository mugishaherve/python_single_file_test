import subprocess
import datetime

# Set the starting date for commits
START_DATE = datetime.datetime(2024, 10, 10)  # Naive datetime

def auto_commit(commit_message=None, push=False):
    try:
        # Step 1: Get the latest commit date
        result = subprocess.run(
            ['git', 'log', '--date=iso', '--pretty=format:%cd', '-n', '1'],
            capture_output=True,
            text=True
        )
        last_commit_date = result.stdout.strip()
        
        if not last_commit_date:
            print("No commits found in the repository. Proceeding with initial commit.")
            last_commit_datetime = None
        else:
            # Parse the last commit date to a naive datetime
            last_commit_datetime = datetime.datetime.fromisoformat(last_commit_date).replace(tzinfo=None)

        # Check if the last commit was before the specified start date
        if last_commit_datetime is None or last_commit_datetime < START_DATE:
            print(f"Last commit was before {START_DATE}. Starting commits from {START_DATE} onward.")
        
        # Step 2: Add all changes
        subprocess.run(['git', 'add', '--all'], check=True)
        print("Staged all changes.")

        # Step 3: Create a commit message
        if not commit_message:
            commit_message = f"Auto commit on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

        # Step 4: Commit changes
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        print(f"Committed changes: {commit_message}")

        # Step 5: Optionally push changes
        if push:
            subprocess.run(['git', 'push'], check=True)
            print("Pushed changes to the remote repository.")
    except subprocess.CalledProcessError as e:
        print(f"Error during Git operation: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Usage
if __name__ == "__main__":
    auto_commit(commit_message="Updated features and fixes from October 10th onwards", push=True)
