# File Organizer & Image Analysis

This project is an automated file organizer and image analysis tool using Python and Jupyter Notebook. The project is structured into three main steps, each with specific functionality to move, categorize, and analyze the files present in a starting directory.

## Project Features

1. **File Organization by Type & Dynamic Updates**: Moves files to subfolders based on their type (audio, documents, images). Updates subfolders and the recap file each time the script is executed.
2. **Command-Line Interface (CLI)**: Allows you to move a single file to the appropriate subfolder using an executable.
3. **Image Analysis**: Analyzes image files to determine if they are grayscale, RGB, or RGBA, and generates a summary table with the information.

---

## Project Structure

The project follows the following structure:


---

## Requirements

To run this project, you need to install the following Python libraries:

```bash
pip install os
pip install shutil
pip install csv
pip install numpy
pip install pillow
pip install tabulate
pip install argparse
```

---

## Phases of Development

  ### 1 - File Organization
  The script within the **fileorganizer.ipynb** iterates through the files in the **files** folder, classifies them based on their format, and moves them to specific subfolders: **audio/**, **docs/**, **images/**. If a subfolder does not exist, it will be automatically created.

Additionally, the script collects file information (name, type, size in bytes) and saves it in a recap.csv file for tracking purposes.

**How to run the script**:

Open the **fileorganizer.ipynb**.
Execute the cell related to Step 1 to organize the files and update the recap.
During execution, information about each file (name, type, size in bytes) will be printed.

  ### 2 - CLI Executable for Single File Moving

  ### 3 - Image Analysis

---

## Conclusions

