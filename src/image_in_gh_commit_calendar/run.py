from pathlib import Path
from datetime import datetime, time, timedelta
from tqdm import tqdm
from shutil import rmtree

from typing import Optional

from . import git, image2calendar


def generate(
    remote_repo_url: Optional[str],
    local_repo_path: str,
    image_path: str,
    max_commits_per_day: int,
):
    image_path = Path(image_path).resolve()
    commit_count_by_date = image2calendar.image2calendar(
        image_path, max_commits_per_day=max_commits_per_day
    )

    repo = Path(local_repo_path)
    if repo.exists():
        rmtree(repo)
    repo.mkdir(parents=True)

    git.init(repo)

    first_commit = True
    for commit_date, commit_count in tqdm(commit_count_by_date.items(), total=len(commit_count_by_date)):
        base_datetime = datetime.combine(commit_date, time(hour=12))
        for seconds in range(commit_count):
            git.commit_on_datetime(
                d=base_datetime + timedelta(seconds=seconds),
                repo=repo,
                first_commit=first_commit,
                image_path=image_path,
            )
            first_commit = False

    if remote_repo_url is not None:
        git.push(repo, remote_repo_url)
    else:
        print(f"Commits created in repo {repo.resolve()}\nGo push it!")
