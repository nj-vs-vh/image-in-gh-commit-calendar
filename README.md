# Cutting-edge GitHub page customization tool

Want to customize your GitHub user page, but don't know how? Now you can make your profile
unique and attractive by placing any greyscale image in stunning 52x7 resolution right on
your contributions timeline!


## Installation

```bash
pip install git+https://github.com/nj-vs-vh/image-in-gh-commit-calendar.git
```


## Usage

### Generating commits from raster image

```bash
# basic run
gh-cal-image generate --image ./example/hello-world.png --max-commits-per-day 50
# with auto-push
gh-cal-image generate --image ./example/hello-world.png --max-commits-per-day 50 --remote git@github.com:nj-vs-vh/my-dummy-repo.git
# full options list
gh-cal-image generate --help
```

### Preview image

```bash
gh-cal-image preview --image ./example/hello-world.png --max-commits-per-day 30 --output preview.png
```
