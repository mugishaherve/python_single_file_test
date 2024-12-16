import subprocess
import datetime

# Set the starting date for commits
START_DATE = datetime.datetime(2024, 10, 10)

def auto_commit(commit_message=None, push=False):
    try:
        # Step 1: Check if there are changes to commit
        result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        changes = result.stdout.strip()

        if not changes:
            print("No changes detected. Nothing to commit.")
            return  # Exit the function if no changes are found

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
