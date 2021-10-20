import subprocess
from datetime import datetime
from pathlib import Path


def _run_shell_command(cmd: str, quiet: bool = True):
    return subprocess.run(cmd, shell=True, capture_output=quiet, check=True)


def is_repo(repo: Path):
    try:
        _run_shell_command(f'cd "{repo.resolve()}" && git status')
        return True
    except subprocess.CalledProcessError:
        return False


README_CONTENT = """
# This repository was created automatically by [\`image-in-gh-commit-calendar\`](https://github.com/nj-vs-vh/gh-commit-calendar)

It contains generated commits spread across time to create an image on contributions calendar on owners' GitHub page.
"""


def commit_on_datetime(
    d: datetime, repo: Path, first_commit: bool = False, image_path: Path = None
):
    dummy_filename = "autogenerated_commits"
    _run_shell_command(
        f'cd "{repo.resolve()}" && '
        + f"touch {dummy_filename} && "
        + f"echo 1 >> {dummy_filename} && "
        + (
            f"cp {image_path} ./source_image{image_path.suffix} && "
            if first_commit and image_path is not None
            else ""
        )
        + (f'echo "{README_CONTENT}" > README.md && ' if first_commit else "")
        + f"git add . &&"
        + f"export GIT_COMMITTER_DATE={d.isoformat()} && "
        + f'git commit -m "auto-committed by image-in-gh-commit-calendar" --date {d.isoformat()}',
    )


def init(repo: Path):
    if not is_repo(repo):
        _run_shell_command(
            f'cd "{repo.resolve()}" && ' + f"git init",
        )
    else:
        raise FileExistsError(f"{repo.resolve()} is inside an existing git repository!")


def push(repo: Path, remote_url: str):
    _run_shell_command(
        f'cd "{repo.resolve()}" && '
        + f"git remote add origin {remote_url} && "
        + f"git branch -M main && "
        + f"git push -u origin main --force",
        quiet=False,
    )
