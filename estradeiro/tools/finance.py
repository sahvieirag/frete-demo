def calculate_net_profit(freight_value: float, fuel_cost: float, toll_cost: float, other_costs: float = 0.0) -> float:
    """
    Calculates the net profit for a trip.
    
    Args:
        freight_value: Total value received for the freight
        fuel_cost: Estimated fuel cost
        toll_cost: Estimated toll cost
        other_costs: Other costs (food, maintenance share, etc.)
        
    Returns:
        Net profit value.
    """
    return round(freight_value - (fuel_cost + toll_cost + other_costs), 2)
