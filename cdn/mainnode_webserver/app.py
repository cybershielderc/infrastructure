from flask import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           node_countries=[
                               ["us", "USA", "259"],
                               ["il", "Israel", "269"],
                               ["de", "Germany", "299"],
                               ["jp", "Japan", "386"],
                               ["ru", "Russia", "102"],
                               ["br", "Brazil", "25"],
                           ],
                           latest_filetransactions=[
                               # File Hash ID , Incoming Node, Storing Node, File Size, Reroutes
                               ["8cc..81", "ECS-ND-004", "US-ND-0101", "12.7 MiB", "29", "approved"],
                               ["8dc..c4", "ECS-ND-005", "US-ND-0156", "13.7 MiB", "14", "rejected"],
                               ["8ec..c1", "ECS-ND-001", "JP-ND-0166", "17.7 MiB", "9", "rejected"],
                               ["8ac..dd", "ECS-ND-002", "RU-ND-0133", "16.7 MiB", "7", "rejected"],
                               ["2dc..e1", "ECS-ND-003", "RU-ND-0012", "1.7 MiB", "15", "approved"],
                               ["0dc..41", "ECS-ND-004", "IL-ND-0093", "0.7 MiB", "11", "approved"],
                               ["a0c..c1", "ECS-ND-004", "IL-ND-0027", "5.7 MiB", "56", "rejected"],
                               ["a4c..d1", "ECS-ND-007", "DE-ND-0056", "6.7 MiB", "34", "approved"],
                               ["e2c..a1", "ECS-ND-006", "BR-ND-0025", "7.7 MiB", "23", "rejected"],
                               ["12c..11", "ECS-ND-002", "US-ND-0202", "1.0 MiB", "12", "approved"],
                           ])


if __name__ == '__main__':
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain('fullchain.pem', 'privkey.pem')
    app.run(ssl_context=context,host='0.0.0.0',port=25560,debug=True)