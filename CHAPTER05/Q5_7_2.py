data = [
    ['0001', 'Male', 'Yamada', 'Tarou25', 'Tokyo'],
    ['0002', 'Male', 'Satou’,'Takeshi','25','Saitama'],
    ['0003', 'Female', 'Tanaka', 'Yuko', '27', 'Kanagawa'],
    ['0004', 'Male', 'Suzuki’,'Ichirou','35','Hokkaido']
]
data

member_information = {}

for recore in data:
    key = record[0]
    info = record[1:]
    member_information[key] = info

print('number', 'information', sep='\t')
for key, info in member_information.items():
    print(key, info)