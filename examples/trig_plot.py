"""
Trigonometric Functions Visualization with Matplotlib

This script demonstrates the Wolfram MCP → Python workflow:
1. Compute data with Wolfram Language (or regenerate with numpy)
2. Create publication-quality plots with matplotlib
3. Export high-resolution images

Run: python3 trig_plot.py
Output: trig_functions.png (150 DPI)
"""

import matplotlib.pyplot as plt
import numpy as np

# Option 1: Use data from Wolfram Language
# (In practice, you would parse the Wolfram output)
# Option 2: Regenerate with numpy (shown here)

def generate_data():
    """Generate trigonometric function data"""
    x = np.linspace(0, 2*np.pi, 100)
    sin_x = np.sin(x)
    cos_x = np.cos(x)
    product = sin_x * cos_x
    return x, sin_x, cos_x, product

def create_plot():
    """Create a two-panel plot of trigonometric functions"""
    x, sin_x, cos_x, product = generate_data()
    
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    # Top plot: All three functions
    ax1.plot(x, sin_x, 'b-', linewidth=2, label='Sin(x)')
    ax1.plot(x, cos_x, 'g-', linewidth=2, label='Cos(x)')
    ax1.plot(x, product, 'm-', linewidth=2, label='Sin(x)·Cos(x)')
    ax1.axhline(y=0, color='k', linestyle='--', alpha=0.3)
    ax1.axvline(x=np.pi, color='k', linestyle='--', alpha=0.3, label='π')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('x (radians)', fontsize=12)
    ax1.set_ylabel('y', fontsize=12)
    ax1.set_title('Trigonometric Functions - Python Visualization', fontsize=14, fontweight='bold')
    ax1.legend(loc='upper right', fontsize=10)
    ax1.set_xlim(0, 2*np.pi)
    ax1.set_ylim(-1.1, 1.1)
    
    # Add π markers on x-axis
    pi_ticks = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    pi_labels = ['0', 'π/2', 'π', '3π/2', '2π']
    ax1.set_xticks(pi_ticks)
    ax1.set_xticklabels(pi_labels)
    
    # Bottom plot: Product function with shaded areas
    ax2.fill_between(x, 0, product, where=(product >= 0), 
                     color='purple', alpha=0.3, label='Positive region')
    ax2.fill_between(x, 0, product, where=(product < 0), 
                     color='orange', alpha=0.3, label='Negative region')
    ax2.plot(x, product, 'purple', linewidth=2)
    ax2.axhline(y=0, color='k', linestyle='-', alpha=0.5)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlabel('x (radians)', fontsize=12)
    ax2.set_ylabel('y', fontsize=12)
    ax2.set_title('Product Function: Sin(x)·Cos(x) = ½·Sin(2x)', fontsize=14, fontweight='bold')
    ax2.legend(loc='upper right', fontsize=10)
    ax2.set_xlim(0, 2*np.pi)
    ax2.set_xticks(pi_ticks)
    ax2.set_xticklabels(pi_labels)
    
    # Add annotation showing the identity
    ax2.annotate('Note: Sin(x)·Cos(x) = ½·Sin(2x)', 
                xy=(np.pi, 0), xytext=(np.pi, -0.3),
                fontsize=10, ha='center',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.3))
    
    plt.tight_layout()
    return fig

def main():
    """Main function to generate and save the plot"""
    print("Generating trigonometric functions plot...")
    
    fig = create_plot()
    
    # Save with high resolution
    output_file = 'trig_functions.png'
    fig.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"✓ Plot saved as: {output_file}")
    
    # Optionally, also save as PDF for publications
    pdf_file = 'trig_functions.pdf'
    fig.savefig(pdf_file, bbox_inches='tight')
    print(f"✓ PDF saved as: {pdf_file}")
    
    print("\nPlot characteristics:")
    print(f"  - Resolution: 150 DPI")
    print(f"  - Format: PNG, PDF")
    print(f"  - Data points: 100")
    print(f"  - Range: 0 to 2π")

if __name__ == "__main__":
    main()
