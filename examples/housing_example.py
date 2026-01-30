#!/usr/bin/env python3
"""
Example: Housing Construction Project Management
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from construction_company import ConstructionCompany, DesignPlan


def main():
    """Demonstrate housing project management"""
    
    # Initialize company
    company = ConstructionCompany("Urban Housing Solutions")
    
    print("="*70)
    print("HOUSING CONSTRUCTION PROJECT EXAMPLE")
    print("="*70)
    
    # Create residential housing design plan
    print("\n📐 Creating Residential Housing Design Plan...")
    residential_plan = company.create_design_plan(
        plan_id="RES-2024-001",
        plan_type="housing",
        description="Modern 3-Bedroom Family Home",
        area_sqft=2500.0,
        estimated_cost=350000.0
    )
    
    # Add specifications
    residential_plan.add_specification("bedrooms", "3")
    residential_plan.add_specification("bathrooms", "2.5")
    residential_plan.add_specification("garage", "2-car")
    residential_plan.add_specification("floors", "2")
    residential_plan.add_specification("style", "Contemporary")
    print(f"✓ Plan created: {residential_plan.plan_id}")
    print(f"✓ {residential_plan.approve_plan()}")
    
    # Create apartment complex design plan
    print("\n📐 Creating Apartment Complex Design Plan...")
    apartment_plan = company.create_design_plan(
        plan_id="APT-2024-001",
        plan_type="housing",
        description="Luxury Apartment Complex - 50 Units",
        area_sqft=75000.0,
        estimated_cost=8500000.0
    )
    
    apartment_plan.add_specification("units", "50")
    apartment_plan.add_specification("floors", "8")
    apartment_plan.add_specification("parking_spaces", "75")
    apartment_plan.add_specification("amenities", "Pool, Gym, Clubhouse")
    print(f"✓ Plan created: {apartment_plan.plan_id}")
    print(f"✓ {apartment_plan.approve_plan()}")
    
    # Create residential housing project
    print("\n🏗️  Creating Residential Housing Project...")
    residential_project = company.create_housing_project(
        project_id="PROJ-RES-001",
        project_name="Oakwood Estates Phase 1",
        housing_type="residential",
        num_units=12
    )
    
    print(f"✓ {residential_project.assign_design_plan(residential_plan)}")
    
    # Add materials
    print("\n📦 Adding Materials to Residential Project...")
    residential_project.add_materials("concrete", 150, "cubic yards")
    residential_project.add_materials("lumber", 25000, "board feet")
    residential_project.add_materials("roofing shingles", 4000, "sq ft")
    residential_project.add_materials("windows", 48, "units")
    residential_project.add_materials("doors", 36, "units")
    print(f"✓ Added {len(residential_project.materials)} material types")
    
    # Start construction
    print("\n🚧 Starting Residential Construction...")
    print(f"✓ {residential_project.start_construction(workers=18)}")
    
    # Create apartment project
    print("\n🏗️  Creating Apartment Complex Project...")
    apartment_project = company.create_housing_project(
        project_id="PROJ-APT-001",
        project_name="Riverside Luxury Apartments",
        housing_type="apartment",
        num_units=50
    )
    
    print(f"✓ {apartment_project.assign_design_plan(apartment_plan)}")
    
    # Add materials for apartment
    print("\n📦 Adding Materials to Apartment Project...")
    apartment_project.add_materials("steel rebar", 85, "tons")
    apartment_project.add_materials("concrete", 2500, "cubic yards")
    apartment_project.add_materials("glass panels", 500, "sq meters")
    apartment_project.add_materials("elevator systems", 3, "units")
    apartment_project.add_materials("HVAC units", 50, "units")
    print(f"✓ Added {len(apartment_project.materials)} material types")
    
    # Start apartment construction
    print("\n🚧 Starting Apartment Construction...")
    print(f"✓ {apartment_project.start_construction(workers=45)}")
    
    # Display company summary
    print("\n" + "="*70)
    print("COMPANY SUMMARY")
    print("="*70)
    summary = company.get_all_projects()
    print(f"Company Name: {summary['company_name']}")
    print(f"Total Housing Projects: {summary['total_housing_projects']}")
    print(f"Active Housing Projects: {summary['active_housing_projects']}")
    print(f"Total Design Plans: {summary['total_design_plans']}")
    
    # List all housing projects
    print("\n" + "="*70)
    print("ALL HOUSING PROJECTS")
    print("="*70)
    for project_info in company.list_housing_projects():
        print(f"\n📋 {project_info['name']}")
        print(f"   ID: {project_info['project_id']}")
        print(f"   Type: {project_info['type']}")
        print(f"   Units: {project_info['units']}")
        print(f"   Status: {project_info['status']}")
        print(f"   Workers: {project_info['workers']}")
        print(f"   Materials: {project_info['materials_count']} types")
    
    print("\n" + "="*70)
    print("✓ Housing example completed successfully!")
    print("="*70)


if __name__ == "__main__":
    main()
