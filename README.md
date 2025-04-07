💧 1. SourceManagement
Purpose: Manage and monitor water sources
Data Used: sources list with info like type, capacity, current level, quality, and status
Example Functions:
1.	add_source(): Add a new water source
2.	remove_source(source_id): Remove an existing source
3.	get_active_sources(): Return all active sources
4.	update_level(source_id, new_level): Update current water level
5.	check_quality(source_id): Return water quality of a source
6.	get_total_capacity(): Sum of capacities of all sources
7.	get_available_water(): Sum of current levels
8.	deactivate_source(source_id): Mark a source as inactive
9.	get_sources_by_type(type): Filter sources by type
10.	print_summary(): Print a summary of all sources

🚰 2. DistributionSystem
Purpose: Manage water flow across zones
Data Used: distribution_zones list with flow rate, pressure, leaks, consumption
Example Functions:
1.	add_zone(): Add a new distribution zone
2.	get_zone_info(zone_id): Get details of a specific zone
3.	update_flow_rate(zone_id, new_rate): Change flow rate
4.	report_leak(zone_id): Increment leak count
5.	repair_leak(zone_id): Decrement leak count
6.	get_total_consumption(): Total water consumed across zones
7.	get_zones_with_low_pressure(): Filter zones with low pressure
8.	schedule_maintenance(zone_id): Schedule maintenance
9.	get_high_consumption_zones(threshold): Return zones exceeding a threshold
10.	print_summary(): Summary of distribution network

📊 3. UsageMonitor
Purpose: Monitor individual usage patterns
Data Used: usage_data list with user type, daily/monthly usage, alerts
Example Functions:
1.	add_user(): Add a new user
2.	remove_user(user_id): Remove user
3.	update_usage(user_id, daily): Update daily/monthly usage
4.	generate_bill(user_id): Calculate a bill based on usage
5.	check_overuse(user_id): Flag over-usage
6.	get_household_users(): Filter households
7.	get_industrial_users(): Filter industries
8.	get_total_usage(): Sum of all users' usage
9.	get_usage_pattern(user_id): Return pattern (if stored over time)
10.	print_summary(): Print report of all users

🧪 4. TreatmentPlant
Purpose: Track purification processes
Data Used: treatment_plants with inflow/outflow, quality, energy usage
Example Functions:
1.	add_plant(): Add new treatment plant
2.	remove_plant(plant_id): Remove plant
3.	update_inflow_outflow(plant_id, inflow, outflow): Update water flow
4.	calculate_efficiency(plant_id): (outflow / inflow) * 100
5.	get_quality_change(plant_id): Compare before vs after
6.	total_energy_usage(): Sum energy across all plants
7.	get_underperforming_plants(): Plants with < 80% efficiency
8.	get_high_efficiency_plants(): Plants with high efficiency
9.	get_plant_info(plant_id): Fetch all data for a plant
10.	print_summary(): Print treatment stats

🌿 5. ConservationStrategy
Purpose: Plan and track conservation efforts
Data Used: strategies list with name, target area, savings, and status
Example Functions:
1.	add_strategy(): Add new conservation strategy
2.	remove_strategy(strategy_id): Remove it
3.	get_strategy(strategy_id): Fetch data
4.	update_status(strategy_id, status): Change progress
5.	get_active_strategies(): Filter in-progress strategies
6.	calculate_total_savings(): Total estimated savings
7.	get_completed_strategies(): Completed ones
8.	get_strategies_by_area(area): Filter by target area
9.	sort_by_savings(): Strategies sorted by savings
10.	print_summary(): Print conservation efforts overview


////////////////////////////////////////////////////////////////
💧 1. SourceManagement
Manages details about water sources
Possible Data:
•	Source ID
•	Source type (River, Borewell, Lake, Rainwater, etc.)
•	Location (latitude, longitude)
•	Capacity (liters/day)
•	Current level
•	Quality rating
•	Operational status (Active/Inactive)
Example:
python
CopyEdit
sources = [
    {"id": 1, "type": "River", "location": (23.1, 77.2), "capacity": 100000, "current_level": 80000, "quality": "Good", "status": "Active"},
    {"id": 2, "type": "Borewell", "location": (22.8, 77.0), "capacity": 20000, "current_level": 12000, "quality": "Fair", "status": "Active"}
]

🚰 2. DistributionSystem
Tracks water distribution across zones
Possible Data:
•	Zone ID
•	Pipelines connected
•	Flow rate (liters/sec)
•	Pressure levels
•	Leak reports
•	Consumption per zone
•	Maintenance schedule
Example:
python
CopyEdit
distribution_zones = [
    {"zone_id": "A", "flow_rate": 50, "pressure": "Normal", "leaks": 1, "consumption": 25000},
    {"zone_id": "B", "flow_rate": 40, "pressure": "Low", "leaks": 2, "consumption": 18000}
]

📊 3. UsageMonitor
Monitors household/industrial water usage
Possible Data:
•	User ID
•	Type (Household/Industry)
•	Daily/Monthly usage (liters)
•	Over-usage alerts
•	Bill generated
•	Usage patterns
Example:
python
CopyEdit
usage_data = [
    {"user_id": "U001", "type": "Household", "daily_usage": 150, "monthly_usage": 4500, "alerts": False},
    {"user_id": "U002", "type": "Industry", "daily_usage": 1200, "monthly_usage": 36000, "alerts": True}
]

🧪 4. TreatmentPlant
Manages water purification and treatment
Possible Data:
•	Plant ID
•	Location
•	Capacity (liters/day)
•	Chemicals used
•	Water inflow/outflow
•	Quality before & after treatment
•	Energy used
Example:
python
CopyEdit
treatment_plants = [
    {"plant_id": "TP01", "location": "Sector 5", "capacity": 50000, "inflow": 45000, "outflow": 44000, "energy": 1200, "quality_before": "Poor", "quality_after": "Good"},
    {"plant_id": "TP02", "location": "Zone A", "capacity": 30000, "inflow": 28000, "outflow": 27000, "energy": 950, "quality_before": "Fair", "quality_after": "Excellent"}
]

🌿 5. ConservationStrategy
Handles plans for water saving and sustainability
Possible Data:
•	Strategy ID
•	Name (Rainwater harvesting, Smart irrigation, etc.)
•	Target area
•	Estimated savings
•	Implementation status
•	Awareness campaign dates
Example:
python
CopyEdit
strategies = [
    {"id": "S001", "name": "Rainwater Harvesting", "target_area": "Sector 9", "savings": 15000, "status": "In Progress"},
    {"id": "S002", "name": "Smart Irrigation", "target_area": "Farms A, B", "savings": 22000, "status": "Completed"}
]


