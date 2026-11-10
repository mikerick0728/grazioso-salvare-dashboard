# Grazioso Salvare Rescue Dog Identification Dashboard

## About the Project
This project is a full stack software application developed for Grazioso Salvare, an international rescue animal training company. The application serves as an interactive web dashboard that interfaces with a backend MongoDB database. It allows users to query, filter, and visualize an extensive dataset of shelter animals from the Austin Animal Center. The system uses a Model-View-Controller architecture, utilizing a custom Python CRUD module to manipulate the database and the Dash framework to present a dynamic, user friendly interface.

## Motivation
Grazioso Salvare identifies specific dogs that are strong candidates for search and rescue training, typically dogs under two years old belonging to specific breeds. The motivation behind this project is to provide the client with an intuitive tool to automatically filter thousands of shelter records into viable candidates for Water Rescue, Mountain Rescue, and Disaster Tracking. By presenting this data visually through interactive tables and geolocation mapping, the dashboard reduces user error, minimizes training time, and accelerates the process of identifying dogs that can save lives[cite: 1]. This project is open source so other rescue organizations can adapt it for their own operations[cite: 1].

## Getting Started
To get a local copy up and running, you will need a Python execution environment (such as Jupyter Notebook or a standard IDE) and a local instance of MongoDB[cite: 1].
1. Start your MongoDB background service[cite: 1].
2. Import the `aac_shelter_outcomes.csv` dataset into a MongoDB database named `aac` and a collection named `animals`[cite: 1].
3. Ensure you have an authenticated database user account configured with read and write privileges[cite: 1].
4. Place the `CRUD_Python_Module.py` and `ProjectTwoDashboard.ipynb` files in the same working directory[cite: 1].

## Installation
The following tools and libraries are required to run this software:
* **MongoDB**: The NoSQL database used for the data model[cite: 1].
* **Python 3.x**: The core programming language[cite: 1].
* **PyMongo**: The official MongoDB driver for Python[cite: 1].
* **Dash & Plotly**: Frameworks for building the interactive web application widgets and pie charts[cite: 1].
* **Dash Leaflet**: Library for rendering the interactive geolocation map[cite: 1].
* **Pandas**: Used for converting database cursors into structured dataframes[cite: 1].

Install the required Python dependencies via your terminal: 
`pip install pymongo dash dash-leaflet plotly pandas jupyter-dash`[cite: 1]

## Usage
The dashboard is designed to be highly intuitive[cite: 1]. Upon launching the application, the user is presented with a set of radio buttons representing the three primary rescue training categories, plus a Reset option[cite: 1].

When a user selects a filter (for example, Water Rescue):
1. The Dash controller triggers a callback function[cite: 1].
2. The controller passes a specific database query to the Python CRUD module[cite: 1].
3. The CRUD module retrieves only the dogs matching the specific breeds, age ranges, and sexes required for that rescue type[cite: 1].
4. The application dynamically updates the interactive Data Table, the Pie Chart (showing the distribution of available breeds), and the Leaflet Geolocation Map (pinpointing the physical location of the currently selected dog)[cite: 1].

Users can also sort the data table by specific columns, paginate through results, and select individual rows to update the geographic map marker[cite: 1].

## Code Example
```python
@app.callback(
    Output('datatable-id', 'data'),
    [Input('filter-type', 'value')]
)
def update_dashboard(filter_type):
    query = {}
    
    if filter_type == 'Water Rescue':
        query = {
            "breed": {"$in": ["Labrador Retriever Mix", "Chesapeake Bay Retriever", "Newfoundland"]},
            "sex_upon_outcome": "Intact Female",
            "age_upon_outcome_in_weeks": {"$gte": 26.0, "$lte": 156.0}
        }
        
    dff = pd.DataFrame.from_records(db.read(query))
    
    if '_id' in dff.columns:
        dff.drop(columns=['_id'], inplace=True)
        
    return dff.to_dict('records')
