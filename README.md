# Construction Company Management System

A comprehensive Python-based management system for construction companies dealing in **Housing**, **Roads**, and **Designing Plans**.

## Features

### 🏗️ Housing Construction Management
- Manage residential, apartment, and villa projects
- Track housing units, materials, and workers
- Handle multiple housing types (residential, apartment, villa)
- Material inventory management
- Construction progress tracking

### 🛣️ Road Construction Management
- Highway, main road, and street project management
- Equipment allocation and tracking
- Road specifications (lanes, surface type)
- Maintenance scheduling
- Support for different road types and surfaces

### 📐 Design Plans
- Create and approve design plans for all project types
- Add detailed specifications to plans
- Track estimated costs and area
- Plan approval workflow
- Support for housing, road, and commercial designs

## Installation

No external dependencies required! This system uses only Python's standard library.

```bash
# Clone the repository
git clone https://github.com/alungamichael/Construction-.git
cd Construction-

# Run the main application
python3 construction_company.py
```

## Usage

### Quick Start

Run the main application to see a complete demonstration:

```bash
python3 construction_company.py
```

### Examples

The `examples/` directory contains specific use-case demonstrations:

#### Housing Projects Example
```bash
python3 examples/housing_example.py
```
Demonstrates:
- Creating residential and apartment projects
- Managing materials and workers
- Design plan assignment
- Project tracking

#### Road Projects Example
```bash
python3 examples/roads_example.py
```
Demonstrates:
- Highway and street construction
- Equipment management
- Road specifications
- Maintenance scheduling

#### Design Plans Example
```bash
python3 examples/design_plans_example.py
```
Demonstrates:
- Creating various design plans
- Adding specifications
- Approval workflow
- Plan tracking and reporting

### Code Example

```python
from construction_company import ConstructionCompany

# Create a construction company
company = ConstructionCompany("My Construction Co.")

# Create a design plan
plan = company.create_design_plan(
    plan_id="PLAN-001",
    plan_type="housing",
    description="Modern Family Home",
    area_sqft=2500.0,
    estimated_cost=350000.0
)
plan.add_specification("bedrooms", "3")
plan.approve_plan()

# Create a housing project
project = company.create_housing_project(
    project_id="PROJ-001",
    project_name="Greenview Homes",
    housing_type="residential",
    num_units=10
)

# Assign plan and start construction
project.assign_design_plan(plan)
project.add_materials("concrete", 200, "cubic yards")
project.start_construction(workers=20)

# Generate company report
print(company.generate_report())
```

## Project Structure

```
Construction-/
├── construction_company.py      # Main application and core classes
├── requirements.txt             # Python dependencies (none required)
├── README.md                    # This file
└── examples/                    # Usage examples
    ├── housing_example.py       # Housing project demonstrations
    ├── roads_example.py         # Road project demonstrations
    └── design_plans_example.py  # Design plan demonstrations
```

## Core Classes

### `ConstructionCompany`
Main management class for the entire construction company operations.

**Key Methods:**
- `create_design_plan()` - Create new design plans
- `create_housing_project()` - Create housing construction projects
- `create_road_project()` - Create road construction projects
- `generate_report()` - Generate comprehensive company report
- `get_all_projects()` - Get summary of all projects

### `DesignPlan`
Represents architectural and engineering design plans.

**Key Methods:**
- `add_specification()` - Add technical specifications
- `approve_plan()` - Approve the design plan
- `get_details()` - Get complete plan details

### `HousingProject`
Manages housing construction projects.

**Key Methods:**
- `assign_design_plan()` - Assign an approved design plan
- `add_materials()` - Add construction materials
- `start_construction()` - Begin construction with workers
- `complete_project()` - Mark project as completed
- `get_project_info()` - Get project details

### `RoadProject`
Manages road construction and maintenance projects.

**Key Methods:**
- `assign_design_plan()` - Assign an approved design plan
- `set_road_specs()` - Set road specifications (lanes, surface)
- `add_equipment()` - Add construction equipment
- `start_construction()` - Begin construction with workers
- `schedule_maintenance()` - Schedule road maintenance
- `complete_project()` - Mark project as completed
- `get_project_info()` - Get project details

## Requirements

- Python 3.6 or higher
- No external packages required (uses only Python standard library)

## Features Overview

### Housing Management
- ✅ Multiple housing types (residential, apartment, villa)
- ✅ Material tracking and inventory
- ✅ Worker assignment
- ✅ Design plan integration
- ✅ Project status tracking
- ✅ Cost estimation

### Road Management
- ✅ Multiple road types (highway, main road, street)
- ✅ Equipment management
- ✅ Lane and surface specifications
- ✅ Maintenance scheduling
- ✅ Worker and equipment allocation
- ✅ Project completion tracking

### Design Planning
- ✅ Multi-type support (housing, road, commercial)
- ✅ Detailed specifications
- ✅ Approval workflow
- ✅ Cost estimation
- ✅ Area calculations
- ✅ Creation date tracking

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available under the MIT License.

## Author

Michael Alunga

## Contact

For questions or support, please open an issue on GitHub.