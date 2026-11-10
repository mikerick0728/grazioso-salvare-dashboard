# Grazioso Salvare Rescue Dog Identification Dashboard

## About the Project
This project is a full stack software application developed for Grazioso Salvare, an international rescue animal training company. The application serves as an interactive web dashboard that interfaces with a backend MongoDB database. It allows users to query, filter, and visualize an extensive dataset of shelter animals from the Austin Animal Center. The system uses a Model-View-Controller architecture, utilizing a custom Python CRUD module to manipulate the database and the Dash framework to present a dynamic, user friendly interface.

## Motivation
Grazioso Salvare identifies specific dogs that are strong candidates for search and rescue training, typically dogs under two years old belonging to specific breeds. The motivation behind this project is to provide the client with an intuitive tool to automatically filter thousands of shelter records into viable candidates for Water Rescue, Mountain Rescue, and Disaster Tracking. By presenting this data visually through interactive tables and geolocation mapping, the dashboard reduces user error, minimizes training time, and accelerates the process of identifying dogs that can save lives. This project is open source so other rescue organizations can adapt it for their own operations.

## Getting Started
To get a local copy up and running, you will need a Python execution environment (such as Jupyter Notebook or a standard IDE) and a local instance of MongoDB.
1. Start your MongoDB background service.
2. Import the `aac_shelter_outcomes.csv` dataset into a MongoDB database named `aac` and a collection named `animals`.
3. Ensure you have an authenticated database user account configured with read and write privileges.
4. Place the `animal_shelter.py` and `ProjectTwoDashboard.ipynb` files in the same working directory.

## Installation
The following tools and libraries are required to run this software:
* **MongoDB**: The NoSQL database used for the data model.
* **Python 3.x**: The core programming language.
* **PyMongo**: The official MongoDB driver for Python.
* **Dash & Plotly**: Frameworks for building the interactive web application widgets and pie charts.
* **Dash Leaflet**: Library for rendering the interactive geolocation map.
* **Pandas**: Used for converting database cursors into structured dataframes.

Install the required Python dependencies via your terminal: 
`pip install pymongo dash dash-leaflet plotly pandas jupyter-dash`

## Usage
The dashboard is designed to be highly intuitive. Upon launching the application, the user is presented with a set of radio buttons representing the three primary rescue training categories, plus a Reset option.

When a user selects a filter (for example, Water Rescue):
1. The Dash controller triggers a callback function.
2. The controller passes a specific database query to the Python CRUD module.
3. The CRUD module retrieves only the dogs matching the specific breeds, age ranges, and sexes required for that rescue type.
4. The application dynamically updates the interactive Data Table, the Pie Chart (showing the distribution of available breeds), and the Leaflet Geolocation Map (pinpointing the physical location of the currently selected dog).

Users can also sort the data table by specific columns, paginate through results, and select individual rows to update the geographic map marker.

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
