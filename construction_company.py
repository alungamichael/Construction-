#!/usr/bin/env python3
"""
Construction Company Management System
Handles Housing, Roads, and Design Plans
"""

from datetime import datetime
from typing import List, Dict, Optional


class DesignPlan:
    """Represents a design plan for construction projects"""
    
    def __init__(self, plan_id: str, plan_type: str, description: str, 
                 area_sqft: float, estimated_cost: float):
        self.plan_id = plan_id
        self.plan_type = plan_type  # 'housing', 'road', 'commercial'
        self.description = description
        self.area_sqft = area_sqft
        self.estimated_cost = estimated_cost
        self.created_date = datetime.now()
        self.approved = False
        self.specifications = {}
    
    def add_specification(self, key: str, value: str):
        """Add technical specifications to the plan"""
        self.specifications[key] = value
    
    def approve_plan(self):
        """Approve the design plan"""
        self.approved = True
        return f"Plan {self.plan_id} approved on {datetime.now().strftime('%Y-%m-%d')}"
    
    def get_details(self) -> Dict:
        """Get plan details"""
        return {
            'plan_id': self.plan_id,
            'type': self.plan_type,
            'description': self.description,
            'area_sqft': self.area_sqft,
            'estimated_cost': self.estimated_cost,
            'approved': self.approved,
            'specifications': self.specifications,
            'created_date': self.created_date.strftime('%Y-%m-%d')
        }


class HousingProject:
    """Manages housing construction projects"""
    
    def __init__(self, project_id: str, project_name: str, 
                 housing_type: str, num_units: int):
        self.project_id = project_id
        self.project_name = project_name
        self.housing_type = housing_type  # 'residential', 'apartment', 'villa'
        self.num_units = num_units
        self.design_plan = None
        self.status = 'planned'  # planned, in_progress, completed
        self.start_date = None
        self.completion_date = None
        self.materials = []
        self.workers_assigned = 0
    
    def assign_design_plan(self, design_plan: DesignPlan):
        """Assign a design plan to the housing project"""
        if not design_plan.approved:
            return "Error: Design plan must be approved first"
        if design_plan.plan_type != 'housing':
            return f"Error: Design plan type '{design_plan.plan_type}' is not compatible with housing projects"
        self.design_plan = design_plan
        return f"Design plan {design_plan.plan_id} assigned to {self.project_name}"
    
    def start_construction(self, workers: int):
        """Start the construction process"""
        if self.design_plan and self.design_plan.approved:
            self.status = 'in_progress'
            self.start_date = datetime.now()
            self.workers_assigned = workers
            return f"Construction started for {self.project_name} with {workers} workers"
        else:
            return "Error: Approved design plan required to start construction"
    
    def add_materials(self, material: str, quantity: float, unit: str):
        """Add materials to the project"""
        self.materials.append({
            'material': material,
            'quantity': quantity,
            'unit': unit
        })
    
    def complete_project(self):
        """Mark project as completed"""
        self.status = 'completed'
        self.completion_date = datetime.now()
        return f"Housing project {self.project_name} completed on {self.completion_date.strftime('%Y-%m-%d')}"
    
    def get_project_info(self) -> Dict:
        """Get project information"""
        return {
            'project_id': self.project_id,
            'name': self.project_name,
            'type': self.housing_type,
            'units': self.num_units,
            'status': self.status,
            'workers': self.workers_assigned,
            'materials_count': len(self.materials),
            'has_design_plan': self.design_plan is not None
        }


class RoadProject:
    """Manages road construction and maintenance projects"""
    
    def __init__(self, project_id: str, road_name: str, 
                 road_type: str, length_km: float):
        self.project_id = project_id
        self.road_name = road_name
        self.road_type = road_type  # 'highway', 'main_road', 'street'
        self.length_km = length_km
        self.design_plan = None
        self.status = 'planned'  # planned, in_progress, completed, maintenance
        self.lanes = 2
        self.surface_type = 'asphalt'
        self.start_date = None
        self.completion_date = None
        self.workers_assigned = 0
        self.equipment = []
    
    def assign_design_plan(self, design_plan: DesignPlan):
        """Assign a design plan to the road project"""
        if not design_plan.approved:
            return "Error: Design plan must be approved first"
        if design_plan.plan_type != 'road':
            return f"Error: Design plan type '{design_plan.plan_type}' is not compatible with road projects"
        self.design_plan = design_plan
        return f"Design plan {design_plan.plan_id} assigned to {self.road_name}"
    
    def set_road_specs(self, lanes: int, surface_type: str):
        """Set road specifications"""
        self.lanes = lanes
        self.surface_type = surface_type
    
    def start_construction(self, workers: int):
        """Start the road construction"""
        if self.design_plan and self.design_plan.approved:
            self.status = 'in_progress'
            self.start_date = datetime.now()
            self.workers_assigned = workers
            return f"Road construction started for {self.road_name} with {workers} workers"
        else:
            return "Error: Approved design plan required to start construction"
    
    def add_equipment(self, equipment_name: str, quantity: int):
        """Add construction equipment"""
        self.equipment.append({
            'equipment': equipment_name,
            'quantity': quantity
        })
    
    def schedule_maintenance(self):
        """Schedule maintenance for the road"""
        if self.status == 'completed':
            self.status = 'maintenance'
            return f"Maintenance scheduled for {self.road_name}"
        else:
            return "Error: Road must be completed before scheduling maintenance"
    
    def complete_project(self):
        """Mark road project as completed"""
        self.status = 'completed'
        self.completion_date = datetime.now()
        return f"Road project {self.road_name} completed on {self.completion_date.strftime('%Y-%m-%d')}"
    
    def get_project_info(self) -> Dict:
        """Get road project information"""
        return {
            'project_id': self.project_id,
            'name': self.road_name,
            'type': self.road_type,
            'length_km': self.length_km,
            'lanes': self.lanes,
            'surface': self.surface_type,
            'status': self.status,
            'workers': self.workers_assigned,
            'equipment_count': len(self.equipment),
            'has_design_plan': self.design_plan is not None
        }


