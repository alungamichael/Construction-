/**
 * Construction Project Management System
 * A simple JavaScript module for managing construction projects
 */

class ConstructionProject {
    constructor(name, location, budget) {
        this.name = name;
        this.location = location;
        this.budget = budget;
        this.tasks = [];
        this.materials = [];
        this.workers = [];
        this.startDate = null;
        this.endDate = null;
        this.status = 'Planning';
    }

    /**
     * Add a task to the project
     * @param {string} taskName - Name of the task
     * @param {number} duration - Duration in days
     * @param {string} assignee - Person assigned to the task
     */
    addTask(taskName, duration, assignee) {
        const task = {
            id: this.tasks.length + 1,
            name: taskName,
            duration: duration,
            assignee: assignee,
            status: 'Pending',
            completed: false
        };
        this.tasks.push(task);
        return task;
    }

    /**
     * Add materials to the project
     * @param {string} materialName - Name of the material
     * @param {number} quantity - Quantity needed
     * @param {number} unitCost - Cost per unit
     */
    addMaterial(materialName, quantity, unitCost) {
        const material = {
            id: this.materials.length + 1,
            name: materialName,
            quantity: quantity,
            unitCost: unitCost,
            totalCost: quantity * unitCost
        };
        this.materials.push(material);
        return material;
    }

    /**
     * Add a worker to the project
     * @param {string} name - Worker's name
     * @param {string} role - Worker's role
     * @param {number} hourlyRate - Hourly rate
     */
    addWorker(name, role, hourlyRate) {
        const worker = {
            id: this.workers.length + 1,
            name: name,
            role: role,
            hourlyRate: hourlyRate,
            hoursWorked: 0
        };
        this.workers.push(worker);
        return worker;
    }

    /**
     * Mark a task as completed
     * @param {number} taskId - ID of the task to complete
     */
    completeTask(taskId) {
        const task = this.tasks.find(t => t.id === taskId);
        if (task) {
            task.completed = true;
            task.status = 'Completed';
            return true;
        }
        return false;
    }

    /**
     * Calculate total material costs
     * @returns {number} Total cost of all materials
     */
    getTotalMaterialCost() {
        return this.materials.reduce((total, material) => total + material.totalCost, 0);
    }

    /**
     * Calculate total labor costs
     * @returns {number} Total labor cost
     */
    getTotalLaborCost() {
        return this.workers.reduce((total, worker) => total + (worker.hourlyRate * worker.hoursWorked), 0);
    }

    /**
     * Get project progress percentage
     * @returns {number} Percentage of completed tasks
     */
    getProgress() {
        if (this.tasks.length === 0) return 0;
        const completedTasks = this.tasks.filter(t => t.completed).length;
        return Math.round((completedTasks / this.tasks.length) * 100);
    }

    /**
     * Get project summary
     * @returns {object} Summary of the project
     */
    getSummary() {
        return {
            name: this.name,
            location: this.location,
            budget: this.budget,
            status: this.status,
            progress: this.getProgress() + '%',
            totalTasks: this.tasks.length,
            completedTasks: this.tasks.filter(t => t.completed).length,
            totalWorkers: this.workers.length,
            materialCost: this.getTotalMaterialCost(),
            laborCost: this.getTotalLaborCost(),
            totalCost: this.getTotalMaterialCost() + this.getTotalLaborCost(),
            remainingBudget: this.budget - (this.getTotalMaterialCost() + this.getTotalLaborCost())
        };
    }

    /**
     * Start the project
     */
    start() {
        this.startDate = new Date();
        this.status = 'In Progress';
    }

    /**
     * Complete the project
     */
    complete() {
        this.endDate = new Date();
        this.status = 'Completed';
    }
}

// Example usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ConstructionProject;
}

// Browser example
if (typeof window !== 'undefined') {
    // Example usage in browser
    const exampleProject = new ConstructionProject('Office Building', '123 Main St', 500000);
    
    exampleProject.addTask('Foundation', 30, 'John Doe');
    exampleProject.addTask('Framing', 45, 'Jane Smith');
    exampleProject.addTask('Roofing', 20, 'Bob Johnson');
    
    exampleProject.addMaterial('Concrete', 100, 150);
    exampleProject.addMaterial('Steel Beams', 50, 500);
    exampleProject.addMaterial('Roofing Tiles', 200, 25);
    
    exampleProject.addWorker('John Doe', 'Foreman', 45);
    exampleProject.addWorker('Jane Smith', 'Carpenter', 35);
    exampleProject.addWorker('Bob Johnson', 'Roofer', 30);
    
    exampleProject.start();
    
    console.log('Construction Project Management System Loaded');
    console.log('Example project created:', exampleProject.name);
}
