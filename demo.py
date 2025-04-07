from source_management import SourceManagement
from conservation_strategy import ConservationStrategy
from treatment_plant import TreatmentPlant
from usage_monitoring import UsageMonitoring
from distribution_system import DistributionSystem

# Initialize all classes
source_mgmt = SourceManagement()
conservation = ConservationStrategy()
treatment = TreatmentPlant()
usage = UsageMonitoring()
distribution = DistributionSystem()


# === Helper Menus === #
def main_menu():
    print("\n=== Water Management System ===")
    print("1. Source Management")
    print("2. Conservation Strategies")
    print("3. Treatment Plans")
    print("4. Usage Monitoring")
    print("5. Distribution System")
    print("0. Exit")

# === Source Management === #
def source_menu():
    while True:
        print("\n--- Source Management ---")
        print("1. Add Source")
        print("2. Remove Source")
        print("3. Show All Sources")
        print("4. Show Active Sources")
        print("5. Update Water Level")
        print("6. Check Quality")
        print("7. Show Total Capacity")
        print("8. Show Available Water")
        print("9. Deactivate Source")
        print("10. Show Sources by Type")
        print("0. Back")
        ch = input("Enter choice: ")

        if ch == "1":
            source = {
                "id": int(input("ID: ")),
                "type": input("Type: "),
                "location": tuple(map(float, input("Location (lat,lon): ").split(","))),
                "capacity": int(input("Capacity: ")),
                "current_level": int(input("Current Level: ")),
                "quality": input("Quality: "),
                "status": input("Status: ")
            }
            source_mgmt.add_source(source)
        elif ch == "2":
            source_mgmt.remove_source(int(input("ID to remove: ")))
        elif ch == "3":
            source_mgmt.print_summary()
        elif ch == "4":
            print(source_mgmt.get_active_sources())
        elif ch == "5":
            print("Updated:", source_mgmt.update_level(int(input("ID: ")), int(input("New Level: "))))
        elif ch == "6":
            print("Quality:", source_mgmt.check_quality(int(input("ID: "))))
        elif ch == "7":
            print("Total Capacity:", source_mgmt.get_total_capacity())
        elif ch == "8":
            print("Available Water:", source_mgmt.get_available_water())
        elif ch == "9":
            print("Deactivated:", source_mgmt.deactivate_source(int(input("ID: "))))
        elif ch == "10":
            print("Sources:", source_mgmt.get_sources_by_type(input("Type: ")))
        elif ch == "0":
            break

# === Conservation Strategy === #
def conservation_menu():
    while True:
        print("\n--- Conservation Strategy ---")
        print("1. Add Strategy")
        print("2. Remove Strategy")
        print("3. Show All Strategies")
        print("4. Active Strategies")
        print("5. Completed Strategies")
        print("6. Update Status")
        print("7. Total Water Saved")
        print("8. By Area")
        print("9. Sorted by Savings")
        print("0. Back")
        ch = input("Enter choice: ")

        if ch == "1":
            s = {
                "id": input("ID: "),
                "name": input("Name: "),
                "target_area": input("Area: "),
                "savings": int(input("Savings (L): ")),
                "status": input("Status: ")
            }
            conservation.add_strategy(s)
        elif ch == "2":
            conservation.remove_strategy(input("ID: "))
        elif ch == "3":
            conservation.print_summary()
        elif ch == "4":
            print(conservation.get_active_strategies())
        elif ch == "5":
            print(conservation.get_completed_strategies())
        elif ch == "6":
            print("Updated:", conservation.update_status(input("ID: "), input("New Status: ")))
        elif ch == "7":
            print("Total Saved:", conservation.calculate_total_savings(), "L")
        elif ch == "8":
            print("Strategies:", conservation.get_strategies_by_area(input("Area: ")))
        elif ch == "9":
            for strat in conservation.sort_by_savings():
                print(strat)
        elif ch == "0":
            break

