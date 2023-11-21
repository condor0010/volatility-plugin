# Final Plugin Development Report

## Project Title: Volatility 3 Plugin Development

**Team Members:**
- Louie Orcinolo
- Nick Falco
- Chandler Hake
- Remi Greko

**Date:** September 28, 2023

### 1. Topic Planned to Develop Plugin On

The focus of our plugin development project is to create a plugin for Volatility 3 that allows us to analyze and extract information related to Linux cgroups. Specifically, we aim to develop a plugin that will enable us to identify and list the cgroups running on a Linux system along with their associated Process IDs (PIDs). This information will provide valuable insights into the containers running on the system, as OCI containers are built on top of cgroups.

### 2. Operating System Targeted

Our plugin will be designed to work with Linux operating systems. This will be compatible with a wide range of Linux distributions, making it a versatile tool for digital forensics and system analysis.

### 3. Workflow of the Plugin Planned to be Developed

The workflow of our plugin can be broken down into the following key steps:

**Step 1: Data Collection**
- The plugin will scan the `/sys/fs/cgroup/` directory on the target Linux system to collect information about the cgroups.

**Step 2: Parsing**
- The collected data will be parsed to extract details about each cgroup, including its name and associated PIDs.

**Step 3: Output Generation**
- The plugin will generate a user-friendly report containing a list of cgroups and their associated PIDs. This report will be presented in a format that can be easily analyzed by digital forensic investigators.

**Step 4: User Interaction**
- The user will execute the plugin through Volatility 3, providing the necessary parameters and options.

**Step 5: Plugin Execution**
- The plugin will execute, collecting and parsing the data, and finally, generating the report.

### 4. Tasks Assigned to Each Group Member

To efficiently complete this project, each team member has been assigned specific tasks:

- **Louie Orcinolo**
  - Task: Implement the data collection module.
  - Responsibilities: Develop code to scan the `/sys/fs/cgroup/` directory and gather information about cgroups.

- **Chandler Hake**
  - Task: Implement the parsing module/_generator.
  - Responsibilities: Develop code to parse the collected data and extract cgroup details, including names and associated PIDs.
 
- **Remi Greko**
  - Task: Implement _generator functionality
  - Responsibilities: Develop code with Chandler to establish _generator functinality to act as a parser for output preparation.
  
- **Nick Falco**
  - Task: Implement the output generation module.
  - Responsibilities: Create code to generate a comprehensive report, presenting cgroups and their associated PIDs in a readable format.

### 5. Timeline Planned to Submit the Plugin

We have established the following timeline for the development and submission of our Volatility 3 plugin:

- **Week 1**: Completion of data collection module (Louie Orcinolo)
- **Week 2**: Completion of parsing module (Nick Falco)
- **Week 3**: Completion of output generation module (Chandler Hake)
- **Week 4**: Integration of modules and initial plugin testing
- **Week 5**: Bug fixes and final testing
- **Week 6**: Submission of the Volatility 3 cgroup plugin

This timeline is subject to change, shit happens.
