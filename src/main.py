import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models import Destination, TripCollection
from src.storage import load_trips, save_trips

def main():
    collection = load_trips()
    
    while True:
        print("\n=== Trip Notes ===")
        print("[1] Add destination")
        print("[2] View all destinations")
        print("[3] Search by country")
        print("[4] Add note to a destination")
        print("[5] Quit")
        print("[6] Mark as Visited")
        print("[7] Wishlist / Visited")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            name = input("Enter destination name: ")
            country = input("Enter country: ")
            budget = float(input("Enter budget: "))
            
            dest = Destination(name, country, budget)
            collection.add(dest)
            save_trips(collection)
            print("Destination added!")
            
        elif choice == "2":
            if len(collection) == 0:
                print("No trips saved yet.")
            else:
                for i, trip in enumerate(collection.get_all(), 1):
                    status = "Visited" if trip.visited else "Wishlist"
                    print(f"{i}. {trip.name} ({trip.country}) - ${trip.budget:.2f} [{status}]")
                    if trip.notes:
                        print(f"   Notes: {trip.notes}")
        
        elif choice == "3":
            country = input("Enter country: ")
            results = collection.search_by_country(country)
            for trip in results:
                status = "Visited" if trip.visited else "Wishlist"
                print(f"{trip.name} ({trip.country}) - ${trip.budget:.2f} [{status}]")
                if trip.notes:
                    print(f"   Notes: {trip.notes}")
        
        elif choice == "4":
            for i, trip in enumerate(collection.get_all(), 1):
                print(f"{i}. {trip.name}")
            
            n = int(input("Select number: "))
            trip = collection.get_by_index(n - 1)
            note = input("Enter note: ")
            trip.add_note(note)
            save_trips(collection)
            print("Note added!")
                
        elif choice == "5":
            print("Goodbye!")
            break

        elif choice == "6":
            trips = collection.get_all()
            for i, trip in enumerate(trips, 1):
                print(f"{i}. {trip.name}")
            
            n = int(input("Select number: "))
            collection.mark_visited(n - 1)
            name = collection.get_by_index(n - 1).name
            save_trips(collection)
            print(f"Marked {name} as visited!")

        elif choice == "7":
            wishlist = collection.get_wishlist()
            visited = collection.get_visited()
            
            print(f"\nWishlist ({len(wishlist)}):")
            for trip in wishlist:
                print(f"- {trip.name} ({trip.country})")
                
            print(f"\nVisited ({len(visited)}):")
            for trip in visited:
                print(f"- {trip.name} ({trip.country})")
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
