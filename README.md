# File Organizer & Image Analysis

This project is an automated file organizer and image analysis tool using Python and Jupyter Notebook. The project is structured into three main steps, each with specific functionality to move, categorize, and analyze the files present in a starting directory.

## Project Features

1. **File Organization by Type & Dynamic Updates**: Moves files to subfolders based on their type (audio, documents, images). Updates subfolders and the recap file each time the script is executed.
2. **Command-Line Interface (CLI)**: Allows you to move a single file to the appropriate subfolder using an executable.
3. **Image Analysis**: Analyzes image files to determine if they are grayscale, RGB, or RGBA, and generates a summary table with the information.

---

## Repository Structure

The project follows the following structure:

- files: folder that contains all the files that need to be moved and/or analyzed
- addfile.py: file created to move a single file by the command line
- fileorganizer.ipynb: file created to manage **File Organization & Image Analysis**
- recap.csv: 

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

The **addfile.py** file implements a command-line interface that allows you to move a single file from the **files** folder to the corresponding subfolder (audio, docs, images), while also updating the recap.csv file.

**How to run the executable:**

```bash
python addfile.py <filename>
```

Where **<filename>** is the name of the file to move, including its extension (e.g., trump.jpeg).

If the specified file does not exist, an error message will be displayed.

  ### 3 - Image Analysis

  Step 3 of the script analyzes image files in the **images/** subfolder. Using the **numpy** library, the images are loaded and analyzed to determine whether they are grayscale, RGB, or RGBA.

In the end, a summary table with image information is generated:

File name
- Image type (Grayscale, RGB, RGBA)
- Dimensions (width x height)
- The table is displayed in a readable format using the tabulate library.

**How to run the image analysis:**

Open the **fileorganizer.ipynb**.
Execute the cell related to Step 3 to analyze the images and display the summary table.

---

## Conclusions

This project demonstrates how to automate file management for multimedia and documents, using Python to classify and analyze various types of files. The command-line interface and image analysis features enhance the script's utility, making it suitable for a wide range of file management scenarios.
