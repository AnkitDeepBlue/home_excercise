import json
import random
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Employee(BaseModel):
    name: str
    salary: int
    title: str


class Demployee(BaseModel):
    name: str


@app.post("/employees")
def add_employee(new_employee: Employee):
    # Generating unique id
    idlist = random.sample(range(1, 1000), 999)
    n = 0
    id = idlist[n]
    n = n + 1
    # reading json data and updating with new employee
    with open("entities.json", "r+") as file:
        content = json.load(file)
        temp = {new_employee.name: {"id": id, "title": new_employee.title, "salary": new_employee.salary}}
        content.update(temp)
    with open("entities.json", "w") as file:
        json.dump(content, file, indent=4)
        return temp


@app.get("/employees")
def get_employees() -> dict:
    with open("entities.json", "r") as file:
        content = json.load(file)
    return content


@app.delete("/employees")
def delete_employees(tgt: Demployee):
    try:
        employees = get_employees()
        del employees[tgt.name]
        with open("entities.json", "w") as file:
            json.dump(employees, file, indent=4)
    except KeyError:
        error_msz= 'Employee Not Found'
        print(error_msz)
    return tgt.name

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
