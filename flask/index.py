from flask import Flask
from flaskext.mysql import MySQL
import json
from flask import Response, request
from passlib.hash import sha256_crypt
import jwt
from flask_cors import CORS
import time
import datetime
app = Flask(__name__)
# cors = CORS(app, resources={r"/api/=":{"orgins":"http://localhost:4200"}}) for deploying only 
CORS(app)


# add one
def createUserProfile():
  return "success"


def checkAuth(jwttoken):
  print(jwttoken)
  if (jwttoken):
    try:
      decoded = jwt.decode(jwttoken, 'memMEBER&&##Data$@#^&#@&#^@&#', algorithms='HS256')
      return True

    except:
      return False
    return True
  else:
    return False

# login
def encryptPassword(password):
  return sha256_crypt.hash(password)


def verifyPasswords(password, dbpassword):
  return sha256_crypt.verify(password, dbpassword)


# connection to mysql
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Newlife7'
app.config['MYSQL_DATABASE_DB'] = 'members'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)



@app.route('/members', methods=['GET'])
def membersList():
  conn = mysql.connect()
  cursor = conn.cursor()

  # # if check for firstName and lastName
  # # if False:
  # else:
  cursor.execute(
    "SELECT firstName, lastName, reason_for_payment, amount, payment_months, todaydate, received_by from membersForm;") 
  returnData = []
  data = cursor.fetchall()
  for info in data:
    userObject = {"firstName": info[0], "lastName": info[1], "reason_for_payment": info[2], "amount": info[3],
                  "payment_months": info[4], "todaydate": info[5], "received_by": info[6]}
    returnData.append(userObject)
  # it has to be out of the loop
  jsonResult = json.dumps(returnData, indent=4, sort_keys=True, default=str)
  return Response(jsonResult, mimetype='application/json')
  # else:


#     return Response(json.dumps({"status": False, "message": "Token not valid"}), mimetype='application/json')


@app.route('/members', methods=['POST'])
def addMembers():
  conn = mysql.connect()
  cursor = conn.cursor()

  data_members = json.loads(request.data)
  firstName = data_members.get('first_name', None)
  lastName = data_members.get('last_name', None)
  reason_for_payment = data_members.get('reason', None)
  amount = data_members.get('amount', None)
  payment_months = data_members.get('payment_month', None)
  todaydate = data_members.get('todaydate', datetime.datetime.today().strftime('%Y-%m-%d'))
  received_by = data_members.get('received_by', None)

  if not firstName:
    return Response(json.dumps({'status': False, 'message': 'First Name is required'}), mimetype='application/json')
  if not lastName:
    return Response(json.dumps({'status': False, 'message': 'Last Name is required'}), mimetype='application/json')
  if not reason_for_payment:
    return Response(json.dumps({'status': False, 'message': 'Reason for payment is required'}),
                    mimetype='application/json')
  if not amount:
    return Response(json.dumps({'status': False, 'message': 'Amount of payment is required'}),
                    mimetype='application/json')

  # try:
  print(todaydate)
  cursor.execute(
    "INSERT INTO membersForm (firstName, lastName, reason_for_payment, amount, payment_months, todaydate, received_by) VALUE (%s,%s,%s,%s,%s,%s,%s)",
    (firstName, lastName, reason_for_payment, amount, payment_months, todaydate, received_by))
  conn.commit()
  return Response(json.dumps({"status": True}), mimetype='application/json')
  # except Exception, e:
  #   return Response(json.dumps({"status": False, 'message': str(e)}), mimetype='application/json')


@app.route('/createUser', methods=['POST'])
def createLoginUser():
  conn = mysql.connect()
  cursor = conn.cursor()
  # table data type was wrong---date
  data_members = json.loads(request.data)
  print(data_members)
  name = data_members.get('name', None)
  sex = data_members.get('sex', None)
  birth = data_members.get('birth', None)
  password = data_members.get('password', None)
  username = data_members.get('username', None)

  if not username:
    return Response(json.dumps({"status": False, "message": "User Name Required"}), mimetype='application/json')

  if not password:
    return Response(json.dumps({"status": False, "message": "Password Required"}), mimetype='application/json')
  try:
    # addtwo-->password = encryptPassword(password)
    password = encryptPassword(password)
    cursor.execute("INSERT INTO users (name, sex, birth, username, password) VALUE (%s,%s,%s,%s,%s)",
                   (name, sex, birth, username, password))
    conn.commit()
    return Response(json.dumps({"status": True}), mimetype='application/json')
  except Exception, e:
    return Response(json.dumps({"status": False, 'message': str(e)}), mimetype='application/json')


