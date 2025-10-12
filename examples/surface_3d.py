"""
3D Surface Plot Visualization
Function: z = sin(sqrt(x^2 + y^2)) - Ripple effect from origin

This script demonstrates creating 3D surface plots using matplotlib.
Data computed with Wolfram Language.

Run: python3 surface_3d.py
Output: surface_3d.png (150 DPI)
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def generate_surface_data():
    """
    Generate 3D surface data
    Can use Wolfram data or regenerate with numpy
    """
    x = np.linspace(-3, 3, 50)
    y = np.linspace(-3, 3, 50)
    X, Y = np.meshgrid(x, y)
    
    # Compute z = sin(sqrt(x^2 + y^2))
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    
    return X, Y, Z

def create_surface_plot():
    """Create 3D surface plot with multiple viewing angles"""
    X, Y, Z = generate_surface_data()
    
    fig = plt.figure(figsize=(15, 10))
    
    # Plot 1: Surface with colormap
    ax1 = fig.add_subplot(221, projection='3d')
    surf1 = ax1.plot_surface(X, Y, Z, cmap='viridis', 
                             linewidth=0, antialiased=True, alpha=0.9)
    ax1.set_xlabel('X', fontsize=10)
    ax1.set_ylabel('Y', fontsize=10)
    ax1.set_zlabel('Z', fontsize=10)
    ax1.set_title('Surface Plot: z = sin(√(x² + y²))', fontsize=12, fontweight='bold')
    ax1.view_init(elev=30, azim=45)
    fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)
    
    # Plot 2: Wireframe view
    ax2 = fig.add_subplot(222, projection='3d')
    ax2.plot_wireframe(X, Y, Z, color='blue', linewidth=0.5, alpha=0.6)
    ax2.set_xlabel('X', fontsize=10)
    ax2.set_ylabel('Y', fontsize=10)
    ax2.set_zlabel('Z', fontsize=10)
    ax2.set_title('Wireframe View', fontsize=12, fontweight='bold')
    ax2.view_init(elev=20, azim=135)
    
    # Plot 3: Contour plot
    ax3 = fig.add_subplot(223)
    contour = ax3.contourf(X, Y, Z, levels=20, cmap='viridis')
    ax3.contour(X, Y, Z, levels=20, colors='black', linewidths=0.5, alpha=0.3)
    ax3.set_xlabel('X', fontsize=10)
    ax3.set_ylabel('Y', fontsize=10)
    ax3.set_title('Contour Plot (Top View)', fontsize=12, fontweight='bold')
    ax3.set_aspect('equal')
    fig.colorbar(contour, ax=ax3, shrink=0.8)
    
    # Plot 4: Different angle with projection
    ax4 = fig.add_subplot(224, projection='3d')
    surf4 = ax4.plot_surface(X, Y, Z, cmap='coolwarm', 
                             linewidth=0, antialiased=True, alpha=0.8)
    ax4.set_xlabel('X', fontsize=10)
    ax4.set_ylabel('Y', fontsize=10)
    ax4.set_zlabel('Z', fontsize=10)
    ax4.set_title('Alternative View (Top-Down)', fontsize=12, fontweight='bold')
    ax4.view_init(elev=60, azim=0)
    fig.colorbar(surf4, ax=ax4, shrink=0.5, aspect=5)
    
    plt.tight_layout()
    return fig

def main():
    """Main function to generate and save the 3D surface plot"""
    print("Generating 3D surface plot...")
    
    fig = create_surface_plot()
    
    # Save with high resolution
    output_file = 'surface_3d.png'
    fig.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"✓ Plot saved as: {output_file}")
    
    print("\nPlot features:")
    print("  - Function: z = sin(√(x² + y²))")
    print("  - 4 different visualizations")
    print("  - Surface, wireframe, and contour views")
    print("  - Multiple viewing angles")
    print("  - Resolution: 150 DPI")

if __name__ == "__main__":
    main()
