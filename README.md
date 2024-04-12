# FastApi-practices

#### Background task

- Simple example of the use of background task ([sourcer](https://www.youtube.com/watch?v=IGb3xvIwRmk&list=WL&index=25&ab_channel=AmoProcedures))

	- to test the app:

		- execute **pip install requirements.txt** in a terminal
		- execute **uvicorn app:app --reaload** 
		- sed a POST request to http://localhost:8000/ with this body **{"title": "test", "body": "test body"}**