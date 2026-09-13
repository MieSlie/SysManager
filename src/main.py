import mng
import json

from flask import Flask, render_template, Response, request
app = Flask(__name__)

@app.route('/')
def main():
  return render_template('index.html')

@app.route('/ssh/<int:ip>')
def ssh(ip):
  mng.connect(ip,'root')
  return Response(status=200)

@app.route('/rdp/<int:ip>')
def rdp(ip):
  mng.rdp(ip,'<username>', '<password>')
  return Response(status=200)

@app.route('/off/<int:ip>')
def off(ip):
  mng.off(ip)
  return Response(status=200)


@app.route('/exec', methods=['POST'])
def exec():
  print(request.json)
  usr = request.json['usr']
  cmd = request.json['cmd']
  ids = request.json['ids']

  for id in ids:
    mng.off(id)
  print(ids)
  return Response(status=200)



if __name__ == '__main__':
  app.run(debug=True, port='2000')