# === Treatment Plants === #
def treatment_menu():
    while True:
        print("\n--- Treatment Plants ---")
        print("1. Add Plant")
        print("2. Remove Plant")
        print("3. Show All Plants")
        print("4. Pending Plants")
        print("5. Operational Plants")
        print("6. Update Status")
        print("7. Total Treatment Capacity")
        print("8. Plants by Location")
        print("9. Sorted by Capacity")
        print("0. Back")
        ch = input("Enter choice: ")

        if ch == "1":
            plant = {
                "id": input("ID: "),
                "location": input("Location: "),
                "capacity": int(input("Capacity (L/day): ")),
                "status": input("Status: ")
            }
            treatment.add_plant(plant)
        elif ch == "2":
            treatment.remove_plant(input("ID: "))
        elif ch == "3":
            treatment.print_summary()
        elif ch == "4":
            print(treatment.get_pending_plants())
        elif ch == "5":
            print(treatment.get_operational_plants())
        elif ch == "6":
            print("Updated:", treatment.update_status(input("ID: "), input("New Status: ")))
        elif ch == "7":
            print("Total Capacity:", treatment.get_total_treatment_capacity(), "L/day")
        elif ch == "8":
            print(treatment.get_plants_by_location(input("Location: ")))
        elif ch == "9":
            for p in treatment.sort_by_capacity():
                print(p)
        elif ch == "0":
            break

    while True:
        print("\n--- Treatment Plans ---")
        print("1. Add Plan")
        print("2. Remove Plan")
        print("3. Show All Plans")
        print("4. Pending Plans")
        print("5. Completed Plans")
        print("6. Update Status")
        print("7. Total Volume Treated")
        print("8. Plans by Location")
        print("9. Sorted by Volume")
        print("0. Back")
        ch = input("Enter choice: ")

        if ch == "1":
            plan = {
                "id": input("ID: "),
                "type": input("Type: "),
                "location": input("Location: "),
                "volume_treated": int(input("Volume Treated: ")),
                "status": input("Status: ")
            }
            treatment.add_plan(plan)
        elif ch == "2":
            treatment.remove_plan(input("ID: "))
        elif ch == "3":
            treatment.print_summary()
        elif ch == "4":
            print(treatment.get_pending_plans())
        elif ch == "5":
            print(treatment.get_completed_plans())
        elif ch == "6":
            print("Updated:", treatment.update_status(input("ID: "), input("New Status: ")))
        elif ch == "7":
            print("Total Treated:", treatment.get_total_treated_volume(), "L")
        elif ch == "8":
            print(treatment.get_plans_by_location(input("Location: ")))
        elif ch == "9":
            for p in treatment.sort_by_volume():
                print(p)
        elif ch == "0":
            break

# === Usage Monitoring === #
def usage_menu():
    while True:
        print("\n--- Usage Monitoring ---")
        print("1. Add Usage Entry")
        print("2. Remove Entry")
        print("3. Show All Entries")
        print("4. Usage by User")
        print("5. Usage by Sector")
        print("6. High Consumers")
        print("7. Update Consumption")
        print("8. Total Usage")
        print("9. Average Usage")
        print("0. Back")
        ch = input("Enter choice: ")

        if ch == "1":
            u = {
                "id": input("ID: "),
                "user_id": input("User ID: "),
                "sector": input("Sector: "),
                "amount": int(input("Amount (L): "))
            }
            usage.add_usage_entry(u)
        elif ch == "2":
            usage.remove_entry(input("ID: "))
        elif ch == "3":
            usage.print_summary()
        elif ch == "4":
            print(usage.get_usage_by_user(input("User ID: ")))
        elif ch == "5":
            print(usage.get_usage_by_sector(input("Sector: ")))
        elif ch == "6":
            print(usage.get_high_consumers(int(input("Threshold (L): "))))
        elif ch == "7":
            print("Updated:", usage.update_consumption(input("ID: "), int(input("New Amount: "))))
        elif ch == "8":
            print("Total Usage:", usage.get_total_usage(), "L")
        elif ch == "9":
            print("Average Usage:", usage.get_average_usage(), "L")
        elif ch == "0":
            break

