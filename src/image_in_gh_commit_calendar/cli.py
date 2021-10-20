import click

from .run import generate
from .image2calendar import image2calendar


@click.group()
def cli():
    pass


@cli.command(
    "generate",
    help=(
        "Create new repository, populate it with commits spread across dates "
        + "so that they create an image and push it to GitHub repo"
    ),
)
@click.option("-i", "--image", "image_path", required=True, help="Path to source image file")
@click.option(
    "-r",
    "--remote",
    "remote_repo",
    default=None,
    help=(
        "Remote repo url, e.g. git@github.com:nj-vs-vh/my-generated-repo.git;"
        + " Please note that this repo will be completely overritten with generated commits"
    ),
)
@click.option(
    "-c",
    "--max-commits-per-day",
    "max_commits_per_day",
    default=30,
    help="Maximum number of commits to generate in one day. Defines 'bit depth' of the image.",
)
@click.option(
    "--repo-dir",
    "local_repo_path",
    default="../image-in-gh-commit-calendar-generated-repo",
    help=(
        "Local directory to create repo. Will be completely overritten. "
        + "Note that it cannot be placed inside existing git repository"
    ),
)
def generate_cmd(image_path, remote_repo, local_repo_path, max_commits_per_day):
    generate(remote_repo, local_repo_path, image_path, max_commits_per_day)


@cli.command(
    "preview",
    help=(
        "Preview image as it will be seen on GitHub commits calendar"
    ),
)
@click.option("-i", "--image", "image_path", required=True, help="Path to source image file")
@click.option("-o", "--output", "preview_path", required=True, help="Path to output preview image file")
@click.option(
    "-c",
    "--max-commits-per-day",
    "max_commits_per_day",
    default=30,
    help="Maximum number of commits to generate in one day. Defines 'bit depth' of the image.",
)
def preview_cmd(image_path, preview_path, max_commits_per_day):
    image2calendar(image_path, max_commits_per_day, save_preview_to=preview_path)
