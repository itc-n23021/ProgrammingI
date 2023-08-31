import random


def generate_students_data(num_students=10):
    """生徒名,身長,体重からなるデータをランダムに生成する

    引数 : num_student: 生徒の人数を取る
    戻り : num_student個のタプル (生徒名, 身長, 体重) からなるリスト

    データの内容
         生徒名 'nXX', XXは10から50のランダムの番号
         身長 150-190 cm からランダムに選んだ値
         体重 50-80 kg からランダムに選んだ値
    """
    student_date = []
    for i in range(num_students):
        name = "n" + str(random.randint(10, 50))
        height = random.randint(150, 190)
        weight = rnddom.randint(50, 80)
        students_data.append((name, height, weight))
        if i == 0:
            print("i, name, height, weight")
        if i < 2 or i == num_students - 1:
            print(i, name, height, weight)
        elif i == 2:
            print("...")
            return students_data

        students_data = generate_students_data(10)
