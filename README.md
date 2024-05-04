# N-Body Simulator

The N-Body Simulator is a Python application that simulates the dynamics of celestial bodies interacting through gravitational forces. This simulator provides a graphical representation of the simulated system and allows users to customize various parameters such as the particle system, time step, gravity constant, and animation length.

![Alt Text](https://github.com/deer-in-haze/N-Body_Simulator/blob/main/SIMULATIONS/Inner%20Solar%20system.gif?raw=true)

## Installation

To use the N-Body Simulator, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required dependencies by running:
3. 
    ```
    pip install tkinter pillow numpy pandas matplotlib.pyplot matplotlib.animation
    ```
    
4. Download the source code files from [GitHub Repository](https://github.com/deer-in-haze/N-Body_Simulator).

## Usage

## Running the N-Body Simulator from the Terminal

To run the N-Body Simulator from the terminal, follow these steps:

1. **Open the Terminal/Command Prompt**: Open the Terminal (Unix/Linux) or Command Prompt (Windows) application on your system.

2. **Navigate to the Project Directory**: Use the `cd` command to navigate to the directory where your Python files are located. For example:
   ```
   cd path/to/N-Body_Simulator
   ```
3. **Run the Python Script**: Execute the Python script by entering the following command:
   ```
   python3 main.py
   ```
This will launch the graphical user interface (GUI) of the simulator.

The `ParticleSystemCreator` class can be used to create a particle system based on a given hostname. This class utilizes data processing, data list creation, and calculations to generate the particle system.

```python
particle_system_creator = ParticleSystemCreator("hostname")
particle_system = particle_system_creator.create_particle_system()
```

### Interface Overview

Upon launching the application, you will see the following components:

- **Hostname:** Select the hostname for data retrieval or choose a predefined particle system.
- **Particle System:** Choose from various predefined particle systems or select a custom one.
- **Time Step:** Choose the time step for the simulation.
- **Gravity Constant:** Select the gravitational constant for the simulation.
- **Animation Length:** Set the duration of the simulation animation.
- **Title:** Specify the title for the simulation animation file.
- **Update Data:** Check this box to update simulation data from NASA's database.
- **Start Simulation:** Click this button to begin the simulation.

### Simulation Results

Once the simulation is complete, a pop-up window will display the simulation results in the form of an animated GIF.

![Alt Text](https://github.com/deer-in-haze/N-Body_Simulator/blob/main/SIMULATIONS/Binary%20system.gif?raw=true)

## Components

## Classes and Modules

### Body (Abstract Base Class)

- `Body` is an abstract base class representing a celestial body or particle. It defines common properties such as mass, position, velocity, and acceleration.

### CelestialBody

- `CelestialBody` is a concrete subclass of `Body` representing a celestial body, such as a star or planet.

### Particle

- `Particle` is a concrete subclass of `Body` representing a particle in the simulation.

### Particles

- `Particles` manages a collection of particles and provides methods for creating and adding particles to the system.

### Settings (Abstract Base Class)

- `Settings` is an abstract base class representing simulation settings. It defines common methods for accessing and displaying settings.

### SimulationSettings

- `SimulationSettings` is a concrete subclass of `Settings` that holds simulation-specific parameters such as gravitational constant, softening factor, and step size.

### Data Processing

- `DataProcessor` and `NASADataProcessor` classes handle the processing of data, including loading, cleaning, analyzing, and saving data from sources such as NASA's database.

### Data List Creator

- `DataListCreator` creates lists of data for the particle system based on grouped data.

### Calculations

- `OrbitalVelocity` calculates the orbital velocities of celestial bodies based on their mass and semi-major axis.

### Visualization

- `FigureSettings` and `Figure` classes provide settings and functionality for visualizing the particle system using matplotlib.

### Decorators

- `status_update` decorator is used to provide status updates during method execution.

### Constants

- Constants module contains predefined constants such as gravitational constant, mass of the Sun, astronomical unit, etc.



