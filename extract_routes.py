import os
import re

def extract_routes(file_path):
    route_pattern = re.compile(r'path\s*[:=]\s*["\']([^"\']+)["\']')
    routes = []
    
    if file_path.endswith(('.js', '.jsx', '.ts', '.tsx')):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            matches = route_pattern.findall(content)
            routes.extend(match for match in matches if not match.endswith('/*'))
    
    return routes

def main():
    file_path = input("Enter the file path to scan: ").strip()
    routes = extract_routes(file_path)
    
    print(f"Total Routes Found: {len(routes)}")
    for i, route in enumerate(routes, start=1):
        print(f"{i}. {route}")

if __name__ == "__main__":
    main()
