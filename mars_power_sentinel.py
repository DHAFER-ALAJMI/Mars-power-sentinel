# Project: Mars Power Sentinel
# Lead Developer: Dhafer Abdulhadi Alajmi
# Agency Target: NASA (Space Apps / Open Source)

class MarsPowerSentinel:
    """
    Predictive energy management system for Mars rovers.
    Analyzes solar efficiency and dust accumulation impact.
    Developed by: Dhafer Abdulhadi Alajmi
    """
    def __init__(self, rover_name="Dhafer-Explorer-1"):
        self.rover_name = rover_name
        self.base_efficiency = 0.22 
        self.dust_rate = 0.005 # Daily dust accumulation rate
        
    def analyze_mission(self, panel_area, daily_usage):
        print(f"--- NASA Project Control: {self.rover_name} ---")
        for day in range(1, 366, 30):
            # Efficiency decreases as dust accumulates over time
            current_efficiency = max(self.base_efficiency * (1 - (day * self.dust_rate)), 0)
            # Calculate energy generated based on Mars solar intensity
            energy_generated = panel_area * 590 * 8 * current_efficiency
            
            status = "STABLE" if energy_generated >= daily_usage else "CRITICAL"
            print(f"Sol {day:3}: Energy Produced: {energy_generated:7.2f}Wh | Status: {status}")
            
            if status == "CRITICAL":
                print(f"\n[!] Mission Risk: Power deficit detected at Sol {day}")
                break

if __name__ == "__main__":
    # Simulation: 2.5m solar panels, 450Wh daily consumption
    system = MarsPowerSentinel()
    system.analyze_mission(panel_area=2.5, daily_usage=450)
