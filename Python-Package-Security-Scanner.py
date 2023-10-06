# Import necessary modules
import pandas as pd
import subprocess
import requests
import io
import os
import platform  # Importing the platform module

# Read the infected packages list from the given URL
def read_infected_packages_from_url(url):
    print("Fetching infected package list from URL...")
    response = requests.get(url)
    csv_data = response.text
    df = pd.read_csv(io.StringIO(csv_data))
    infected_packages = df['Package_Name'].tolist()
    print(f"Found {len(infected_packages)} infected packages in the list.")
    return infected_packages

# Get list of installed Python packages via pip
def get_installed_python_packages(python_executable):
    print(f"Scanning installed Python packages for {python_executable}...")
    result = subprocess.run([python_executable, '-m', 'pip', 'list', '--format=freeze'], capture_output=True, text=True)
    installed_packages = [line.split('==')[0] for line in result.stdout.split('\n') if line]
    print(f"Found {len(installed_packages)} installed Python packages.")
    return installed_packages

# Compare and report any infected installed packages
def find_and_report_infected_packages(installed_packages, infected_packages):
    print("Comparing installed Python packages with infected packages...")
    infected_installed_packages = []
    for package in infected_packages:
        if package in installed_packages:
            print(f"!!Warning: Found infected package - {package}!!")
            infected_installed_packages.append(package)
    if infected_installed_packages:
        print("Summary: The following infected packages are installed:")
        for package in infected_installed_packages:
            print(f"  - {package}")
    else:
        print("No infected packages found.")

# Get the Python executables in the current environment
def get_python_executables():
    print("Searching for Python executables...")
    if platform.system() == 'Windows':  # Check if the system is Windows
        result = subprocess.run(['where', 'python', 'python3'], capture_output=True, text=True, shell=True)
    else:
        result = subprocess.run(['which', 'python', 'python3'], capture_output=True, text=True)  # For Unix-like systems
    executables = result.stdout.split('\n')
    executables = [exe for exe in executables if exe]  # Remove empty strings
    print(f"Found Python executables: {executables}")
    return executables

# Main function
if __name__ == "__main__":
    infected_packages_url = "https://gist.githubusercontent.com/masteryoda101/65b55a117fe2ea33735f05024abc92c2/raw/765aa71606c7c6e245aef41581012fa87e38b787/Persistent_Python_Threat_April_August.csv"
    infected_packages = read_infected_packages_from_url(infected_packages_url)
    python_executables = get_python_executables()
    for python_executable in python_executables:
        print(f"Checking environment with Python executable: {python_executable}")
        installed_packages = get_installed_python_packages(python_executable)
        find_and_report_infected_packages(installed_packages, infected_packages)
