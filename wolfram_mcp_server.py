"""
Wolfram Language MCP Server
Provides computational tools via Wolfram Language/Mathematica integration
"""

import subprocess
import json
import tempfile
import os
from pathlib import Path
from typing import Optional, Dict, Any
from fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("Wolfram Language")

# Configuration
WOLFRAM_SCRIPT_PATH = r"C:\Program Files\Wolfram Research\Mathematica\14.0\wolframscript.exe"
MATH_KERNEL_PATH = r"C:\Program Files\Wolfram Research\Mathematica\14.0\MathKernel.exe"

class WolframExecutor:
    """Handles execution of Wolfram Language code"""
    
    def __init__(self, use_kernel: bool = False):
        self.executable = MATH_KERNEL_PATH if use_kernel else WOLFRAM_SCRIPT_PATH
        self.use_kernel = use_kernel
    
    def execute(self, code: str, timeout: int = 30) -> Dict[str, Any]:
        """
        Execute Wolfram Language code and return results
        
        Args:
            code: Wolfram Language code to execute
            timeout: Execution timeout in seconds
            
        Returns:
            Dictionary with 'success', 'result', and optional 'error'
        """
        try:
            result = subprocess.run(
                [self.executable, "-c", code],
                stdin=subprocess.DEVNULL,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            
            if result.returncode == 0:
                output = result.stdout.strip()
                return {
                    "success": True,
                    "result": output,
                    "raw_output": result.stdout,
                    "stderr": result.stderr
                }
            else:
                return {
                    "success": False,
                    "error": f"Execution failed with code {result.returncode}",
                    "stderr": result.stderr,
                    "stdout": result.stdout
                }
                    
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "error": f"Execution timed out after {timeout} seconds"
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Execution error: {str(e)}"
            }

# Initialize executor (switch back to WolframScript)
executor = WolframExecutor(use_kernel=False)

@mcp.tool()
def wolfram_calculate(expression: str) -> str:
    """
    Evaluate a mathematical expression using Wolfram Language.
    
    Args:
        expression: Mathematical expression in Wolfram Language syntax
        
    Examples:
        - "2 + 2"
        - "Integrate[x^2, x]"
        - "Solve[x^2 - 5x + 6 == 0, x]"
        - "Plot[Sin[x], {x, 0, 2*Pi}]"
    """
    result = executor.execute(expression)
    
    if result["success"]:
        return f"Result: {result['result']}"
    else:
        return f"Error: {result['error']}"

@mcp.tool()
def wolfram_solve(equation: str, variable: str) -> str:
    """
    Solve an equation for a variable using Wolfram Language.
    
    Args:
        equation: Equation to solve (use == for equality)
        variable: Variable to solve for
        
    Example:
        equation="x^2 - 5x + 6 == 0", variable="x"
    """
    code = f"Solve[{equation}, {variable}]"
    result = executor.execute(code)
    
    if result["success"]:
        return f"Solution: {result['result']}"
    else:
        return f"Error: {result['error']}"

@mcp.tool()
def wolfram_integrate(expression: str, variable: str, limits: Optional[str] = None) -> str:
    """
    Compute integral using Wolfram Language.
    
    Args:
        expression: Expression to integrate
        variable: Variable of integration
        limits: Optional limits in format "a, b" for definite integral
        
    Examples:
        - expression="x^2", variable="x" (indefinite)
        - expression="x^2", variable="x", limits="0, 1" (definite)
    """
    if limits:
        code = f"Integrate[{expression}, {{{variable}, {limits}}}]"
    else:
        code = f"Integrate[{expression}, {variable}]"
    
    result = executor.execute(code)
    
    if result["success"]:
        return f"Integral: {result['result']}"
    else:
        return f"Error: {result['error']}"

@mcp.tool()
def wolfram_differentiate(expression: str, variable: str, order: int = 1) -> str:
    """
    Compute derivative using Wolfram Language.
    
    Args:
        expression: Expression to differentiate
        variable: Variable to differentiate with respect to
        order: Order of derivative (default 1)
        
    Example:
        expression="x^3 + 2x^2 + x", variable="x", order=1
    """
    if order == 1:
        code = f"D[{expression}, {variable}]"
    else:
        code = f"D[{expression}, {{{variable}, {order}}}]"
    
    result = executor.execute(code)
    
    if result["success"]:
        return f"Derivative: {result['result']}"
    else:
        return f"Error: {result['error']}"

