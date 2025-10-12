# Wolfram MCP Visualization Workflow

## Overview

This guide documents the best practices for creating visual graphs and charts using Wolfram MCP in combination with modern visualization tools. The Wolfram MCP excels at mathematical computation but returns symbolic representations rather than rendered images. This workflow combines Wolfram's computational power with visualization libraries to create beautiful, interactive charts.

## The Problem

When you execute plotting commands in Wolfram Language through the MCP:

```wolfram
Plot[Sin[x], {x, 0, 2*Pi}]
```

You receive a **symbolic Graphics object** rather than a rendered image:

```
Legended[-Graphics-, ...]
```

This is because the MCP operates in a text-based environment without graphics rendering capabilities.

## The Solution: Hybrid Workflow

### Best Workflow Pattern

```
Wolfram MCP (Computation) → Data Extraction → Visualization Tool (Rendering)
```

**Step 1:** Use Wolfram for precise mathematical computations  
**Step 2:** Extract numerical data from Wolfram  
**Step 3:** Visualize using React, Python, or other visualization libraries

---

## Method 1: Wolfram → React (Interactive Web Visualization)

### Advantages
- ✅ Fully interactive (zoom, pan, toggle)
- ✅ Beautiful, modern UI
- ✅ Responsive and web-ready
- ✅ Great for dashboards and reports

### Workflow

#### Step 1: Generate Data with Wolfram

```wolfram
Table[{x, Sin[x], Cos[x], Sin[x]*Cos[x]}, {x, 0, 2*Pi, 0.2}]
```

This returns a nested array of numerical values.

#### Step 2: Convert to JavaScript Format

Transform the Wolfram output into JavaScript array syntax:

```javascript
const data = [
  {x: 0.0, sin: 0.0, cos: 1.0, product: 0.0},
  {x: 0.2, sin: 0.199, cos: 0.980, product: 0.195},
  // ... more data points
];
```

#### Step 3: Create React Component

Use a charting library like **Recharts**:

```jsx
import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

export default function Chart() {
  return (
    <ResponsiveContainer width="100%" height={400}>
      <LineChart data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="x" label={{ value: 'x (radians)', position: 'insideBottom' }} />
        <YAxis label={{ value: 'y', angle: -90, position: 'insideLeft' }} />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="sin" stroke="#3b82f6" strokeWidth={2} name="Sin(x)" />
        <Line type="monotone" dataKey="cos" stroke="#10b981" strokeWidth={2} name="Cos(x)" />
      </LineChart>
    </ResponsiveContainer>
  );
}
```

### Libraries to Use

- **Recharts**: Simple, React-native charts (recommended for beginners)
- **D3.js**: Maximum customization and control
- **Plotly.js**: Scientific/engineering visualizations
- **Chart.js**: Lightweight, general-purpose

---

## Method 2: Wolfram → Python (Static Publication-Quality Plots)

### Advantages
- ✅ Publication-quality exports (PNG, PDF, SVG)
- ✅ Extensive customization options
- ✅ Perfect for reports and papers
- ✅ Integrates with scientific Python ecosystem

### Workflow

#### Step 1: Generate Data with Wolfram

Same as React method - use `Table` or other data generation functions.

#### Step 2: Create Python Script

```python
import matplotlib.pyplot as plt
import numpy as np

# Data from Wolfram or generate with numpy
x = np.linspace(0, 2*np.pi, 100)
sin_x = np.sin(x)
cos_x = np.cos(x)

# Create plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, sin_x, 'b-', linewidth=2, label='Sin(x)')
ax.plot(x, cos_x, 'g-', linewidth=2, label='Cos(x)')
ax.grid(True, alpha=0.3)
ax.set_xlabel('x (radians)', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Trigonometric Functions', fontsize=14, fontweight='bold')
ax.legend()

# Save high-resolution image
plt.savefig('plot.png', dpi=150, bbox_inches='tight')
```

#### Step 3: Export and Use

```bash
python3 plot_script.py
```

Produces a high-quality PNG file suitable for inclusion in documents, presentations, or publications.

### Python Libraries to Use

- **Matplotlib**: Industry standard, highly customizable
- **Seaborn**: Statistical visualizations with beautiful defaults
- **Plotly**: Interactive HTML exports
- **Bokeh**: Interactive web-ready plots

---

## Method 3: Direct Wolfram Computation → Visualization

### When Wolfram is Enough

For quick checks and symbolic analysis, Wolfram's text output is often sufficient:

```wolfram
Integrate[x^2, x]
(* Returns: x^3/3 *)

Solve[x^2 - 5x + 6 == 0, x]
(* Returns: {{x -> 2}, {x -> 3}} *)
```

### When You Need Visualization

- Exploring function behavior visually
- Creating reports or presentations
- Comparing multiple datasets
- Interactive exploration of parameters

---

## Complete Example: End-to-End Workflow

### Scenario: Visualize a Complex Function

**Objective:** Plot the function `f(x) = sin(x) * e^(-x/10)` from 0 to 4π

#### Step 1: Use Wolfram MCP for Computation

```wolfram
wolfram:wolfram_execute(
  "Table[{x, Sin[x]*Exp[-x/10]}, {x, 0, 4*Pi, 0.1}]"
)
```

**Result:** Array of [x, y] pairs with precise numerical values

#### Step 2: Create Interactive React Visualization

