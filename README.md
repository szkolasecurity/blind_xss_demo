simple blind xss app

sudo docker build -t blindxss .

sudo docker run -p 5000:5000 --rm --name blindxss blindxss
