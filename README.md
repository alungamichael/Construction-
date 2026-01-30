# Construction Project Management System

A simple JavaScript-based construction project management system for tracking tasks, materials, workers, and budgets.

## Features

- **Project Management**: Create and manage construction projects with budgets and locations
- **Task Tracking**: Add, track, and complete construction tasks
- **Material Management**: Track materials, quantities, and costs
- **Worker Management**: Manage workers, roles, and labor costs
- **Budget Tracking**: Monitor total costs against budget
- **Progress Monitoring**: View project completion percentage

## Files

- `construction.js` - Core JavaScript module with ConstructionProject class
- `index.html` - Interactive web interface demonstrating the system

## Usage

### In Node.js

```javascript
const ConstructionProject = require('./construction.js');

const project = new ConstructionProject('Office Building', '123 Main St', 500000);

// Add tasks
project.addTask('Foundation', 30, 'John Doe');
project.addTask('Framing', 45, 'Jane Smith');

// Add materials
project.addMaterial('Concrete', 100, 150);
project.addMaterial('Steel Beams', 50, 500);

// Add workers
project.addWorker('John Doe', 'Foreman', 45);

// Start project
project.start();

// Complete tasks
project.completeTask(1);

// Get summary
console.log(project.getSummary());
```

### In Browser

Simply open `index.html` in a web browser to see the interactive demo.

## API Reference

### ConstructionProject Class

#### Constructor
- `new ConstructionProject(name, location, budget)` - Create a new project

#### Methods
- `addTask(taskName, duration, assignee)` - Add a task to the project
- `addMaterial(materialName, quantity, unitCost)` - Add materials
- `addWorker(name, role, hourlyRate)` - Add a worker
- `completeTask(taskId)` - Mark a task as completed
- `getTotalMaterialCost()` - Get total cost of materials
- `getTotalLaborCost()` - Get total labor costs
- `getProgress()` - Get completion percentage
- `getSummary()` - Get comprehensive project summary
- `start()` - Start the project
- `complete()` - Mark project as completed

## License

Open source - feel free to use and modify.