```jsx
import React from 'react';
import { LineChart, Line, XAxis, YAxis, ResponsiveContainer, Tooltip } from 'recharts';

const wolframData = [
  {x: 0.0, y: 0.0},
  {x: 0.1, y: 0.0995},
  // ... data from Wolfram
];

export default function DampedSineWave() {
  return (
    <div className="p-8 bg-white rounded-lg shadow-lg">
      <h2 className="text-2xl font-bold mb-4">Damped Sine Wave: f(x) = sin(x)·e^(-x/10)</h2>
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={wolframData}>
          <XAxis dataKey="x" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="y" stroke="#8b5cf6" strokeWidth={2} dot={false} />
        </LineChart>
      </ResponsiveContainer>
      <p className="text-sm text-gray-600 mt-4">
        Data computed using Wolfram Language MCP
      </p>
    </div>
  );
}
```

#### Step 3 (Alternative): Create Python Plot

```python
import matplotlib.pyplot as plt
import numpy as np

# From Wolfram or regenerate
x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x) * np.exp(-x/10)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'purple', linewidth=2)
plt.fill_between(x, 0, y, alpha=0.3, color='purple')
plt.xlabel('x (radians)')
plt.ylabel('f(x)')
plt.title('Damped Sine Wave: f(x) = sin(x)·e^(-x/10)')
plt.grid(True, alpha=0.3)
plt.savefig('damped_sine.png', dpi=150)
```

---

## Best Practices

### 1. Data Generation

**✅ Do:**
- Use `Table[]` for discrete data points
- Use `N[]` to force numerical evaluation
- Generate appropriate number of points (50-200 for smooth curves)

**❌ Don't:**
- Return symbolic expressions when you need numbers
- Generate excessive data points (>1000) for simple plots
- Forget to specify ranges and step sizes

### 2. Data Transfer

**✅ Do:**
- Parse Wolfram arrays carefully
- Maintain precision (3-4 decimal places usually sufficient)
- Structure data for your visualization library

**❌ Don't:**
- Manually transcribe large datasets
- Lose precision unnecessarily
- Use incompatible data formats

### 3. Visualization Choice

**Choose React when:**
- Building web applications
- Need user interaction
- Creating dashboards
- Want responsive layouts

**Choose Python when:**
- Creating static exports
- Writing papers/reports
- Batch processing many plots
- Need publication quality

---

## Common Patterns

### Pattern 1: Compare Multiple Functions

```wolfram
data = Table[{x, Sin[x], Cos[x], Tan[x]}, {x, -Pi, Pi, 0.1}]
```

Visualize with multiple lines/series.

### Pattern 2: Parameter Sweep

```wolfram
Table[{x, Sin[a*x]}, {a, 1, 5}, {x, 0, 2*Pi, 0.1}]
```

Create animated or multi-series plots showing parameter effects.

### Pattern 3: Statistical Analysis

```wolfram
data = RandomVariate[NormalDistribution[0, 1], 1000];
{Mean[data], StandardDeviation[data], Histogram[data]}
```

Use Python's seaborn or matplotlib for distribution plots.

### Pattern 4: Complex Mathematical Surfaces

```wolfram
Table[{x, y, Sin[x]*Cos[y]}, {x, -Pi, Pi, 0.2}, {y, -Pi, Pi, 0.2}]
```

Use Plotly or three.js for 3D interactive visualization.

---

## Troubleshooting

### Issue: Wolfram Returns Symbolic Graphics

**Problem:** `Plot[]` returns `-Graphics-` text

**Solution:** Use `Table[]` to extract numerical data instead of plotting commands

### Issue: Data Format Mismatch

**Problem:** Wolfram array structure doesn't match your visualization library

**Solution:** Transform data structure in JavaScript/Python:

```javascript
// Wolfram: [[x1, y1], [x2, y2], ...]
// Transform to: [{x: x1, y: y1}, {x: x2, y: y2}, ...]
const formatted = wolframData.map(([x, y]) => ({x, y}));
```

### Issue: Too Many Data Points

**Problem:** Chart is slow or cluttered

**Solution:** Reduce points in Wolfram `Table[]` or downsample in your code:

```javascript
const downsampled = data.filter((_, index) => index % 5 === 0);
```

---

## Examples Directory

See the `examples/` directory for complete working examples:

- `trig_visualization.jsx` - Interactive trigonometric functions
- `damped_wave.py` - Python matplotlib example
- `statistical_analysis.jsx` - Statistical data visualization
- `3d_surface.jsx` - 3D surface plot with Three.js

---

## Resources

### Wolfram Language
- [Wolfram Language Documentation](https://reference.wolfram.com/language/)
- [Data Manipulation Functions](https://reference.wolfram.com/language/guide/DataManipulation.html)
- [Numerical Computation](https://reference.wolfram.com/language/guide/NumericalComputation.html)

### React Visualization
- [Recharts Documentation](https://recharts.org/)
- [D3.js](https://d3js.org/)
- [Plotly.js](https://plotly.com/javascript/)

### Python Visualization
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Plotly Python](https://plotly.com/python/)

---

## Summary

| Step | Tool | Purpose |
|------|------|---------|
| 1. Compute | Wolfram MCP | Precise mathematical calculations |
| 2. Extract | Table[], N[] | Generate numerical data |
| 3. Format | JavaScript/Python | Transform data structure |
| 4. Visualize | React/Python | Create beautiful charts |

**Key Takeaway:** Use Wolfram MCP for what it does best (computation), then leverage specialized visualization tools for rendering beautiful, interactive graphics.

---

*Last Updated: October 2025*
*Wolfram MCP Server Version: 1.0*
