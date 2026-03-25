import pandas as pd

df = pd.DataFrame({
    "Nombre": ["Juan", "Ana"],
    "Edad": [25, 30]
})

df.to_excel("test.xlsx", index=False)
print("Excel creado")
