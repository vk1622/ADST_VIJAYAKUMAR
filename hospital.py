patient_name = input("Enter patient name:")
requested_dept = input("Enter requested departments:")
requested_dept = requested_dept.split(",")
requested_dept = [dept.strip() for dept in requested_dept]

available_dept = input("Enter available departments:")
available_dept = available_dept.split(",")

visited_dept = input("Enter previously visited departments:")
visited_dept = visited_dept.split(",")

preferred_doctor = input("Enter preferred doctors:")
preferred_doctor = preferred_doctor.split(",")

available_doctor = input("Enter available doctor: ")
available_doctor = available_doctor.split(",")

emergency_dept = input("Enter emergency department:")
emergency_dept = emergency_dept.split(",")
emergency_dept = [dept.strip() for dept in emergency_dept]


requested_set = set(requested_dept)
available_set = set(available_dept)
visited_set = set(visited_dept)
preferred_doc_set = set(preferred_doctor)
available_doc_set = set(available_doctor)
emergency_set = set(emergency_dept)


common_dept = requested_set.intersection(available_set)
unavailable_dept = requested_set.difference(available_set)
visited_common = requested_set.intersection(visited_set)
common_doctor = preferred_doc_set.intersection(available_doc_set)
emergency_common = requested_set.intersection(emergency_set)
all_dept = requested_set.union(available_set)


if "Cardiology" in requested_set:
    print("Cardiology is requested.")

if "Cardiology" in available_set:
    print("Cardiology Available.")


duplicate_dept = []

for dept in requested_dept:
    if requested_dept.count(dept) > 1:
        if dept not in duplicate_dept:
            duplicate_dept.append(dept)


first_dept = requested_dept[0]

first_two_dept = requested_dept[:2]


requested_dept.append("General medicine")

if "General medicine" in requested_dept:
    requested_dept.remove("General medicine")


if len(emergency_common) > 0:
    recommended_dept = list(emergency_dept)[0]
    appointment_status = "Emergency appointment required"

elif len(common_dept) > 0:
    recommended_dept = list(common_dept)[0]
    appointment_status = "appointment can be scheduled"

else:
    recommended_dept = "Not Available"
    appointment_status = "Cannot schedule"


print("\n Final Appointment Report")
print("Patient Name", patient_name)
print("Requested department:", requested_dept)
print("Available department:", list(common_dept))
print("Unavailable departments:", list(unavailable_dept))
print("Common department:", list(common_dept))
print("Previous Department:", list(visited_common))
print("Duplicate Requests:", duplicate_dept)
print("Emergency:", list(emergency_common))
print("Recommended Department:", recommended_dept)
print("Final Status:", appointment_status)