# age = int(input("Enter Your Age ? : "))
#
# income = int(input("Enter Your Income ? : "))
#
#
# investments = input("Do u have any investments ? : ")
#
# total_invest = 0
# investmentcount = 0
#
# if(investments=='yes'):
#     inp = int(input("enter Total investments : "))
#     total_invest += inp
#     i = 1
#     while(total_invest>0):
#         total_invest -= 1
#         investmentcount += int(input(f"Enter expected return from {i} investment"))
#         i += 1
#
# govt_serv = input("Do u worked in govt service")
# pension = 0
# if(govt_serv=='yes'):
#     pension = int(input("Enter your expected pension"))
#
# expected_income = (60 - age)*income * 12 + (pension*12) + investmentcount
#
# print(f"your age {age} , your income is {income} , your investment {investments} , total invest = {total_invest} , do u govt serv{govt_serv},pension - {pension},")
#
# print(expected_income)

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_expected_income():
    if request.method == 'POST':
        age = int(request.form['age'])
        income = int(request.form['income'])
        investments = request.form['investments']
        total_invest = 0
        investmentcount = 0

        if investments == 'yes':
            total_invest = int(request.form['total_invest'])
            i = 1
            while total_invest > 0:
                investment_input = request.form.get(f'investment_{i}', 0)
                investmentcount += int(investment_input)
                total_invest -= 1
                i += 1

        govt_serv = request.form['govt_serv']
        pension = 0
        if govt_serv == 'yes':
            pension = int(request.form['pension'])

        expected_income = (60 - age) * income * 12 + (pension * 12) + investmentcount

        return render_template('result.html', age=age, income=income, investments=investments, total_invest=total_invest, govt_serv=govt_serv, pension=pension, expected_income=expected_income)

    return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)
