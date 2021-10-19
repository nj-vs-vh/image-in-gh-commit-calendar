from gh_commit_calendar import create_repo_with_image


create_repo_with_image(
    remote_repo_url='git@github.com:nj-vs-vh/gh-commit-calendar-generated-image.git',
    local_repo_name='test',
    image_file='example/hello-world.png',
    max_commits_per_day=20,
)
