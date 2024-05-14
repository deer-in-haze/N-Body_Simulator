# N-Body Simulator

The N-Body Simulator is a Python application that simulates the dynamics of celestial bodies interacting through gravitational forces. This simulator provides a graphical representation of the simulated system and allows users to customize various parameters such as the particle system, time step, gravity constant, and animation length.

![Alt Text](https://github.com/deer-in-haze/N-Body_Simulator/blob/main/SIMULATIONS/Inner%20Solar%20system.gif?raw=true)

## Installation

To use the N-Body Simulator, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required dependencies by running:
3. 
    ```python
    pip install tk pillow numpy pandas matplotlib requests
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

### Interface Overview

Upon launching the application, you will see the following components:

![Alt text](https://github.com/deer-in-haze/N-Body_Simulator/blob/main/DATA/application_examples/Screenshot%20from%202024-05-14%2022-24-09.png)

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

![Alt text](https://github.com/deer-in-haze/N-Body_Simulator/blob/main/DATA/application_examples/Screenshot%20from%202024-05-14%2022-09-01.png)

![Alt Text](https://github.com/deer-in-haze/N-Body_Simulator/blob/main/SIMULATIONS/Binary%20system.gif?raw=true)

# Components

## main.py

`main.py` serves as the entry point for the N-body simulator, initializing the main application window using Tkinter. It creates an instance of `MainApplication` from `main_interface.py` and enters the Tkinter event loop, which is essential for running the GUI.

The file abstracts the initialization process of the GUI, leaving details to `MainApplication`.
   ```python
    def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
  ```

## main_interface.py

`main_interface.py` defines the `MainApplication` class, which is responsible for setting up the graphical user interface using Tkinter. It allows the user to configure parameters such as hostname, particle system, time step, gravity constant, and animation length. The class handles user inputs, validates them, and initiates the simulation based on the selected settings.


## simulation.py

The `Simulation` class orchestrates the simulation process for an N-body system:
- Initializes particle data using the specified `particle_system`.
- Applies various calculations (e.g., acceleration, center of mass) through specialized classes like `CentreOfMass` and `Acceleration`.
- Configures animation settings to visualize the simulation with `ParticleAnimation`.

#### Implementation of OOP Principles
- **Encapsulation**: Uses private attributes (e.g., `__particle_system`, `__step_size`) to encapsulate simulation data and configuration.
- **Abstraction**: The `start()` method provides a high-level interface for the entire simulation process.

#### Design Patterns Used
- **Builder**: The `Builder` pattern in `FigureSettings`, `SimulationSettings`, and `AnimationSettings` allows flexible and incremental configuration of settings.
- **Decorator**: The `status_update` decorator provides a standardized way to include status messages in the `start()` method.

## particles.py

The module defines core data structures for representing bodies and particles in an N-body simulation:
- **`Body`**: An abstract base class (ABC) representing a generic body with mass, position, velocity, and acceleration attributes. It provides encapsulated getter methods for each property.
- **`CelestialBody`** and **`Particle`**: Concrete subclasses of `Body`, currently serving as markers with potential for future extension.
- **`Particles`**: Manages collections of `Body` instances, facilitating grouped access to particle properties like mass, position, velocity, and acceleration.

#### Implementation of OOP Principles
- **Abstraction**: The `Body` class uses abstract methods and hides the internal structure, serving as a base class for specialized implementations.
- **Inheritance**: `CelestialBody` and `Particle` inherit from `Body`, benefiting from shared attributes and encapsulated methods.
- **Encapsulation**: `Body` and `Particles` classes encapsulate the core data structures through private attributes with controlled access via getter methods.

#### Design Patterns Used
- **Decorator**: The `status_update` decorator is applied to methods like `create_particles` and `add_particle`, enriching these with additional behavior while preserving the original functionality.

## calculations.py

#### Limits, CentreOfMass, Acceleration, and OrbitalVelocity Modules

The following modules provide essential mathematical and physics calculations required for the N-Body simulation, covering features such as calculating the limits, determining the center of mass, computing acceleration, and computing orbital velocities.

#### Limits
The `Limits` class helps determine the appropriate visual limits for the entire particle system by:
- Analyzing the maximum distance between particles.
- Adding a 10% buffer to ensure the whole system remains visible.

It encapsulates this logic in the `calculate_limits` method and returns the computed limit via the `get_limit` method.

#### CentreOfMass
The `CentreOfMass` class calculates the overall center of mass and velocity of a given particle system. It achieves this by:
- Multiplying each particle's mass with its position to determine the weighted mean position.
- Using similar calculations for velocity to determine the weighted mean velocity.

These calculations help to:
1. Offset the particle system to ensure the center of mass remains at the origin.
2. Ensure the velocity of the center of mass remains stationary.

#### Acceleration
The `Acceleration` class computes the gravitational acceleration of each particle due to the gravitational effects of every other particle. Key details:
- It employs the **N-body** gravitational acceleration formula using vectorized calculations with NumPy.
- The results are in two columns, one for each coordinate axis (x, y).

#### OrbitalVelocity
The `OrbitalVelocity` class calculates the orbital velocity of each planet in a given system. It:
- Uses Kepler's laws to determine orbital velocity based on semi-major axis and orbital period data.
- Returns a list of computed velocities.

#### Implementation of OOP Principles

1. **Encapsulation**:
   - Each class encapsulates its internal properties, using getter methods to access critical data. For example, `get_velocity_list` provides access to the velocity data while keeping it private.

2. **Polymorphism**:
   - The `Body` class (used in other files) serves as an abstract base class, allowing different types like `Particle` and `CelestialBody` to inherit and provide their specific implementations.

These structures ensure that the various mathematical and physical calculations are modular, reusable, and maintainable.

## figure.py


The `Figure` class is responsible for creating and managing the plot that visualizes the N-body simulation using the Matplotlib library.

#### Initialization
- **Particle Properties**:
  - The particle properties include colors, sizes, and positions, derived from `figure_settings` and `particle_list`.
- **Lines**:
  - Lines are configured using customizable styles to represent particle paths.
- **Plot Settings**:
  - Axis limits are derived from the `limits` parameter to ensure consistent visual boundaries for the entire simulation.

#### Key Methods
1. **get_figure**:
   - Returns the Matplotlib figure object containing the plot.

2. **get_scatter**:
   - Provides the scatter plot object used to visualize the particles.

3. **get_lines**:
   - Retrieves the list of lines used to track particle paths.

4. **plot_figure**:
   - Sets up the plot by:
     - Configuring the background and plot colors.
     - Establishing the x and y axis limits.
     - Creating a scatter plot of particles with appropriate styles.
     - Initializing lines to plot each particle's path.

#### Implementation of OOP Principles
1. **Encapsulation**:
   - The private attributes ensure that key plot properties are maintained internally and can only be accessed via public methods.

## animation.py

The `ParticleAnimation` class is responsible for orchestrating the animation of the N-body simulation, utilizing Matplotlib's animation functionality.

#### Initialization
- **Particle Properties**:
  - Accesses particle acceleration, velocity, and position lists to control their animation.
  - The `figure` instance provides access to the figure and scatter plot, while the lines are used to trace paths.

- **Settings**:
  - Various simulation settings control the animation speed, interval, and frames.
  - The animation settings determine whether lines are included, and if the blitting technique should be used.

#### Key Methods
1. **__animate**:
   - This private method:
     - Updates velocities using the current acceleration and step size.
     - Updates positions based on the new velocities.
     - Recalculates accelerations for the next frame.
     - Updates the scatter plot and optionally updates the lines to trace particle paths.

2. **create_animation**:
   - Uses the `FuncAnimation` class to create an animation object.
   - Passes the `__animate` method as the update function and sets the frame count, interval, and blitting settings.

3. **save_animation**:
   - Saves the generated animation to a file using the Pillow library.

#### Implementation of OOP Principles
1. **Encapsulation**:
   - The class encapsulates settings and figure properties, ensuring that the animation works cohesively within specified constraints.

2. **Decorator Pattern**:
   - The methods `create_animation` and `save_animation` are decorated with `@status_update`, indicating progress updates.

## particle_systems.py
 In this code snippet, multiple celestial and particle systems are being defined for use in simulations. Here's a breakdown:

   ```python
#system example
star1 = CelestialBody(1.403 * 10 ** 30, [0, 0], [0, 0])
planet1 = CelestialBody(1.403 * 10 ** 30, [0.799 * AU, 0], [0, 27958.3133])
planet2 = CelestialBody(1.403 * 10 ** 30, [-0.799 * AU, 0], [0, -27958.3133])
   ```

### Particle Matrix
- **Particles** `p1` through `p9` are created using the `Particle` class. Each particle has a mass of 500 or 1000 units and occupies a specific position on a grid.
- The `particle_list` variable stores all the created particles for future simulations.

### Solar System Simulation
- **Planets** and the **Sun** are modeled using the `CelestialBody` class. Each body is initialized with:
  - A mass in kilograms (e.g., Sun's mass is `1.988e30` kg).
  - A starting position in astronomical units (AU), adjusted with an `OFFSET` value.
  - A velocity vector representing the body's initial speed.
- Several planets (Earth, Venus, Mars, Mercury, Jupiter, Saturn, Uranus, and Neptune) are positioned according to their average distance from the Sun and have appropriate orbital speeds.

### Earth-Moon System
- **Earth** is part of the solar system but is also listed separately with the **Moon**.
- The moon's position and velocity relative to Earth are calculated to reflect its real-world orbit.

### Custom Systems
- **Binary System**:
  - Contains two celestial bodies orbiting each other in a binary star-like system.
- **Three-Body System**:
  - Contains a third body orbiting in the binary system, creating a complex, three-body interaction.

## particle_system_creator.py

- **ParticleSystemCreator** (Class):
  - Facilitates the creation of a particle system (planetary system) using NASA's planetary database.
  - **Attributes**:
    - `_hostname`: The name of the host star to analyze.
  - **Methods**:
    - `create_particle_system()`: The main method to generate a planetary system.
      - **Workflow**:
        1. **Data Processing**:
            - Initializes `NASADataProcessor` with a given API key.
            - Loads cleaned data and groups it by host star.
        2. **Data List Creation**:
            - Creates an instance of `DataListCreator` using the grouped data and specified hostname.
            - Calls `create_data_list()` to extract planetary data for the host star system.
        3. **Orbital Velocity Calculation**:
            - Initializes `OrbitalVelocity` with the created data lists.
            - Calculates velocities of the planets and stores them in the data lists.
        4. **Particle Creation**:
            - Uses the `Particles` class to create particle representations of the planets.
            - Retrieves the final particle list representing the planetary system.
      - **Returns**: A particle system representing the host star system.

#### OOP Principles Implemented

- **Encapsulation**:
  - Classes like `NASADataProcessor`, `DataListCreator`, `OrbitalVelocity`, and `Particles` encapsulate their state and behavior using private attributes and methods, which are only exposed via public methods (e.g., getters/setters, specific tasks).
  
- **Abstraction**:
  - Abstract class `DataProcessor` defines a general interface that its subclasses (e.g., `NASADataProcessor`) implement to ensure consistent data handling while hiding implementation specifics.
  - Decorators (`@status_update`) provide modular and reusable logging functions to methods.

- **Inheritance**:
  - `NASADataProcessor` inherits from the abstract `DataProcessor` class, sharing a common structure while providing specific behavior tailored to NASA data.
  
- **Polymorphism**:
  - The `DataProcessor` abstract class allows different data processors to be implemented interchangeably, adhering to the common interface.

## data_processing.py

- **DataProcessor** (Abstract Class):
  - Defines a blueprint for data processors with abstract methods:
    - `load_data()`
    - `_analyse_data()`
    - `_clean_data()`
    - `_save_data()`

- **NASADataProcessor** (Concrete Class):
  - Inherits from `DataProcessor` and implements data processing specifically for NASA data.
  - **Attributes**:
    - `__api_url`: NASA API URL for fetching data.
    - `__destination_path`, `__original_file_name`, `__cleaned_file_name`: Paths and filenames for data storage.
    - `__original_data`, `__clean_data`, `__grouped_data`, `__df`: Data structures used during processing.
  - **Methods**:
    - **Private**:
      - `__fetch_data()`: Downloads data from the NASA API and stores it as `__original_data`.
      - `__delete_outdated_data()`: Removes outdated rows by keeping only the most recent update for each planet.
      - `__handle_missing_data()`: Drops rows containing any missing data.
    - **Public**:
      - `_analyse_data()`: Checks for and prints missing data information.
      - `_clean_data()`: Calls internal methods to clean outdated and incomplete data.
      - `_save_data(option)`: Saves either the original or cleaned data, depending on `option`.
      - `load_data(option)`: Loads the specified data file into a DataFrame for processing.
      - `group_data()`: Groups the DataFrame by `hostname`.
      - `update_data()`: Orchestrates the full update process:
        - Fetches data from the API.
        - Saves the raw data.
        - Loads and analyzes the data.
        - Cleans and analyzes the data again.
        - Saves the cleaned data.

### Usage
- Use the `NASADataProcessor` class to fetch and process NASA data:
  - Initialize with the appropriate API URL.
  - Call `update_data()` to fetch, clean, and analyze the data.

## data_list_creator.py

- **DataListCreator** (Class):
  - Responsible for creating data lists from grouped data, specifically for a given host star system.
  - **Attributes**:
    - `__grouped_data`: The grouped data, a Pandas GroupBy object.
    - `__hostname`: The name of the host star to analyze.
    - `__planet_system`, `__host_star`, `__host_mass`, `__planet_count`: Data attributes related to the star system.
    - `__planet_name_list`, `__planet_mass_list`, `__semi_major_axis_list`, `__position_list`, `__orbital_period_list`: Lists for planetary data.
    - `__particle_list`: Placeholder for future expansion.
  - **Methods**:
    - **Getters**: Retrieve specific data attributes.
      - `get_hostname()`
      - `get_planet_system()`
      - `get_host_star()`
      - `get_host_mass()`
      - `get_planet_count()`
      - `get_planet_name_list()`
      - `get_planet_mass_list()`
      - `get_semi_major_axis_list()`
      - `get_position_list()`
      - `get_orbital_period_list()`
      - `get_particle_list()`
    - **Private**:
      - `__get_group()`: Retrieves the group (host star system) from the grouped data.
      - `__append_data_lists()`: Fills the lists with planetary information, including:
        - `pl_name`: Planet names.
        - `pl_bmassj`: Planet masses in Jupiter units (converted to Earth masses).
        - `pl_orbsmax`: Semi-major axes (converted to AU).
        - `pl_orbper`: Orbital periods (converted to days).
    - **Public**:
      - `create_data_list()`: Coordinates the data list creation by calling private methods to retrieve and fill data.

### Usage
- Use the `DataListCreator` class to organize and extract planetary data:
  - Initialize the object with grouped data and a specific hostname.
  - Call `create_data_list()` to populate planetary data lists.

## Abstract `Settings` Class

- **Description**:
  - This is an abstract class that other concrete settings classes can inherit from.
  - It requires any subclass to implement the `display` method, ensuring a consistent interface.

- **Implementation**:
  ```python
  from abc import ABC, abstractmethod
  
  class Settings(ABC):
      @abstractmethod
      def display(self):
          pass
  
## simulation_settings.py

The `SimulationSettings` class is responsible for managing the settings and parameters used in physics simulations, such as gravitational constants, time step sizes, and softening factors.

### Key Features
- **Builder Pattern**: The inner `Builder` class enables step-by-step construction of a `SimulationSettings` instance.
- **Getters**: Public methods provide controlled access to the encapsulated settings attributes.


### `SimulationSettings.Builder` (Inner Class)

- Implements the builder pattern for creating `SimulationSettings` instances.
- Provides method chaining for setting configuration parameters.

#### Methods
- **`set_gravity_const(gravity_const)`**: Sets the gravitational constant.
- **`set_step_size(step_size)`**: Sets the step size for time increments.
- **`set_softening(softening)`**: Sets the softening parameter to prevent singularities.
- **`build()`**: Returns a fully configured `SimulationSettings` instance.

### `SimulationSettings` (Outer Class)

- Holds the simulation settings such as gravitational constant, time step size, and softening parameter.

#### Attributes
- **`__gravity_const`**: Gravitational constant used in calculations.
- **`__softening`**: Softening parameter to handle singularities.
- **`__step_size`**: Time increment size for each step of the simulation.
- **`__half_step_size`**: Half the step size, used in calculations.

#### Methods
- **`get_gravity_const()`**: Returns the gravitational constant.
- **`get_step_size()`**: Returns the time step size.
- **`get_softening()`**: Returns the softening parameter.
- **`get_half_step_size()`**: Returns half of the step size.

#### OOP Principles Implemented

1. **Encapsulation**:
   - All attributes are private, ensuring data is accessed only via public getter methods.

2. **Inheritance & Abstraction**:
   - Inherits from `Settings`, which defines the abstract `display` method.
   - Implements an empty `display` method for future customization.

3. **Builder Pattern**:
   - Simplifies object creation by enabling method chaining and separating the building process from the `SimulationSettings` class itself.

### Example Usage
```python
# Example usage of the SimulationSettings class with the builder pattern
settings = SimulationSettings.Builder()\
    .set_gravity_const(6.67430e-11)\
    .set_step_size(86400)\
    .set_softening(0.01)\
    .build()

# Using the getter methods to access the settings
print(settings.get_gravity_const())
print(settings.get_step_size())
print(settings.get_softening())
print(settings.get_half_step_size())
```
## figure_settings.py

The `FigureSettings` class manages various settings related to the visual appearance of a figure, including particle colors, line styles, and plot background.

### Key Features
- **Builder Pattern**: The inner `Builder` class allows for a fluent API to set up the `FigureSettings` object in a step-by-step manner.
- **Getters**: Public getter methods provide controlled access to encapsulated visual properties.

### `FigureSettings.Builder` (Inner Class)

- Implements the builder pattern to provide an organized way to set up the `FigureSettings` object.
- Offers method chaining for each visual property.

#### Methods
- **`set_fig_size(fig_size)`**: Sets the figure size.
- **`set_background(background)`**: Sets the background color.
- **`set_edge_colour(edge_colour)`**: Sets the edge color.
- **`set_plot_colour(plot_colour)`**: Sets the plot color.
- **`set_particle_colour(particle_colour)`**: Sets the particle color.
- **`set_custom_colours(custom_colours)`**: Sets custom colors for particles.
- **`set_custom_sizes(custom_sizes)`**: Sets custom sizes for particles.
- **`set_line_weight(line_weight)`**: Sets the line weight.
- **`set_line_colour(line_colour)`**: Sets the line color.
- **`set_line_style(line_style)`**: Sets the line style.
- **`set_line_custom_colours(line_custom_colours)`**: Sets custom colors for lines.
- **`build()`**: Returns a configured `FigureSettings` instance.

### `FigureSettings` (Outer Class)

- Holds settings related to the figure's appearance, such as line style, particle color, and plot background.

#### Attributes
- **`__fig_size`**: Size of the figure.
- **`__background`**: Background color.
- **`__edge_colour`**: Edge color.
- **`__plot_colour`**: Plot color.
- **`__particle_colour`**: Particle color.
- **`__custom_colours`**: Custom particle colors.
- **`__custom_sizes`**: Custom particle sizes.
- **`__line_weight`**: Line weight.
- **`__line_colour`**: Line color.
- **`__line_style`**: Line style.
- **`__line_custom_colours`**: Custom line colors.

#### Methods
- **`get_fig_size()`**: Returns the figure size.
- **`get_background()`**: Returns the background color.
- **`get_edge_colour()`**: Returns the edge color.
- **`get_plot_colour()`**: Returns the plot color.
- **`get_particle_colour()`**: Returns the particle color.
- **`get_custom_colours()`**: Returns the custom particle colors.
- **`get_custom_sizes()`**: Returns the custom particle sizes.
- **`get_line_weight()`**: Returns the line weight.
- **`get_line_colour()`**: Returns the line color.
- **`get_line_style()`**: Returns the line style.
- **`get_line_custom_colours()`**: Returns the custom line colors.

- **`display()`**: Currently an abstract method for future customization.

#### OOP Principles Implemented

1. **Encapsulation**:
   - Attributes are private to ensure safe data access via getter methods.

2. **Inheritance & Abstraction**:
   - Inherits from the `Settings` class and provides an empty implementation of the abstract `display` method.

3. **Builder Pattern**:
   - Separates the building logic from the class itself, making it easier to construct complex configurations.

## Example Usage
```python
# Example usage of FigureSettings with the builder pattern
figure_settings = FigureSettings.Builder()\
    .set_fig_size((8, 8))\
    .set_background('white')\
    .set_edge_colour('black')\
    .set_particle_colour('blue')\
    .set_line_weight(2)\
    .build()

# Accessing the settings
print(figure_settings.get_fig_size())
print(figure_settings.get_background())
print(figure_settings.get_edge_colour())
print(figure_settings.get_particle_colour())
print(figure_settings.get_line_weight())
```

## animation_settings.py

The `AnimationSettings` class encapsulates the configuration details required for animations, such as frame count, interval between frames, and line visibility.

#### Key Features
- **Builder Pattern**: The inner `Builder` class allows fluent API access for setting up the `AnimationSettings` object step-by-step.
- **Encapsulation**: Configuration properties are accessible through getter methods only.

### `AnimationSettings.Builder` (Inner Class)

- Uses the builder pattern to facilitate the creation of an `AnimationSettings` instance.
- Provides method chaining to configure animation properties.

#### Methods
- **`set_lines(boolean)`**: Configures whether to draw lines between frames.
- **`set_frames(frames)`**: Specifies the number of animation frames.
- **`set_interval(interval)`**: Sets the interval (in milliseconds) between frames.
- **`set_blit(boolean)`**: Configures whether to use blitting for faster rendering.
- **`build()`**: Returns a configured `AnimationSettings` object.

### `AnimationSettings` (Outer Class)

- Stores the animation properties, such as frame count, interval, line visibility, and blitting.

#### Attributes
- **`__lines`**: Whether to draw lines between frames.
- **`__frames`**: Number of frames in the animation.
- **`__interval`**: Interval between frames in milliseconds.
- **`__blit`**: Whether to use blitting for faster rendering.

#### Methods
- **`get_lines()`**: Returns whether lines are to be drawn between frames.
- **`get_frames()`**: Returns the total number of frames.
- **`get_interval()`**: Returns the interval between frames in milliseconds.
- **`get_blit()`**: Returns whether blitting is enabled.
- **`display()`**: Currently an abstract method intended for future expansion.

#### OOP Principles Implemented

1. **Encapsulation**:
   - Private attributes prevent external modification, providing safe data access via getter methods.

2. **Inheritance & Abstraction**:
   - Inherits from the `Settings` abstract class and provides a stub implementation of `display`.

3. **Builder Pattern**:
   - Simplifies object creation by separating the setup logic from the main class.

## Example Usage
```python
# Example usage of AnimationSettings with the builder pattern
animation_settings = AnimationSettings.Builder()\
    .set_lines(True)\
    .set_frames(300)\
    .set_interval(25)\
    .set_blit(True)\
    .build()

# Accessing the settings
print(animation_settings.get_lines())
print(animation_settings.get_frames())
print(animation_settings.get_interval())
print(animation_settings.get_blit())
```
# Results and conclusions:

- **Results**: The planetary simulation system successfully showcases the dynamic movements of celestial bodies, providing insightful visualization and accurate data representation of their orbital mechanics.

- **Challenges**: Significant challenges were encountered during the animation creation and interface implementation, specifically optimizing the rendering of smooth animations while ensuring accurate calculations and minimizing resource usage.

- **System Robustness**: The design structure ensures modularity and maintainability, resulting in reusable and adaptable components that facilitate smooth data processing and flexible configuration management.

- **OOP Benefits**: Implementing Object-Oriented Programming principles led to an efficient architecture that emphasizes abstraction, encapsulation, inheritance, and polymorphism, thereby allowing new features to be easily incorporated in the future.

- **Program Achievements**: The program achieves realistic simulations by calculating orbital mechanics using scientifically accurate data. It also includes customizable settings for animations, figure plotting, and data handling, offering users flexibility in configuring the simulation environment.

- **Future Prospects**: Future developments could include implementing new acceleration calculation methods like adaptive time-stepping, optimizing animations, and incorporating a dashboard that provides live data analysis. This would make the program more comprehensive and useful for both educational and research purposes.

- **Extensibility**: The modular design lays a solid foundation for future enhancements, including adding new acceleration calculation methods, optimizing animations, and developing an intuitive dashboard for live data analysis.


