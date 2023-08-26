import time
from github import Github
import re
from pathlib import Path
import sys

# Adding the grandparent directory to sys.path
sys.path.append(str(Path(__file__).parent.parent.parent.resolve()))  # nopep8

from scripts.github.access_token import ACCESS_TOKEN  # nopep8


# Initialize using an access token
g = Github(ACCESS_TOKEN)

# Name of your repository
REPO_NAME = 'jm0rt1/dental-simulation-analysis'

# Fetch the repo
repo = g.get_repo(REPO_NAME)

# Parse the markdown file


def parse_md(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    milestones = re.split(r'##\s+', content)[1:]
    parsed_data = {}

    for m in milestones:
        lines = m.splitlines()
        milestone_name = lines[0].strip()

        issue_data = []
        parent_issue = None
        for i in lines[1:]:
            if not i:
                continue
            issue_title = i.split(']')[1].split('|')[0].strip()
            assignee = None
            labels = None

            if len(i.split('|')) > 1:
                assignee = i.split('|')[1].strip()

            if len(i.split('|')) > 2:
                labels = [label.strip()
                          for label in i.split('|')[2].split(',')]

            if i.startswith('-'):
                parent_issue = issue_title
                issue_data.append((issue_title, assignee, labels, None))
            else:
                issue_data.append(
                    (issue_title, assignee, labels, parent_issue))

        parsed_data[milestone_name] = issue_data

    return parsed_data


def create_milestones_and_issues(data):
    for milestone_name, issues in data.items():
        # Create or fetch milestone
        milestone = None
        for m in repo.get_milestones():
            if m.title == milestone_name:
                milestone = m
                break

        if milestone is None:
            milestone = repo.create_milestone(milestone_name)

        parent_issue_number = None
        # Create issues
        for issue_tuple in issues:
            issue_title, assignee, labels, parent_issue_title = issue_tuple

            # Create a description with a reference to the parent issue if it's a child task
            description = f"Related to #{parent_issue_number}" if parent_issue_title else ""

            issue = repo.create_issue(title=issue_title, milestone=milestone, body=description,
                                      assignee=assignee, labels=labels)
            # If it's a parent issue, store its number
            if not parent_issue_title:
                parent_issue_number = issue.number

            # Sleep for a short period (e.g., 2 seconds) between issue creations to avoid rate limits
            time.sleep(2)


data = parse_md('docs/tasks/tasks.md')
create_milestones_and_issues(data)
