# Examples

This directory contains practical examples demonstrating the Wolfram MCP visualization workflow.

## Files

### `trig_visualization.jsx`
Interactive React component visualizing trigonometric functions.

**Features:**
- Toggle buttons to show/hide functions
- Interactive tooltips
- Responsive design using Recharts
- Data computed with Wolfram Language

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
Python script creating publication-quality matplotlib plots.

**Features:**
- Dual-panel layout
- Shaded regions
- High-resolution export (PNG, PDF)
- Annotation and styling

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

## Quick Start

### 1. Generate Data with Wolfram MCP

```python
from wolfram_mcp_server import WolframMCPServer

# In your Claude conversation:
# "Use Wolfram to compute: Table[{x, Sin[x], Cos[x]}, {x, 0, 2*Pi, 0.1}]"
```

### 2. Choose Your Visualization Method

**For Web/Interactive:**
```jsx
// Use trig_visualization.jsx as template
// Replace wolframData with your computed values
```

**For Static/Publication:**
```python
# Use trig_plot.py as template
# Modify data source or regenerate with numpy
```

---

## Workflow Pattern

```
┌─────────────────┐
│  Wolfram MCP    │  1. Compute precise mathematical data
│  (Computation)  │     Table[], Integrate[], Solve[], etc.
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Data Extraction │  2. Extract numerical values
│  Table[], N[]   │     Format: arrays, lists, numbers
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Visualization  │  3. Create visual output
│  React/Python   │     Interactive or static plots
└─────────────────┘
```

---

## More Examples Coming Soon

- 3D surface plots
- Statistical distributions
- Parametric curves
- Animation examples
- Real-time data visualization

---

## Resources

- [Main Workflow Documentation](../VISUALIZATION_WORKFLOW.md)
- [Wolfram Language Docs](https://reference.wolfram.com/)
- [Recharts Docs](https://recharts.org/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/)
