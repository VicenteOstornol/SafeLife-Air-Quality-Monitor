#!/bin/sh
# This script is used to deploy the application to the server
# It is called by a github action
# It is assumed that the server is already configured to accept ssh connections
# and that the server has the correct ssh key to connect to the server
touch key.pem
echo $AWS_SSH_KEY > key.pem
cat key.pem
chmod 400 key.pem
ssh -i key.pem $EC2_USER@$EC2_HOST "
cd $TARGET_DIR && git pull
source venv/bin/activate
pip install -r requirements.txt
cd project
python manage.py migrate
gunicorn -w 2 --bind :8000 project.wsgi:application &
exit
"
