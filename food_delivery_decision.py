
print("=== Food Delivery Order Decision System ===")

order_amount = float(input("Order amount (Rs.): "))
delivery_distance = float(input("Delivery distance (km): "))
customer_type = input("Customer type (regular/premium/new): ").strip().lower()
demand_level = input("Demand level (low/medium/high): ").strip().lower()
restaurant_rating = float(input("Restaurant rating (1.0 to 5.0): "))
prep_time = int(input("Estimated preparation time (minutes): "))
payment_method = input("Payment method (online/cod): ").strip().lower()
weather_condition = input("Weather (clear/rain/storm): ").strip().lower()
peak_hour = input("Is it peak hour? (yes/no): ").strip().lower()
previous_cancellations = int(input("Previous cancellations: "))

decision = "ACCEPTED"
decision_reason = "Order meets the standard delivery conditions."
delivery_charge = 30.0
discount = 0.0
priority_status = "Normal"
cancellation_risk = "Low"
restaurant_status = "Available"

if restaurant_rating < 2.5:
    restaurant_status = "Needs quality review"
elif restaurant_rating < 3.5:
    restaurant_status = "Available with caution"
else:
    restaurant_status = "Available"

if previous_cancellations >= 5:
    cancellation_risk = "High"
elif previous_cancellations >= 2:
    cancellation_risk = "Medium"
else:
    cancellation_risk = "Low"

if delivery_distance > 12:
    delivery_charge = 90.0
elif delivery_distance > 8:
    delivery_charge = 70.0
elif delivery_distance > 5:
    delivery_charge = 50.0
else:
    delivery_charge = 30.0

if weather_condition == "rain":
    delivery_charge = delivery_charge + 15.0
elif weather_condition == "storm":
    delivery_charge = delivery_charge + 35.0
else:
    delivery_charge = delivery_charge

if peak_hour == "yes" and demand_level == "high":
    delivery_charge = delivery_charge + 20.0
elif peak_hour == "yes":
    delivery_charge = delivery_charge + 10.0
else:
    delivery_charge = delivery_charge

if customer_type == "premium":
    discount = order_amount * 0.10
    priority_status = "High"
elif customer_type == "new" and order_amount >= 300:
    discount = order_amount * 0.05
    priority_status = "Normal"
elif customer_type == "regular" and order_amount >= 800:
    discount = order_amount * 0.03
    priority_status = "Normal"
else:
    discount = 0.0
    priority_status = "Normal"

if demand_level == "high" and peak_hour == "yes":
    if customer_type == "premium" or order_amount >= 1000:
        priority_status = "High"
    else:
        priority_status = "Normal"
elif demand_level == "low":
    priority_status = "Standard"
else:
    priority_status = priority_status

if order_amount <= 0 or delivery_distance <= 0 or prep_time <= 0:
    decision = "REJECTED"
    decision_reason = "Order amount, distance, and preparation time must be positive."
elif weather_condition == "storm" and delivery_distance > 8:
    decision = "REJECTED"
    decision_reason = "Storm conditions make this long-distance delivery unsafe."
elif restaurant_rating < 2.5 and previous_cancellations >= 5:
    decision = "REJECTED"
    decision_reason = "Restaurant quality and customer cancellation risk are both too high."
elif delivery_distance > 15 or prep_time > 75:
    decision = "MANUAL REVIEW"
    decision_reason = "Long delivery distance or unusually high preparation time."
elif previous_cancellations >= 5:
    decision = "MANUAL REVIEW"
    decision_reason = "Customer has a high previous-cancellation history."
elif restaurant_rating < 3.0:
    decision = "MANUAL REVIEW"
    decision_reason = "Restaurant rating requires an operations check."
elif payment_method == "cod" and order_amount > 1500:
    decision = "MANUAL REVIEW"
    decision_reason = "High-value cash-on-delivery order requires verification."
elif demand_level == "high" and peak_hour == "yes" and prep_time > 45:
    decision = "MANUAL REVIEW"
    decision_reason = "High demand, peak hour, and long preparation time."
elif weather_condition == "storm":
    decision = "MANUAL REVIEW"
    decision_reason = "Storm conditions require a dispatcher check."
else:
    decision = "ACCEPTED"
    decision_reason = "Order meets the standard delivery conditions."

final_payable_amount = order_amount + delivery_charge - discount

print("\n=== Order Decision ===")
print("Decision:", decision)
print("Reason:", decision_reason)
print("Delivery charge: Rs.", format(delivery_charge, ".2f"))
print("Discount: Rs.", format(discount, ".2f"))
print("Priority status:", priority_status)
print("Cancellation risk:", cancellation_risk)
print("Restaurant status:", restaurant_status)
print("Final payable amount: Rs.", format(final_payable_amount, ".2f"))
