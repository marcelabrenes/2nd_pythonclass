# Desarrolle un programa que solicite la distancia de su casa a la U,
# el costo por kilometro, la cantidad de días a la semana que viaja a la U
# Y que calcule el costo total de trasladarse por cuatrimestre.
# Asuma que cada visita implica ida y vuelta y que el cuatri tiene 15 semanas.
distance=int(input("How far is the site from your house?(kilometers"))
cost=int(input("How much does it cost?"))
days_per_week=int(input("How many days you have to go the the site on a weekly basis?"))
total_distance= 2*(distance+cost)
total_days=days_per_week*15
result=total_distance*total_days
print("The moving cost for an entire forthmester is",result)