@app.route('/login', methods=['POST'])
def loginUser():
  conn = mysql.connect()
  cursor = conn.cursor()

  data_members = json.loads(request.data)
  print(data_members)
  username = data_members.get('username', None)
  password = data_members.get('password', None)

  if not username:
    return Response(json.dumps({"status": False, "message": "User Name Required"}), mimetype='application/json')

  if not password:
    return Response(json.dumps({"status": False, "message": "Password Required"}), mimetype='application/json')
  try:
    cursor.execute("SELECT * from users WHERE username  = %s", (username))
    info = cursor.fetchone()
    print(info)
    if info is None:
      return Response(json.dumps({"status": False, "message": "User Name is not valid"}), mimetype='application/json')

    dbpassword = info[5]
    isValidPassword = verifyPasswords(password, dbpassword)

    if not isValidPassword:
      return Response(json.dumps({"status": False, "message": "Invalid Password"}), mimetype='application/json')

    # birthdate = False
    # if info[2]:
    #     birthdate= time.mktime(info[2].timetuple())
# "'unicode' object has no attribute 'timetuple'"---index error
    returnMembersData = {
      "id": info[0],
      "name": info[1],
      "birthdate": time.mktime(info[3].timetuple()),
      # "birthdate": birthdate,
      "sex": info[2]
    }
    print(returnMembersData)
  #when coding need the algoriths but encoding need list :- 'HS256' need to be string
    encoded = jwt.encode(returnMembersData, 'memMEBER&&##Data$@#^&#@&#^@&#', algorithm='HS256')
    print(encoded)
    return Response(json.dumps({"status": True, "token": encoded}), mimetype='application/json')

  except Exception as e:
    return Response(json.dumps({"status": False, "message": str(e)}), mimetype='application/json')


@app.route('/social-login', methods=['POST'])
def socialLogin():
  conn = mysql.connect()
  cursor = conn.cursor()
  # 1.update the item we need to see
  data_members = json.loads(request.data)
  print(data_members)
  id_user = data_members.get('id', None)
  email = data_members.get('email', None)
  image = data_members.get('image', None)
  name = data_members.get('name', None)
  # 2.change the required filed and create a column in the table THIS CODE WILL CHECK IF A USER EXIST
  if not id_user:
    return Response(json.dumps({"status": False, "message": "Facebook ID Required"}), mimetype='application/json')

  if not email:
    return Response(json.dumps({"status": False, "message": "Email Required"}), mimetype='application/json')
  try:
    cursor.execute("SELECT * from users WHERE id_user = %s", (id_user))
    info = cursor.fetchone()
    # 3.if the id is not valied and a first time visiter create insert the new user
    if info is None:
      try:
        cursor.execute(
          "INSERT INTO users (name, sex, username, password, id_user, image, email) VALUES (%s, %s, %s, %s, %s, %s, %s)",
          (name, 'D', '', '', id_user, image, email))
        conn.commit()
        cursor.execute("SELECT * from users WHERE id_user = %s", (id_user))
        info = cursor.fetchone()
      except Exception, e:
        return Response(json.dumps({"status": False, "message": str(e)}), mimetype='application/json')
    # 4. if we have user we will return the data
    returnMembersData = {
      "id": info[0],
      "name": info[1],
      "birthdate": False,
      "sex": info[2],
      "id_user": info[5],
      "image": info[3],
      "email": info[7],
    }
    # Here wew are creating the token
    encoded = jwt.encode(returnMembersData, 'memMEBER&&##Data$@#^&#@&#^@&#', algorithm='HS256')

    return Response(json.dumps({"status": True, "token": encoded}), mimetype='application/json')
  except Exception as e:
    return Response(json.dumps({"status": False, "message": str(e)}), mimetype='application/json')
