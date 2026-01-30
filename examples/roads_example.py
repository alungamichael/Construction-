#!/usr/bin/env python3
"""
Example: Road Construction Project Management
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from construction_company import ConstructionCompany


def main():
    """Demonstrate road construction project management"""
    
    # Initialize company
    company = ConstructionCompany("Highway Masters Inc.")
    
    print("="*70)
    print("ROAD CONSTRUCTION PROJECT EXAMPLE")
    print("="*70)
    
    # Create highway design plan
    print("\n📐 Creating Highway Design Plan...")
    highway_plan = company.create_design_plan(
        plan_id="HWY-2024-001",
        plan_type="road",
        description="Interstate Highway Extension - 4 Lanes",
        area_sqft=250000.0,
        estimated_cost=12000000.0
    )
    
    highway_plan.add_specification("lanes", "4")
    highway_plan.add_specification("surface", "asphalt")
    highway_plan.add_specification("median_width", "12 feet")
    highway_plan.add_specification("shoulder_width", "10 feet")
    highway_plan.add_specification("speed_limit", "65 mph")
    print(f"✓ Plan created: {highway_plan.plan_id}")
    print(f"✓ {highway_plan.approve_plan()}")
    
    # Create main road design plan
    print("\n📐 Creating Main Road Design Plan...")
    main_road_plan = company.create_design_plan(
        plan_id="MRD-2024-001",
        plan_type="road",
        description="Urban Main Road - 2 Lanes with Bike Lanes",
        area_sqft=85000.0,
        estimated_cost=3500000.0
    )
    
    main_road_plan.add_specification("lanes", "2")
    main_road_plan.add_specification("bike_lanes", "2")
    main_road_plan.add_specification("surface", "asphalt")
    main_road_plan.add_specification("sidewalks", "both sides")
    main_road_plan.add_specification("lighting", "LED street lights")
    print(f"✓ Plan created: {main_road_plan.plan_id}")
    print(f"✓ {main_road_plan.approve_plan()}")
    
    # Create highway project
    print("\n🛣️  Creating Highway Project...")
    highway_project = company.create_road_project(
        project_id="PROJ-HWY-001",
        road_name="Interstate 95 Extension",
        road_type="highway",
        length_km=25.5
    )
    
    print(f"✓ {highway_project.assign_design_plan(highway_plan)}")
    highway_project.set_road_specs(lanes=4, surface_type="asphalt")
    
    # Add equipment for highway
    print("\n🚜 Adding Equipment to Highway Project...")
    highway_project.add_equipment("excavator", 5)
    highway_project.add_equipment("bulldozer", 4)
    highway_project.add_equipment("asphalt paver", 3)
    highway_project.add_equipment("road roller", 6)
    highway_project.add_equipment("dump truck", 15)
    highway_project.add_equipment("grader", 3)
    print(f"✓ Added {len(highway_project.equipment)} equipment types")
    
    # Start highway construction
    print("\n🚧 Starting Highway Construction...")
    print(f"✓ {highway_project.start_construction(workers=75)}")
    
    # Create main road project
    print("\n🛣️  Creating Main Road Project...")
    main_road_project = company.create_road_project(
        project_id="PROJ-MRD-001",
        road_name="Downtown Parkway",
        road_type="main_road",
        length_km=8.2
    )
    
    print(f"✓ {main_road_project.assign_design_plan(main_road_plan)}")
    main_road_project.set_road_specs(lanes=2, surface_type="asphalt")
    
    # Add equipment for main road
    print("\n🚜 Adding Equipment to Main Road Project...")
    main_road_project.add_equipment("excavator", 2)
    main_road_project.add_equipment("asphalt paver", 2)
    main_road_project.add_equipment("road roller", 3)
    main_road_project.add_equipment("dump truck", 8)
    main_road_project.add_equipment("line painter", 1)
    print(f"✓ Added {len(main_road_project.equipment)} equipment types")
    
    # Start main road construction
    print("\n🚧 Starting Main Road Construction...")
    print(f"✓ {main_road_project.start_construction(workers=35)}")
    
    # Create a street project
    print("\n🛣️  Creating Street Project...")
    street_plan = company.create_design_plan(
        plan_id="STR-2024-001",
        plan_type="road",
        description="Residential Street Network",
        area_sqft=45000.0,
        estimated_cost=850000.0
    )
    street_plan.add_specification("lanes", "2")
    street_plan.add_specification("surface", "concrete")
    print(f"✓ {street_plan.approve_plan()}")
    
    street_project = company.create_road_project(
        project_id="PROJ-STR-001",
        road_name="Maple Street Extension",
        road_type="street",
        length_km=3.5
    )
    print(f"✓ {street_project.assign_design_plan(street_plan)}")
    street_project.set_road_specs(lanes=2, surface_type="concrete")
    street_project.add_equipment("concrete mixer", 2)
    street_project.add_equipment("finishing machine", 1)
    print(f"✓ {street_project.start_construction(workers=20)}")
    
    # Display company summary
    print("\n" + "="*70)
    print("COMPANY SUMMARY")
    print("="*70)
    summary = company.get_all_projects()
    print(f"Company Name: {summary['company_name']}")
    print(f"Total Road Projects: {summary['total_road_projects']}")
    print(f"Active Road Projects: {summary['active_road_projects']}")
    print(f"Total Design Plans: {summary['total_design_plans']}")
    
    # List all road projects
    print("\n" + "="*70)
    print("ALL ROAD PROJECTS")
    print("="*70)
    for project_info in company.list_road_projects():
        print(f"\n🛣️  {project_info['name']}")
        print(f"   ID: {project_info['project_id']}")
        print(f"   Type: {project_info['type']}")
        print(f"   Length: {project_info['length_km']} km")
        print(f"   Lanes: {project_info['lanes']}")
        print(f"   Surface: {project_info['surface']}")
        print(f"   Status: {project_info['status']}")
        print(f"   Workers: {project_info['workers']}")
        print(f"   Equipment: {project_info['equipment_count']} types")
    
    # Demonstrate maintenance scheduling
    print("\n" + "="*70)
    print("PROJECT COMPLETION AND MAINTENANCE")
    print("="*70)
    
    # Complete a project
    print(f"\n✓ {street_project.complete_project()}")
    
    # Schedule maintenance
    print(f"✓ {street_project.schedule_maintenance()}")
    
    print("\n" + "="*70)
    print("✓ Road construction example completed successfully!")
    print("="*70)


if __name__ == "__main__":
    main()
