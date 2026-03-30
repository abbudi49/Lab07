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
                    print(f"{i}. {trip.name} ({trip.country}) - ${trip.budget:.2f}")
                    if trip.notes:
                        print(f"   Notes: {trip.notes}")
        
        elif choice == "3":
            country = input("Enter country: ")
            results = collection.search_by_country(country)
            for trip in results:
                print(f"{trip.name} ({trip.country}) - ${trip.budget:.2f}")
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
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
