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
        print("[8] Rate a Trip")
        print("[9] View Top Rated")
        
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
                    rating = f"Rating: {trip.rating}/5" if trip.rating > 0 else "unrated"
                    print(f"{i}. {trip.name} ({trip.country}) - ${trip.budget:.2f} [{status}] ({rating})")
                    if trip.notes:
                        print(f"   Notes: {trip.notes}")
        
        elif choice == "3":
            country = input("Enter country: ")
            results = collection.search_by_country(country)
            for trip in results:
                status = "Visited" if trip.visited else "Wishlist"
                rating = f"Rating: {trip.rating}/5" if trip.rating > 0 else "unrated"
                print(f"{trip.name} ({trip.country}) - ${trip.budget:.2f} [{status}] ({rating})")
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

        elif choice == "8":
            trips = collection.get_all()
            for i, trip in enumerate(trips, 1):
                rating = f"{trip.rating}/5" if trip.rating > 0 else "unrated"
                print(f"{i}. {trip.name} ({rating})")
            
            n = int(input("Select number: "))
            r = int(input("Enter rating (1-5): "))
            collection.rate(n - 1, r)
            save_trips(collection)
            print(f"Rated {trips[n-1].name} as {r}/5!")

        elif choice == "9":
            top = collection.top_rated(3)
            if not top:
                print("No rated trips yet.")
            else:
                print("\n=== Top Rated Trips ===")
                for trip in top:
                    print(f"- {trip.name}: {trip.rating}/5")
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
