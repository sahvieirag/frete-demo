import random
from typing import List, Dict, Optional

def search_freight(origin: str, destination: str, vehicle_type: str = "truck") -> List[Dict]:
    """
    Searches for available freight loads between origin and destination.
    
    Args:
        origin: City/State of origin (e.g., "São Paulo, SP")
        destination: City/State of destination (e.g., "Curitiba, PR")
        vehicle_type: Type of vehicle (truck, bitrem, carreta, truck_syder, etc.)
        
    Returns:
        List of dictionaries containing freight details.
    """
    # Mock data generation
    freights = []
    base_price = 4500.0  # Base price for simulation
    
    # Generate 3-5 mock options
    for i in range(random.randint(3, 5)):
        price = base_price * (0.8 + random.random() * 0.4) # vary price by +/- 20%
        weight = random.randint(10, 25) # tons
        
        freights.append({
            "id": f"FRT-{random.randint(1000, 9999)}",
            "origin": origin,
            "destination": destination,
            "product": random.choice(["Soja", "Eletrodomésticos", "Peças Automotivas", "Cimento", "Bebidas"]),
            "weight_tons": weight,
            "price": round(price, 2),
            "vehicle_type": vehicle_type,
            "company": random.choice(["TransLog", "RapidoCargo", "LogisticaBrasil", "FreteAgil"])
        })
        
    return freights

def calculate_toll(origin: str, destination: str, axles: int = 2) -> float:
    """
    Calculates the estimated toll cost for a route.
    
    Args:
        origin: City of origin
        destination: City of destination
        axles: Number of axles on the vehicle
        
    Returns:
        Estimated toll cost in BRL.
    """
    # Simple mock logic: random cost between 100 and 500 depending on "distance" (simulated)
    base_toll = random.uniform(50.0, 150.0)
    return round(base_toll * axles * 0.5, 2)

def estimate_fuel(distance_km: float, vehicle_type: str) -> float:
    """
    Estimates fuel cost based on distance and vehicle type.
    
    Args:
        distance_km: Distance in km
        vehicle_type: Type of vehicle
        
    Returns:
        Estimated fuel cost in BRL.
    """
    # Mock fuel prices and consumption
    diesel_price = 6.20
    
    consumption_km_l = 3.5 # average truck
    if "bitrem" in vehicle_type.lower():
        consumption_km_l = 2.0
    elif "truck" in vehicle_type.lower():
        consumption_km_l = 4.0
        
    liters_needed = distance_km / consumption_km_l
    return round(liters_needed * diesel_price, 2)

def get_distance(origin: str, destination: str) -> float:
    """
    Mock function to get distance between two cities.
    DEPRECATED: Use GoogleSearchTool for real distances.
    """
    # Return a random distance between 300 and 1500 km for demo
    return float(random.randint(300, 1500))
