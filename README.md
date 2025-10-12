# Wolfram Language MCP Server

A Model Context Protocol (MCP) server that provides powerful mathematical computation capabilities via Wolfram Language/Mathematica integration. Built with FastMCP for seamless integration with Claude Desktop.

## Features

- **Mathematical Calculations** - Evaluate complex expressions
- **Equation Solving** - Solve algebraic and differential equations
- **Calculus Operations** - Integration and differentiation
- **Matrix Operations** - Linear algebra computations
- **Statistical Analysis** - Statistical measures and data analysis
- **Symbolic Mathematics** - Simplify, factor, and expand expressions
- **Arbitrary Code Execution** - Execute any Wolfram Language code
- **Data Visualization Workflow** - Generate data with Wolfram, visualize with React/Python

## Prerequisites

- Python 3.10+
- Wolfram Mathematica 14.0+ or Wolfram Engine (free for developers)
- Claude Desktop

## Installation

### 1. Install Wolfram Mathematica or Wolfram Engine

**Option A: Wolfram Mathematica** (Commercial)
- Download from [Wolfram Research](https://www.wolfram.com/mathematica/)

**Option B: Wolfram Engine** (Free for developers)
- Download from [Wolfram Engine](https://www.wolfram.com/engine/)
- Requires free license activation

### 2. Install the MCP Server

```bash
# Clone the repository
git clone https://github.com/paraporoco/Wolfram-MCP.git
cd Wolfram-MCP

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Claude Desktop

Add to your Claude Desktop configuration file:

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`  
**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "wolfram": {
      "command": "C:\\Users\\YOUR_USERNAME\\Projects\\Wolfram-MCP\\venv\\Scripts\\python.exe",
      "args": [
        "C:\\Users\\YOUR_USERNAME\\Projects\\Wolfram-MCP\\wolfram_mcp_server.py"
      ]
    }
  }
}
```

**Note:** Adjust paths according to your installation location.

### 4. Verify Installation

Restart Claude Desktop and ask:
```
Can you test the Wolfram connection?
```

Claude should use the `wolfram_test_connection` tool and report success.

## Available Tools

| Tool | Description | Example |
|------|-------------|---------|
| `wolfram_calculate` | Evaluate mathematical expressions | `2 + 2`, `Integrate[x^2, x]` |
| `wolfram_solve` | Solve equations | Solve `x^2 - 5x + 6 == 0` for `x` |
| `wolfram_integrate` | Compute integrals | Integrate `x^2` with respect to `x` |
| `wolfram_differentiate` | Compute derivatives | Differentiate `x^3 + 2x^2 + x` |
| `wolfram_simplify` | Simplify expressions | Simplify `(x^2 - 1)/(x - 1)` |
| `wolfram_factor` | Factor expressions | Factor `x^2 - 5x + 6` |
| `wolfram_expand` | Expand expressions | Expand `(x + 1)^3` |
| `wolfram_matrix_operations` | Matrix computations | Inverse of `{{1,2},{3,4}}` |
| `wolfram_statistics` | Statistical analysis | Mean of `{1, 2, 3, 4, 5}` |
| `wolfram_execute` | Execute arbitrary Wolfram code | `Table[Prime[n], {n, 1, 10}]` |
| `wolfram_test_connection` | Test Wolfram connection | Verify setup |

## Visualization Workflow

The Wolfram MCP excels at mathematical computation but returns symbolic representations rather than rendered images. For visual graphs and charts, use the hybrid workflow:

**Wolfram (Computation) → Data Extraction → Visualization Tool (Rendering)**

📖 **[Complete Visualization Guide](VISUALIZATION_WORKFLOW.md)** - Comprehensive documentation on creating beautiful, interactive charts

### Quick Example

1. **Generate data with Wolfram:**
```wolfram
Table[{x, Sin[x], Cos[x]}, {x, 0, 2*Pi, 0.1}]
```

2. **Visualize with React or Python:**
- See [`examples/trig_visualization.jsx`](examples/trig_visualization.jsx) for interactive React charts
- See [`examples/trig_plot.py`](examples/trig_plot.py) for publication-quality matplotlib plots

📁 **[View All Examples](examples/)** - Complete working examples with code

---

## Usage Examples

### Basic Mathematics
```
What is the integral of x^2?
Solve the equation x^2 - 5x + 6 = 0
```

### Advanced Calculus
```
Find the derivative of sin(x) * cos(x)
Compute the definite integral of x^2 from 0 to 1
```

### Linear Algebra
```
Calculate the inverse of the matrix {{1,2},{3,4}}
Find the eigenvalues of {{4,1},{2,3}}
```

### Statistics
```
What is the mean of the dataset {1, 2, 3, 4, 5}?
Calculate the standard deviation of {10, 20, 30, 40, 50}
```

### Symbolic Math
```
Simplify (x^2 - 1)/(x - 1)
Factor x^2 - 5x + 6
Expand (x + 1)^3
```

## Configuration

The server defaults to using WolframScript at:
```
C:\Program Files\Wolfram Research\Mathematica\14.0\wolframscript.exe
```

To use a different version or location, modify the paths in `wolfram_mcp_server.py`:
```python
WOLFRAM_SCRIPT_PATH = r"C:\Your\Custom\Path\wolframscript.exe"
MATH_KERNEL_PATH = r"C:\Your\Custom\Path\MathKernel.exe"
```

## Troubleshooting

### "Wolfram Language Not Found"
- Verify Mathematica/Wolfram Engine is installed
- Check the paths in `wolfram_mcp_server.py` match your installation
- Ensure Wolfram Engine is activated (run `wolframscript` in terminal)

### "Connection Test Failed"
- Make sure your Mathematica license is active
- Try running `wolframscript -code "2+2"` in your terminal
- Check that the executable path is correct

### "Execution Timed Out"
- Complex calculations may need more time
- Use `wolfram_execute` with a custom timeout parameter
- Consider simplifying the expression

## Development

### Project Structure
```
Wolfram-MCP/
├── wolfram_mcp_server.py    # Main server implementation
├── requirements.txt          # Python dependencies
├── README.md                # Documentation
├── LICENSE                  # MIT License
└── venv/                    # Virtual environment (not in git)
```

### Running Tests
```bash
# Test the connection directly
python wolfram_mcp_server.py

# Use with Claude Desktop to test all tools
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License - see [LICENSE](LICENSE) file for details

## Acknowledgments

- Built with [FastMCP](https://github.com/jlowin/fastmcp) by Marvin
- Powered by [Wolfram Language](https://www.wolfram.com/language/)
- Designed for [Claude Desktop](https://claude.ai/download)

## Links

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [Wolfram Language Documentation](https://reference.wolfram.com/language/)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)

## Support

For issues and questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Refer to Wolfram Language documentation for syntax help

---

**Made with ❤️ for the Claude + Wolfram community**
