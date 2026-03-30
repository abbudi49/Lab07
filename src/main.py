import sys
import os

# Add project root to sys.path
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
            try:
                budget_input = input("Enter budget: ")
                budget = float(budget_input)
            except ValueError:
                print("Invalid budget. Using 0.0.")
                budget = 0.0
            
            dest = Destination(name=name, country=country, budget=budget)
            collection.add(dest)
            save_trips(collection)
            print("Destination added!")
            
        elif choice == "2":
            trips = collection.get_all()
            if not trips:
                print("No trips saved yet.")
            else:
                for i, trip in enumerate(trips, 1):
                    print(f"{i}. {trip.name} ({trip.country}) - ${trip.budget:.2f}")
                    if trip.notes:
                        print(f"   Notes: {', '.join(trip.notes)}")
        
        elif choice == "3":
            country = input("Enter country to search: ")
            results = collection.search_by_country(country)
            if not results:
                print(f"No trips found for {country}.")
            else:
                for trip in results:
                    print(f"- {trip.name} (${trip.budget:.2f})")
                    if trip.notes:
                        print(f"  Notes: {', '.join(trip.notes)}")
        
        elif choice == "4":
            trips = collection.get_all()
            if not trips:
                print("No trips saved yet.")
                continue
            
            for i, trip in enumerate(trips, 1):
                print(f"{i}. {trip.name} ({trip.country})")
            
            try:
                idx_input = input("Select destination number to add note: ")
                idx = int(idx_input) - 1
                if 0 <= idx < len(trips):
                    note = input("Enter note: ")
                    trip = collection.get_by_index(idx)
                    trip.add_note(note)
                    save_trips(collection)
                    print("Note added!")
                else:
                    print("Invalid destination number.")
            except ValueError:
                print("Invalid input.")
                
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
