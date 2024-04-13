# QuoDroidAssignment

## Steps to run the app
1. There is a requirements.text file that contains the name of the libraries to install. Run the command **pip install -r requirements.txt** to install the library.
2. Run the command **python manage.py runserver** to start the server.
3. There is a **postman collection** json file, import it in the Postman application and hit the send button.

## Description
This app contains a **Django API** in the **automate** folder. It executes the test cases present in the request body of the post request. It creates a **dynamic_test.robot** file in the **test** folder and creates result files in the **result folder** after the execution of the test cases.
