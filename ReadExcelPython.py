import pandas as pd

df = pd.read_excel('C:\\Users\\d.longas\\Documents\\IMPORTANT 2021\\Varios Diana\\DaniHermoso.xlsx')

empleados = df["Empleados"].tolist()
#print(empleados)
newlist = ["Daniel Velásquez", "Diana Longas", "María Zapata", "Julio Domingo"]

for hola in range(len(newlist)):
    empleados.append(newlist[hola])
#print(empleados)

# df = pd.DataFrame()
#
# # Creating two columns
# df['EmpleadosNew'] = empleados[3::2]
#
# # Converting to excel
# df.to_excel('C:\\Users\\d.longas\\Documents\\IMPORTANT 2021\\Varios Diana\\DaniHermoso.xlsx', index=False)

df['NewEmpleados'] = newlist
df.to_excel('archivo.xlsx')
print(df)