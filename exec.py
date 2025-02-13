from extract_routes import extract_routes
from diff_lists import compute_diff, print_diff

def main():
    v3_path = input("Enter the path to the v3 routes file: ").strip()
    v3_routes = extract_routes(v3_path)
    
    v6_path = input("Enter the path to the v6 routes file: ").strip()
    v6_routes = extract_routes(v6_path)

    print("\nV3 ROUTES")
    print(f"Total Routes Found: {len(v3_routes)}")
    for i, route in enumerate(v3_routes, start=1):
        print(f"{i}. {route}")
        
    print("\nV6 ROUTES")
    print(f"Total Routes Found: {len(v6_routes)}")
    for i, route in enumerate(v6_routes, start=1):
        print(f"{i}. {route}")
    
    v3_diff, v6_diff = compute_diff(v3_routes, v6_routes)
    print("\nRESULTS\n")
    print_diff(v3_diff, v6_diff)

if __name__ == "__main__":
    main()