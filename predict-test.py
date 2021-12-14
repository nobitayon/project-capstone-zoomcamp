import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

data ={
    'url':'https://www.thestatesman.com/wp-content/uploads/2017/08/1493458748-beauty-face-517.jpg'
}
result = requests.post(url , json =data).json()
print('Probability that person in image using glasses is' , 1-result[0])
