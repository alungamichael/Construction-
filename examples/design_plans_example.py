#!/usr/bin/env python3
"""
Example: Design Plans Management
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from construction_company import ConstructionCompany


def main():
    """Demonstrate design plan management"""
    
    # Initialize company
    company = ConstructionCompany("Design & Build Solutions")
    
    print("="*70)
    print("DESIGN PLANS MANAGEMENT EXAMPLE")
    print("="*70)
    
    # Create various design plans
    print("\n📐 Creating Design Plans...")
    
    # 1. Villa design plan
    print("\n1. Villa Design Plan")
    villa_plan = company.create_design_plan(
        plan_id="VILLA-001",
        plan_type="housing",
        description="Luxury Mediterranean Villa",
        area_sqft=6500.0,
        estimated_cost=1250000.0
    )
    villa_plan.add_specification("bedrooms", "5")
    villa_plan.add_specification("bathrooms", "4.5")
    villa_plan.add_specification("floors", "2")
    villa_plan.add_specification("pool", "Yes - Infinity pool")
    villa_plan.add_specification("garage", "3-car")
    villa_plan.add_specification("outdoor_kitchen", "Yes")
    villa_plan.add_specification("style", "Mediterranean")
    print(f"   Created: {villa_plan.plan_id}")
    print(f"   Type: {villa_plan.plan_type}")
    print(f"   Area: {villa_plan.area_sqft} sq ft")
    print(f"   Estimated Cost: ${villa_plan.estimated_cost:,.2f}")
    
    # 2. Commercial plaza design plan
    print("\n2. Commercial Plaza Design Plan")
    commercial_plan = company.create_design_plan(
        plan_id="COM-001",
        plan_type="commercial",
        description="Shopping Plaza with Mixed Use",
        area_sqft=125000.0,
        estimated_cost=15000000.0
    )
    commercial_plan.add_specification("retail_spaces", "45")
    commercial_plan.add_specification("restaurants", "8")
    commercial_plan.add_specification("office_floors", "3")
    commercial_plan.add_specification("parking_levels", "2 underground")
    commercial_plan.add_specification("parking_capacity", "500 vehicles")
    commercial_plan.add_specification("elevators", "6")
    commercial_plan.add_specification("escalators", "4")
    print(f"   Created: {commercial_plan.plan_id}")
    print(f"   Type: {commercial_plan.plan_type}")
    print(f"   Area: {commercial_plan.area_sqft} sq ft")
    print(f"   Estimated Cost: ${commercial_plan.estimated_cost:,.2f}")
    
    # 3. Bridge design plan
    print("\n3. Bridge Design Plan")
    bridge_plan = company.create_design_plan(
        plan_id="BRG-001",
        plan_type="road",
        description="Pedestrian and Vehicle Bridge",
        area_sqft=35000.0,
        estimated_cost=8500000.0
    )
    bridge_plan.add_specification("length", "450 feet")
    bridge_plan.add_specification("width", "80 feet")
    bridge_plan.add_specification("vehicle_lanes", "4")
    bridge_plan.add_specification("pedestrian_walkways", "2")
    bridge_plan.add_specification("bike_lanes", "2")
    bridge_plan.add_specification("load_capacity", "80 tons")
    bridge_plan.add_specification("structure_type", "Cable-stayed")
    print(f"   Created: {bridge_plan.plan_id}")
    print(f"   Type: {bridge_plan.plan_type}")
    print(f"   Area: {bridge_plan.area_sqft} sq ft")
    print(f"   Estimated Cost: ${bridge_plan.estimated_cost:,.2f}")
    
    # 4. Town house complex plan
    print("\n4. Townhouse Complex Design Plan")
    townhouse_plan = company.create_design_plan(
        plan_id="TWN-001",
        plan_type="housing",
        description="Modern Townhouse Community - 30 Units",
        area_sqft=90000.0,
        estimated_cost=9500000.0
    )
    townhouse_plan.add_specification("units", "30")
    townhouse_plan.add_specification("bedrooms_per_unit", "3")
    townhouse_plan.add_specification("bathrooms_per_unit", "2.5")
    townhouse_plan.add_specification("floors_per_unit", "3")
    townhouse_plan.add_specification("attached_garage", "2-car per unit")
    townhouse_plan.add_specification("common_areas", "Clubhouse, Playground")
    townhouse_plan.add_specification("style", "Contemporary")
    print(f"   Created: {townhouse_plan.plan_id}")
    print(f"   Type: {townhouse_plan.plan_type}")
    print(f"   Area: {townhouse_plan.area_sqft} sq ft")
    print(f"   Estimated Cost: ${townhouse_plan.estimated_cost:,.2f}")
    
    # Approve some plans
    print("\n" + "="*70)
    print("APPROVING DESIGN PLANS")
    print("="*70)
    print(f"✓ {villa_plan.approve_plan()}")
    print(f"✓ {commercial_plan.approve_plan()}")
    print(f"✓ {townhouse_plan.approve_plan()}")
    
    # Show all design plans
    print("\n" + "="*70)
    print("ALL DESIGN PLANS")
    print("="*70)
    
    all_plans = company.list_design_plans()
    for i, plan in enumerate(all_plans, 1):
        print(f"\n{i}. Plan ID: {plan['plan_id']}")
        print(f"   Type: {plan['type']}")
        print(f"   Description: {plan['description']}")
        print(f"   Area: {plan['area_sqft']} sq ft")
        print(f"   Estimated Cost: ${plan['estimated_cost']:,.2f}")
        print(f"   Approved: {'✓ Yes' if plan['approved'] else '✗ No'}")
        print(f"   Created: {plan['created_date']}")
        if plan['specifications']:
            print(f"   Specifications:")
            for key, value in plan['specifications'].items():
                print(f"      - {key}: {value}")
    
    # Summary statistics
    print("\n" + "="*70)
    print("DESIGN PLANS SUMMARY")
    print("="*70)
    
    approved_plans = sum(1 for p in all_plans if p['approved'])
    pending_plans = len(all_plans) - approved_plans
    total_estimated_cost = sum(p['estimated_cost'] for p in all_plans)
    
    print(f"Total Design Plans: {len(all_plans)}")
    print(f"Approved Plans: {approved_plans}")
    print(f"Pending Approval: {pending_plans}")
    print(f"Total Estimated Cost: ${total_estimated_cost:,.2f}")
    
    # Plan types breakdown
    plan_types = {}
    for plan in all_plans:
        ptype = plan['type']
        plan_types[ptype] = plan_types.get(ptype, 0) + 1
    
    print(f"\nPlans by Type:")
    for ptype, count in plan_types.items():
        print(f"  - {ptype}: {count}")
    
    print("\n" + "="*70)
    print("✓ Design plans example completed successfully!")
    print("="*70)


if __name__ == "__main__":
    main()
