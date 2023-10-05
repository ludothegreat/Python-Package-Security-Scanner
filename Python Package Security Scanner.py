import pandas as pd
import subprocess
import requests
import io

# Read the infected apps list from the given URL
def read_infected_apps_from_url(url):
    print("Fetching infected application list from URL...")
    response = requests.get(url)
    csv_data = response.text
    df = pd.read_csv(io.StringIO(csv_data))
    infected_apps = df['Package_Name'].tolist()
    print(f"Found {len(infected_apps)} infected applications in the list.")
    return infected_apps

# Get list of installed Python packages via pip
def get_installed_python_packages():
    print("Scanning installed Python packages on your computer...")
    result = subprocess.run(['pip', 'list', '--format=freeze'], capture_output=True, text=True)
    installed_apps = [line.split('==')[0] for line in result.stdout.split('\n') if line]
    print(f"Found {len(installed_apps)} installed Python packages.")
    print("Installed Python packages:")
    for app in installed_apps:
        print(f"  - {app}")
    return installed_apps

# Compare and report any infected installed apps
def find_and_report_infected_apps(installed_apps, infected_apps):
    print("Comparing installed Python packages with infected applications...")
    infected_installed_apps = []
    
    for app in infected_apps:
        print(f"Checking for infected application: {app}")
        if app in installed_apps:
            print(f"Warning: Found infected application - {app}")
            infected_installed_apps.append(app)
            
    if infected_installed_apps:
        print("Summary: The following infected applications are installed:")
        for app in infected_installed_apps:
            print(f"  - {app}")
    else:
        print("No infected applications found.")

if __name__ == "__main__":
    infected_apps_url = "https://gist.githubusercontent.com/masteryoda101/65b55a117fe2ea33735f05024abc92c2/raw/765aa71606c7c6e245aef41581012fa87e38b787/Persistent_Python_Threat_April_August.csv"
    infected_apps = read_infected_apps_from_url(infected_apps_url)
    installed_apps = get_installed_python_packages()
    find_and_report_infected_apps(installed_apps, infected_apps)
