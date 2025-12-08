import pandas as pd
#membuat data frame
data = {
    'Nama': ['John', 'Jane', 'Bob', 'Alice'],
    'Usia' : [25, 30, 22, 28],
    'pelerjaan' : ["Engineer", 'Teacher', 'Designer', 'Doctor']
}
df = pd.DataFrame(data)

# menampilkan DataFrame
print(df)