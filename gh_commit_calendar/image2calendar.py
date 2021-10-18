from PIL import Image, ImageOps
from pathlib import Path
from datetime import datetime, timedelta, date

from typing import Dict, Optional


GITHUB_CALENDAR_WEEKS = 52
GITHUB_CALENDAR_DAYS_PER_WEEK = 7


def weekday(dt: datetime) -> int:
    """Weekday, where 0 is Sun, 1 is Mon, 6 is Sat, following GitHub calendar"""
    return (dt.weekday() + 1) % 7


def pixel2date(i_day: int, j_week: int, year: Optional[int]) -> datetime:
    if year is None:
        now = datetime.utcnow()
    else:
        now = datetime(year=year, month=12, day=31)
    # right-bottom pixel of an image
    last_saturday = now - timedelta(days=(1 + weekday(now)))
    target_week_saturday = last_saturday - timedelta(days=7*(GITHUB_CALENDAR_WEEKS - (j_week + 1)))
    target_day = target_week_saturday - timedelta(days=(GITHUB_CALENDAR_DAYS_PER_WEEK - (i_day + 1)))
    return target_day.date()


def image2calendar(image_file: Path, max_commits_per_day: int = 100, year: Optional[int] = None) -> Dict[date, int]:
    img = Image.open(image_file)
    img = ImageOps.grayscale(img)
    img = ImageOps.invert(img)
    img = img.resize((GITHUB_CALENDAR_WEEKS, GITHUB_CALENDAR_DAYS_PER_WEEK), resample=Image.BICUBIC)

    commit_count_by_date = dict()

    for idx, pixel in enumerate(img.getdata()):
        i = idx // GITHUB_CALENDAR_WEEKS
        j = idx % GITHUB_CALENDAR_WEEKS
        pixel = pixel / 255  # 0 - 1 float value

        commit_count_by_date[pixel2date(i, j, year)] = int(pixel * max_commits_per_day)

    return {dt: commit_count_by_date[dt] for dt in sorted(commit_count_by_date.keys())}
