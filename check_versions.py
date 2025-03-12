import subprocess
import re
import sys

def get_latest_version(package_name):
    try:
        result = subprocess.run(
            ["uv", "pip", "search", package_name], 
            capture_output=True, 
            text=True
        )
        if result.returncode != 0:
            # Try PyPI API search as fallback
            result = subprocess.run(
                ["curl", "-s", f"https://pypi.org/pypi/{package_name}/json"],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                import json
                data = json.loads(result.stdout)
                return data.get("info", {}).get("version", "Unknown")
        
        # Parse the output to find the latest version
        lines = result.stdout.split('\n')
        for line in lines:
            if package_name in line:
                version_match = re.search(r'\d+\.\d+\.\d+', line)
                if version_match:
                    return version_match.group(0)
        
        return "Unknown"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Parse requirements file
    with open("requirements.txt", "r") as f:
        requirements = f.readlines()
    
    updated_requirements = []
    
    for line in requirements:
        # Skip comments and empty lines
        if line.strip().startswith("#") or not line.strip():
            updated_requirements.append(line)
            continue
        
        # Extract package name and version constraint
        match = re.match(r'([a-zA-Z0-9_-]+)([<>=~!].+)?', line.strip())
        if match:
            package_name = match.group(1)
            latest_version = get_latest_version(package_name)
            
            if latest_version != "Unknown":
                updated_requirements.append(f"{package_name}>={latest_version}\n")
            else:
                updated_requirements.append(line)
        else:
            updated_requirements.append(line)
    
    # Write updated requirements
    with open("requirements.txt.new", "w") as f:
        f.writelines(updated_requirements)
    
    print("Updated requirements written to requirements.txt.new")

if __name__ == "__main__":
    main()