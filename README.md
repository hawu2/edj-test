# edj-test

## How to use it

python3 -m venv edjtest
cd edjtest
source activate
(in case upgrade pip required)  curl https://bootstrap.pypa.io/get-pip.py | python3			(upgrade TLS)
pip install behave
pip install selenium



## How to run it

### GUI test by Selenium:
Demo testing add an event.
cd GUI_test/features
behave test_add.feature

works with localhost only. not working with live server


### API Test by Selenium:
Todo


# Live Server:
https://edjuster.herokuapp.com/
Database backend change from derby to JawsDB MySQL: todo



