from pathlib import Path
from datetime import datetime, time, timedelta
from tqdm import tqdm
from shutil import rmtree

from gh_commit_calendar import git, image2calendar


def create_repo_with_image(remote_repo_url: str, local_repo_name: str, image_file: Path, overwrite: bool = True):
    commit_count_by_date = image2calendar.image2calendar(image_file, max_commits_per_day=30)

    repo = Path(__file__).parent / f'../../gh-commit-calendar-generated-repos/{local_repo_name}'
    if overwrite and repo.exists():
        rmtree(repo)
    repo.mkdir(parents=True)

    git.init(repo)
    
    readme_generated = False
    n_dates = len(commit_count_by_date)
    for commit_date, commit_count in tqdm(commit_count_by_date.items(), total=n_dates):
        common_datetime = datetime.combine(commit_date, time(hour=12))
        for seconds in range(commit_count):
            if not readme_generated:
                readme_generated = False
                add_readme = True
            else:
                add_readme = False

            git.commit_on_datetime(
                d=common_datetime + timedelta(seconds=seconds),
                repo=repo,
                add_readme=add_readme,
            )

    git.push(repo, remote_repo_url)
