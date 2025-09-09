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

def find_patient_by_id(patient_list, patient_id):
    """
    Searches for a patient in a list by their ID.
    Args:
        patient_list (list): A list of patient dictionaries.
        patient_id (str): The ID of the patient to find.
 
        dict or None: The patient dictionary if found, otherwise None.
    """
    for patient in patient_list:
        if patient["id"] == patient_id:
            return patient
    return None
# Sample patient data (a list of dictionaries)
hospital_patients = [
    {"id": "P001", "name": "Alice Smith", "age": 45, "condition": "Fever"},
    {"id": "P002", "name": "Bob Johnson", "age": 62, "condition": "Diabetes"},
    {"id": "P003", "name": "Charlie Brown", "age": 30, "condition": "Fracture"}
]
# Usage
found_patient = find_patient_by_id(hospital_patients, "P003")
if found_patient:
    print(f"Found patient: {found_patient['name']}")
else:
    print("Patient not found.")