# === Distribution System === #
def distribution_menu():
    while True:
        print("\n--- Distribution System ---")
        print("1. Add Route")
        print("2. Remove Route")
        print("3. Show All Routes")
        print("4. Routes by Status")
        print("5. Routes by Area")
        print("6. High Loss Routes")
        print("7. Update Flow Rate")
        print("8. Total Distributed Volume")
        print("9. Average Loss")
        print("0. Back")
        ch = input("Enter choice: ")

        if ch == "1":
            r = {
                "id": input("ID: "),
                "area": input("Area: "),
                "volume": int(input("Volume (L): ")),
                "flow_rate": int(input("Flow Rate (L/min): ")),
                "loss": int(input("Loss (L): ")),
                "status": input("Status: ")
            }
            distribution.add_route(r)
        elif ch == "2":
            distribution.remove_route(input("ID: "))
        elif ch == "3":
            distribution.print_summary()
        elif ch == "4":
            print(distribution.get_routes_by_status(input("Status: ")))
        elif ch == "5":
            print(distribution.get_routes_by_area(input("Area: ")))
        elif ch == "6":
            print(distribution.get_high_loss_routes(int(input("Loss Threshold: "))))
        elif ch == "7":
            print("Updated:", distribution.update_flow_rate(input("ID: "), int(input("New Flow Rate: "))))
        elif ch == "8":
            print("Total Distributed:", distribution.get_total_distributed_volume(), "L")
        elif ch == "9":
            print("Average Loss:", distribution.calculate_average_loss(), "L")
        elif ch == "0":
            break

# === Run the System === #
def run():
    while True:
        main_menu()
        choice = input("Select option: ")

        if choice == "1":
            source_menu()
        elif choice == "2":
            conservation_menu()
        elif choice == "3":
            treatment_menu()
        elif choice == "4":
            usage_menu()
        elif choice == "5":
            distribution_menu()
        elif choice == "0":
            print("Exiting Water Management System. Goodbye!")
            break
        else:
            print("Invalid input.")

# Demo data for Source Management
source_mgmt.sources = [
    {"id": 1, "type": "river", "location": (28.6, 77.2), "capacity": 10000, "current_level": 7000, "quality": "good", "status": "active"},
    {"id": 2, "type": "lake", "location": (26.8, 75.8), "capacity": 8000, "current_level": 3000, "quality": "moderate", "status": "inactive"}
]

# Demo data for Conservation Strategy
conservation.strategies = [
    {"id": "C1", "name": "Rainwater Harvesting", "target_area": "Sector A", "savings": 2000, "status": "active"},
    {"id": "C2", "name": "Public Awareness", "target_area": "Sector B", "savings": 1500, "status": "completed"}
]

# Demo data for Treatment Plant
treatment = TreatmentPlant()
treatment.plants = [
    {"id": "T1", "location": "North Zone", "capacity": 5000, "status": "operational"},
    {"id": "T2", "location": "East Zone", "capacity": 3000, "status": "pending"}
]

# Demo data for Usage Monitoring
usage.usages = [
    {"id": "U1", "user_id": "user001", "sector": "residential", "amount": 1200},
    {"id": "U2", "user_id": "user002", "sector": "commercial", "amount": 3400}
]

# Demo data for Distribution System
distribution.routes = [
    {"id": "D1", "area": "Zone A", "volume": 4000, "flow_rate": 250, "loss": 100, "status": "active"},
    {"id": "D2", "area": "Zone B", "volume": 3000, "flow_rate": 200, "loss": 400, "status": "maintenance"}
]

# Start the app
run()
