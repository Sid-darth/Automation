import os
import datetime
import subprocess
import re

def update_readme():
    current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    last_commit = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf-8").strip()

    with open("README.md", "r+") as f:
        content = f.read()
        pattern = r"Last pushed: (.*)"
        match = re.search(pattern, content)
        if match:
            new_line = f"Last pushed: {current_date_time} | Commit #{last_commit[:5]}\n"
            content = re.sub(pattern, new_line, content)
        else:
            content += f"Last pushed: {current_date_time} | Commit #{last_commit[:5]}\n"
        f.seek(0)
        f.write(content)
        f.truncate()

    # subprocess.run(["git", "add", "README.md"])
    # subprocess.run(["git", "commit", "-m", "Update README.md with last push time and commit number"])
    # subprocess.run(["git", "push", "origin", "main"])

if __name__ == "__main__":
    update_readme()