class ConstructionCompany:
    """Main Construction Company Management System"""
    
    def __init__(self, company_name: str):
        self.company_name = company_name
        self.housing_projects: List[HousingProject] = []
        self.road_projects: List[RoadProject] = []
        self.design_plans: List[DesignPlan] = []
        self.total_workers = 0
        self.active_projects = 0
    
    def create_design_plan(self, plan_id: str, plan_type: str, 
                          description: str, area_sqft: float, 
                          estimated_cost: float) -> DesignPlan:
        """Create a new design plan"""
        plan = DesignPlan(plan_id, plan_type, description, area_sqft, estimated_cost)
        self.design_plans.append(plan)
        return plan
    
    def create_housing_project(self, project_id: str, project_name: str,
                              housing_type: str, num_units: int) -> HousingProject:
        """Create a new housing project"""
        project = HousingProject(project_id, project_name, housing_type, num_units)
        self.housing_projects.append(project)
        return project
    
    def create_road_project(self, project_id: str, road_name: str,
                           road_type: str, length_km: float) -> RoadProject:
        """Create a new road project"""
        project = RoadProject(project_id, road_name, road_type, length_km)
        self.road_projects.append(project)
        return project
    
    def get_all_projects(self) -> Dict:
        """Get all projects summary"""
        in_progress_housing = sum(1 for p in self.housing_projects if p.status == 'in_progress')
        in_progress_roads = sum(1 for p in self.road_projects if p.status == 'in_progress')
        
        return {
            'company_name': self.company_name,
            'total_housing_projects': len(self.housing_projects),
            'total_road_projects': len(self.road_projects),
            'total_design_plans': len(self.design_plans),
            'active_housing_projects': in_progress_housing,
            'active_road_projects': in_progress_roads,
            'total_active_projects': in_progress_housing + in_progress_roads
        }
    
    def list_housing_projects(self) -> List[Dict]:
        """List all housing projects"""
        return [project.get_project_info() for project in self.housing_projects]
    
    def list_road_projects(self) -> List[Dict]:
        """List all road projects"""
        return [project.get_project_info() for project in self.road_projects]
    
    def list_design_plans(self) -> List[Dict]:
        """List all design plans"""
        return [plan.get_details() for plan in self.design_plans]
    
    def generate_report(self) -> str:
        """Generate a comprehensive company report"""
        summary = self.get_all_projects()
        
        report = f"""
{'='*60}
{self.company_name.upper()} - CONSTRUCTION COMPANY REPORT
{'='*60}

SUMMARY:
--------
Total Housing Projects: {summary['total_housing_projects']}
Total Road Projects: {summary['total_road_projects']}
Total Design Plans: {summary['total_design_plans']}
Active Projects: {summary['total_active_projects']}

HOUSING PROJECTS:
----------------
"""
        for project in self.housing_projects:
            info = project.get_project_info()
            report += f"  - {info['name']} ({info['type']}): {info['status']}\n"
        
        report += f"""
ROAD PROJECTS:
-------------
"""
        for project in self.road_projects:
            info = project.get_project_info()
            report += f"  - {info['name']} ({info['type']}, {info['length_km']}km): {info['status']}\n"
        
        report += f"""
{'='*60}
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'='*60}
"""
        return report


def main():
    """Example usage of the Construction Company Management System"""
    
    # Create construction company
    company = ConstructionCompany("Premier Construction Ltd.")
    
    print(f"Welcome to {company.company_name}")
    print("="*60)
    
    # Create design plans
    print("\n1. Creating Design Plans...")
    housing_plan = company.create_design_plan(
        "DP001", "housing", "Residential Complex Blueprint", 
        5000.0, 250000.0
    )
    housing_plan.add_specification("bedrooms", "3")
    housing_plan.add_specification("bathrooms", "2")
    housing_plan.add_specification("floors", "2")
    print(housing_plan.approve_plan())
    
    road_plan = company.create_design_plan(
        "DP002", "road", "Main Highway Design", 
        100000.0, 1500000.0
    )
    road_plan.add_specification("lanes", "4")
    road_plan.add_specification("surface", "asphalt")
    print(road_plan.approve_plan())
    
    # Create housing projects
    print("\n2. Creating Housing Projects...")
    housing1 = company.create_housing_project(
        "HP001", "Greenview Apartments", "apartment", 24
    )
    print(housing1.assign_design_plan(housing_plan))
    housing1.add_materials("cement", 500, "bags")
    housing1.add_materials("steel", 10, "tons")
    housing1.add_materials("bricks", 50000, "pieces")
    print(housing1.start_construction(25))
    
    # Create road projects
    print("\n3. Creating Road Projects...")
    road1 = company.create_road_project(
        "RD001", "Central Highway", "highway", 15.5
    )
    print(road1.assign_design_plan(road_plan))
    road1.set_road_specs(4, "asphalt")
    road1.add_equipment("excavator", 2)
    road1.add_equipment("roller", 3)
    road1.add_equipment("paver", 1)
    print(road1.start_construction(40))
    
    # Generate and display report
    print("\n4. Company Report:")
    print(company.generate_report())
    
    # Display project details
    print("\nDetailed Housing Project Info:")
    print(housing1.get_project_info())
    
    print("\nDetailed Road Project Info:")
    print(road1.get_project_info())


if __name__ == "__main__":
    main()
