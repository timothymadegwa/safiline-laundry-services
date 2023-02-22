from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


'''
@app.route('/predict',methods=['POST'])
def predict():    

    return render_template('report.html', text='Client {} : Probability of repayment for {} {} {} on a loan of KES {} is: {} %'.format(customer_id, title, f_name, l_name, amt, output))
    
'''
if __name__ == "__main__":
    app.run(debug=False)