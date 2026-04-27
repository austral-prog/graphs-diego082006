[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/dhP-wksu)
# Data Visualization Assignment

## Objective
Create a Jupyter Notebook that demonstrates your ability to generate and customize different types of plots using Matplotlib in Python. The notebook should contain **5 distinct visualizations** with explanations.

## Requirements

### Notebook Specifications
- File name: `visualization_assignment.ipynb`
- Exported notebook to html: `visualization_assignment.html`
- Must include Markdown cells explaining each visualization
- Clean, well-organized code with comments
- All imports at the top of the notebook
- Kernel should be restarted and run all before submission (ensure no errors)

### Graph Requirements
Each of the 5 graphs must:
1. Have a **descriptive title**
2. Include **properly labeled axes** (with units if applicable)
3. Include a **legend** when showing multiple data series
4. Use **appropriate plot type** for the data
5. Demonstrate **custom styling** (colors, markers, line styles, etc.)
6. Include 2-3 sentences explaining **what the graph shows** and **why you chose this visualization**

### Suggested Graph Types (Choose 5):
- Line plot (time series or function)
- Bar chart (comparison)
- Histogram (distribution)
- Scatter plot (relationship)
- Pie chart (composition)
- Box plot (statistics)
- Heatmap (correlation)
- Custom/advanced plot (3D, subplots, etc.)

## Submission Files

```
 visualization_assignment.ipynb
 visualization_assignment.html
 imgs/
  ├── line_plot.png
  ├── bar_chart.png
  ├── histogram.png
  ├── scatter_plot.png
  └── custom_plot.png
```

### Image Export Requirements:
- Save each graph as PNG in an `imgs` directory
- Use descriptive filenames (e.g., `temperature_trends.png`)
- Ensure images are clearly visible (adjust DPI if needed)
- Export using: `plt.savefig('imgs/filename.png', dpi=300, bbox_inches='tight')`

## Data Sources
You may use:
1. Generated data (using NumPy)
2. Built-in datasets (e.g., `seaborn.load_dataset()`)
3. Simple CSV files (include in submission if not built-in)
4. Real-world data (include source attribution)

## Resources
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [NumPy Random Sampling](https://numpy.org/doc/stable/reference/random/index.html)
- [Seaborn Example Datasets](https://seaborn.pydata.org/generated/seaborn.load_dataset.html)
