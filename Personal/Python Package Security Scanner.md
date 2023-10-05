# Python Package Security Scanner

## Overview

This Python script is designed to scan your installed Python packages and compare them against a list of known malicious packages. The need for such a script was highlighted in a [BleepingComputer article](https://www.bleepingcomputer.com/news/security/hundreds-of-malicious-python-packages-found-stealing-sensitive-data/), which reported the presence of hundreds of malicious Python packages

## Why This is Important

As Python continues to grow in popularity, the risk of encountering malicious packages also increases. Often these packages are named similarly to well-known packages, making it easy to install them by mistake. Once installed, they could execute harmful code, jeopardizing your data and system security.

## Source of Malicious Package List

The list of malicious packages used by this script is based on the CSV file mentioned in the BleepingComputer article. The CSV file can be found [here](https://gist.github.com/masteryoda101/65b55a117fe2ea33735f05024abc92c2).

## How the Script Works

The script performs the following tasks:

1.  Fetches a list of known malicious Python packages from the given URL.
2.  Lists all Python packages installed on your system via pip.
3.  Compares the installed packages with the list of malicious packages.
4.  Reports if any malicious package is installed.

## Dependencies

- Python 3.x
- `requests` package for fetching data from the URL
- `pip` for listing installed Python packages

## Usage

1.  Clone the repository or download the script.
2.  Open a terminal and navigate to the folder containing the script.
3.  Run `python scan_for_infected_apps.py`.

The script will then fetch the list of malicious apps, scan your installed Python packages, and report any matches.