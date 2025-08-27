def get_gripping_force(object_weight_kg):
    """
    Determines the optimal gripping force for a robotic arm.
    Args:
        object_weight_kg (float): The weight of the object in kilograms.
    Returns:
        str: Description of the gripping force.
    """
    if object_weight_kg < 0.5:
        return "Light_Grip"
    elif 0.5 <= object_weight_kg < 2.0:
        return "Medium_Grip"
    else:
        return "Strong_Grip"

# Usage
item_weight = 4
grip_strength = get_gripping_force(item_weight)
print(f"Required gripping force: {grip_strength}")


