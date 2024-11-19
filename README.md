# SwissCheese_Public
Red team persistence toolkit

---

## Motivation
During simulated cyber-attacks ensuring persistent access for the red team (simulated attackers) across multiple devices and platforms can be a daunting and time-consuming task. The manual effort required to implement and manage persistence methods on a large scale, especially in diverse environments with Linux and Windows systems, can lead to inefficiencies and inconsistencies.

To address these challenges, **Swiss Cheese** is being developed as an automation framework tailored to the needs of the red team during simulated cyber-attacks. The framework intends to simplify setting up and managing persistent access on both Linux and Windows devices.

## Key Objectives
- **Efficiency**: Automates persistence tasks to minimize the time and effort required during cybersecurity exercises.
- **Scalability**: Can deploy persistence mechanisms across large networks of devices with minimal manual input.
- **Stealth**: Enhances the realism of engagements by focusing on persistence methods that evade detection.

## Features
1. **Automation**:
    - Streamlines the deployment of persistence methods across both Linux and Windows systems.
    - Reduces the manual labor typically required to maintain persistence across a variety of systems.
2. **Comprehensive Library of Persistence Methods**:
    - A detailed library documenting persistence techniques for both Linux and Windows platforms, including:
    - For more specific details reference the readme within the relevant folder
    - The library serves as a reference for quickly deploying persistence mechanisms.
    - Linux
        - Startup scripts
        - Root user creation
        - Service manipulation
        - Bianary swaping
        - Cronjobs
        - SSH keys
        - Ailiases
        - Login scripts
    - Windows
        - User creation
        - RDP enabling
    - The library serves as a reference for quickly deploying persistence mechanisms.
---

### New Features
1. **Modular and Extensible**:
    - Written in Python, Bash, and Batch scripting to ensure cross-platform compatibility.
    - Modular design allows red teams to customize and extend the framework based on their specific engagement needs.
    
### Features Under Development


1.  **Stealth and Evasion**:
    - Includes obfuscation techniques and anti-detection measures to ensure persistence methods are less likely to be detected by defensive tools or logging mechanisms.
    - Helps maintain a realistic and challenging environment for blue teams during exercises.

### Technologies
- **Python**: The core language for cross-platform automation, providing the backbone for calling Bash and Batch scripts.
- **Bash Scripting**: Used for implementing persistence methods on Linux devices, ensuring compatibility with Unix-like environments.
- **Batch Scripting**: Employed for persistence tasks on Windows devices, enabling efficient automation within Windows environments.

## Development Issues/Notes

---

- 
- **Windows**: Research Items
    -  What additional persistence is possible on windows
-  **Stealth**: Research Items
    - How can I edit logs to hide the scripts running

## Summary

---

**Swiss Cheese** will be a powerful automation framework designed to enhance the efficiency, scalability, and stealth of red team members during engagements. By automating the deployment and management of persistence methods across both Linux and Windows devices, **Swiss Cheese** allows red teams to focus on their primary objective—maintaining persistent access to compromised systems throughout their engagements.

---

### GNU General Public License v3.0
Swiss Cheese is distributed under the terms of the GNU General Public License v3.0.

You can view the full license at: [https://www.gnu.org/licenses/gpl-3.0.en.html](https://www.gnu.org/licenses/gpl-3.0.en.html)

