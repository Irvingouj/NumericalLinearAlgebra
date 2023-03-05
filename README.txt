# To Run The program

pip install -r requirements.txt

this will run all test
python3 -m unittest discover -s ./test/Lab3 -p '*test.py'

but problem 2 takes too long, so better specify the name by 
python3 -m unittest ./test/Problem1_test.py 
or 
python3 -m unittest ./test/Problem3_test.py 

for different problems