@mcp.tool()
def wolfram_simplify(expression: str) -> str:
    """
    Simplify a mathematical expression using Wolfram Language.
    
    Args:
        expression: Expression to simplify
        
    Example:
        expression="(x^2 - 1)/(x - 1)"
    """
    code = f"Simplify[{expression}]"
    result = executor.execute(code)
    
    if result["success"]:
        return f"Simplified: {result['result']}"
    else:
        return f"Error: {result['error']}"

@mcp.tool()
def wolfram_factor(expression: str) -> str:
    """
    Factor a mathematical expression using Wolfram Language.
    
    Args:
        expression: Expression to factor
        
    Example:
        expression="x^2 - 5x + 6"
    """
    code = f"Factor[{expression}]"
    result = executor.execute(code)
    
    if result["success"]:
        return f"Factored: {result['result']}"
    else:
        return f"Error: {result['error']}"

@mcp.tool()
def wolfram_expand(expression: str) -> str:
    """
    Expand a mathematical expression using Wolfram Language.
    
    Args:
        expression: Expression to expand
        
    Example:
        expression="(x + 1)^3"
    """
    code = f"Expand[{expression}]"
    result = executor.execute(code)
    
    if result["success"]:
        return f"Expanded: {result['result']}"
    else:
        return f"Error: {result['error']}"

@mcp.tool()
def wolfram_matrix_operations(operation: str, matrix_data: str) -> str:
    """
    Perform matrix operations using Wolfram Language.
    
    Args:
        operation: Operation to perform (Inverse, Determinant, Eigenvalues, Eigenvectors, etc.)
        matrix_data: Matrix in Wolfram Language format, e.g., "{{1,2},{3,4}}"
        
    Example:
        operation="Inverse", matrix_data="{{1,2},{3,4}}"
    """
    code = f"{operation}[{matrix_data}]"
    result = executor.execute(code)
    
    if result["success"]:
        return f"Result: {result['result']}"
    else:
        return f"Error: {result['error']}"

@mcp.tool()
def wolfram_statistics(operation: str, data: str) -> str:
    """
    Compute statistical measures using Wolfram Language.
    
    Args:
        operation: Statistical operation (Mean, Median, StandardDeviation, Variance, etc.)
        data: Data as list, e.g., "{1, 2, 3, 4, 5}"
        
    Example:
        operation="Mean", data="{1, 2, 3, 4, 5}"
    """
    code = f"{operation}[{data}]"
    result = executor.execute(code)
    
    if result["success"]:
        return f"{operation}: {result['result']}"
    else:
        return f"Error: {result['error']}"

@mcp.tool()
def wolfram_execute(code: str, timeout: int = 30) -> str:
    """
    Execute arbitrary Wolfram Language code.
    Use this for complex calculations or operations not covered by other tools.
    
    Args:
        code: Wolfram Language code to execute
        timeout: Execution timeout in seconds (default 30)
        
    Example:
        code="Table[Prime[n], {n, 1, 10}]"
    """
    result = executor.execute(code, timeout)
    
    if result["success"]:
        return f"Result: {result['result']}\n\nRaw output: {result['raw_output']}"
    else:
        error_msg = f"Error: {result['error']}"
        if result.get('stderr'):
            error_msg += f"\nStderr: {result['stderr']}"
        if result.get('stdout'):
            error_msg += f"\nStdout: {result['stdout']}"
        return error_msg

@mcp.tool()
def wolfram_test_connection() -> str:
    """
    Test the connection to Wolfram Language/Mathematica.
    Returns version information and confirms the system is working.
    """
    test_code = """
{
  "Version" -> $Version,
  "VersionNumber" -> $VersionNumber,
  "SystemID" -> $SystemID,
  "Test" -> 2 + 2
}
"""
    result = executor.execute(test_code)
    
    if result["success"]:
        return f"✓ Wolfram Language Connected\n\nResult: {result['result']}\n\nExecutable: {executor.executable}"
    else:
        return f"✗ Connection Failed\n\nError: {result.get('error', 'Unknown error')}\n\nExecutable: {executor.executable}\n\nPlease ensure Wolfram Language/Mathematica is properly installed and licensed."

if __name__ == "__main__":
    mcp.run()
