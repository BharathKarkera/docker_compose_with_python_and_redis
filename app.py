import flask
import redis

app=flask.Flask(__name__)
app.config["DEBUG"]=True

redis=redis.Redis(host='redis_server',port=6379)

@app.route('/display',methods=["GET"])
def display_function():
    redis.incr("hits")
    return f'Hi This is a test webserver and this is your {int(redis.get("hits"))}th visit to the website'

app.run(host="0.0.0.0")    
