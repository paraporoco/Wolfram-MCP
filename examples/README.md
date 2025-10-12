# Examples

This directory contains practical examples demonstrating the Wolfram MCP visualization workflow and statistical calculations.

## Files

### `standard_deviation_example.md`
Comprehensive guide to calculating standard deviation and statistical measures with Wolfram Language.

**Features:**
- Basic to advanced standard deviation calculations
- Population vs sample standard deviation
- Z-score calculations
- Moving averages
- Interactive Claude usage examples
- Visualization integration with Python

**Topics Covered:**
- Mean, median, variance
- Coefficient of variation
- Quartiles and IQR
- Outlier detection
- Time series analysis

**Usage:**
```
Calculate the standard deviation of {10, 20, 30, 40, 50}
```

---

### `statistical_distributions.py`
Python script for visualizing multiple statistical distributions with comprehensive analysis.

**Features:**
- Multiple distribution types (Normal, Uniform, Exponential, Chi-Square)
- 6-panel visualization layout
- Histogram overlays
- Box plot comparisons
- Q-Q plots for normality testing
- Cumulative distribution functions (CDF)
- Statistical summary tables

**Usage:**
```bash
python3 statistical_distributions.py
```

**Dependencies:**
```bash
pip install matplotlib numpy scipy
```

**Output:**
- `statistical_distributions.png` (150 DPI multi-panel plot)

---

### `trig_visualization.jsx`
Interactive React component visualizing trigonometric functions.

**Features:**
- Toggle buttons to show/hide sin, cos, tan functions
- Interactive tooltips with precise values
- Responsive design using Recharts
- Data computed with Wolfram Language
- Smooth animations

**Usage:**
```jsx
import TrigVisualization from './examples/trig_visualization';

function App() {
  return <TrigVisualization />;
}
```

**Dependencies:**
```bash
npm install recharts react
```

---

### `trig_plot.py`
Python script creating publication-quality matplotlib plots of trigonometric functions.

**Features:**
- Dual-panel layout (functions + derivatives)
- Shaded regions for emphasis
- High-resolution export (PNG, PDF)
- Professional annotations
- Publication-ready styling

**Usage:**
```bash
python3 trig_plot.py
```

**Dependencies:**
```bash
pip install matplotlib numpy
```

**Output:**
- `trig_functions.png` (150 DPI)
- `trig_functions.pdf` (vector format)

---

### `surface_3d.py`
Python script for creating 3D surface plots using matplotlib.

**Features:**
- 3D surface visualization
- Configurable viewing angles
- Color mapping and shading
- Contour projections
- High-resolution export

**Usage:**
```bash
python3 surface_3d.py
```

**Dependencies:**
```bash
pip install matplotlib numpy
```

**Output:**
- 3D surface plot PNG file

---

### `surface_3d.jsx`
Interactive React component for 3D surface visualization.

**Features:**
- Interactive 3D rendering
- Mouse controls for rotation
- Real-time updates
- WebGL acceleration
- Data computed with Wolfram Language

**Usage:**
```jsx
import Surface3D from './examples/surface_3d';

function App() {
  return <Surface3D />;
}
```

**Dependencies:**
```bash
npm install react-three-fiber three
```

---

## Quick Start

### 1. Generate Data with Wolfram MCP

#### Statistical Data
```
Calculate the mean, standard deviation, and variance of {10, 20, 30, 40, 50}
```

#### Function Data
```
Use Wolfram to compute: Table[{x, Sin[x], Cos[x]}, {x, 0, 2*Pi, 0.1}]
```

#### 3D Surface Data
```
Generate 3D surface data: Table[{x, y, Sin[x]*Cos[y]}, {x, -π, π, 0.2}, {y, -π, π, 0.2}]
```

### 2. Choose Your Visualization Method

**For Web/Interactive:**
```jsx
// Use .jsx templates for interactive React visualizations
// - trig_visualization.jsx for 2D function plots
// - surface_3d.jsx for 3D surface plots
```

**For Static/Publication:**
```python
# Use .py templates for publication-quality matplotlib plots
# - trig_plot.py for 2D function plots
# - surface_3d.py for 3D surface plots
# - statistical_distributions.py for statistical analysis
```

**For Documentation/Learning:**
```markdown
# See .md files for comprehensive examples
# - standard_deviation_example.md for statistics tutorials
```

---

## Workflow Pattern

```
┌─────────────────────────┐
│     Wolfram MCP         │  1. Compute precise mathematical data
│    (Computation)        │     Table[], Statistics[], Solve[], etc.
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│   Data Extraction       │  2. Extract numerical values
│   Table[], N[], ToList  │     Format: arrays, lists, JSON
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│    Visualization        │  3. Create visual output
│   React/Python/Both     │     Interactive or static plots
└─────────────────────────┘
```

---

## Example Workflows

### Statistical Analysis Workflow
1. **Calculate with Wolfram:**
   ```
   What's the standard deviation of {85, 92, 78, 95, 88, 91, 76, 89}?
   ```

2. **Visualize with Python:**
   ```python
   # Use statistical_distributions.py as template
   # Modify data variable with your dataset
   python3 statistical_distributions.py
   ```

### Function Plotting Workflow
1. **Generate data with Wolfram:**
   ```
   Create a table of sine and cosine values from 0 to 2π with 0.1 step
   ```

2. **Choose visualization:**
   - **Interactive:** Use `trig_visualization.jsx`
   - **Static:** Use `trig_plot.py`

### 3D Surface Workflow
1. **Generate surface data with Wolfram:**
   ```
   Generate a 3D grid of Sin[x]*Cos[y] from -π to π
   ```

2. **Visualize:**
   - **Interactive 3D:** Use `surface_3d.jsx`
   - **Static 3D:** Use `surface_3d.py`

---

## Tips for Best Results

### Data Generation
- Use `N[]` in Wolfram for numerical precision
- Use `Table[]` for structured data generation
- Consider `ToList` or `Flatten` for data formatting
- Specify appropriate step sizes for smooth plots

### Visualization
- **React/JSX:** Best for interactive web applications
- **Python/Matplotlib:** Best for publication-quality static images
- **Both:** Use Python for initial analysis, React for presentation

### Performance
- Limit data points for interactive visualizations (< 1000 points recommended)
- Use higher resolution for static plots
- Cache Wolfram computations for repeated visualizations

---

## Resources

- [Main Workflow Documentation](../VISUALIZATION_WORKFLOW.md)
- [Wolfram Language Documentation](https://reference.wolfram.com/)
- [Standard Deviation Examples](standard_deviation_example.md)
- [Recharts Documentation](https://recharts.org/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/)
- [Three.js Documentation](https://threejs.org/)

---

## Contributing

Have a great example? Submit a PR with:
1. Well-commented code
2. Clear usage instructions
3. Dependencies list
4. Example output (if applicable)

---

**Made with ❤️ for the Claude + Wolfram community**
