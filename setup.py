from setuptools import setup, find_packages


setup(
    name='image_in_gh_commit_calendar',
    version='0.0.3',
    author='Igor Vaiman',
    description='Cutting-edge GitHub page customization tool',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['Pillow>=8.4.0', 'click>=8', 'tqdm>=4'],
    python_requires='>=3',
    entry_points={
        'console_scripts': ['gh-cal-image=image_in_gh_commit_calendar.cli:cli'],
    },
)
