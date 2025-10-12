"""
Statistical Distributions Visualization
Demonstrates multiple statistical distributions and their properties

Data can be generated with Wolfram Language or Python's numpy
Visualizations include histograms, PDF/CDF curves, and box plots

Run: python3 statistical_distributions.py
Output: statistical_distributions.png (150 DPI)
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def generate_distributions():
    """Generate data from multiple statistical distributions"""
    np.random.seed(42)
    
    distributions = {
        'Normal': np.random.normal(0, 1, 1000),
        'Uniform': np.random.uniform(-3, 3, 1000),
        'Exponential': np.random.exponential(1, 1000),
        'Chi-Square': np.random.chisquare(3, 1000)
    }
    
    return distributions

def create_statistical_plots():
    """Create comprehensive statistical visualization"""
    distributions = generate_distributions()
    
    fig = plt.figure(figsize=(16, 10))
    
    # Plot 1: Overlaid histograms
    ax1 = fig.add_subplot(2, 3, 1)
    for name, data in distributions.items():
        ax1.hist(data, bins=50, alpha=0.5, label=name, density=True)
    ax1.set_xlabel('Value', fontsize=10)
    ax1.set_ylabel('Density', fontsize=10)
    ax1.set_title('Distribution Comparison - Histograms', fontsize=12, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Normal distribution details
    ax2 = fig.add_subplot(2, 3, 2)
    normal_data = distributions['Normal']
    counts, bins, patches = ax2.hist(normal_data, bins=50, density=True, 
                                      alpha=0.7, color='blue', edgecolor='black')
    
    # Overlay theoretical PDF
    x = np.linspace(normal_data.min(), normal_data.max(), 100)
    pdf = stats.norm.pdf(x, np.mean(normal_data), np.std(normal_data))
    ax2.plot(x, pdf, 'r-', linewidth=2, label='Theoretical PDF')
    
    ax2.set_xlabel('Value', fontsize=10)
    ax2.set_ylabel('Density', fontsize=10)
    ax2.set_title(f'Normal Distribution (μ={np.mean(normal_data):.2f}, σ={np.std(normal_data):.2f})', 
                 fontsize=12, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Plot 3: Box plots
    ax3 = fig.add_subplot(2, 3, 3)
    data_list = [distributions[name] for name in distributions.keys()]
    bp = ax3.boxplot(data_list, labels=list(distributions.keys()), patch_artist=True)
    
    colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
    
    ax3.set_ylabel('Value', fontsize=10)
    ax3.set_title('Box Plot Comparison', fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Plot 4: Q-Q plot for Normal distribution
    ax4 = fig.add_subplot(2, 3, 4)
    stats.probplot(normal_data, dist="norm", plot=ax4)
    ax4.set_title('Q-Q Plot: Normal Distribution', fontsize=12, fontweight='bold')
    ax4.grid(True, alpha=0.3)
    
    # Plot 5: Cumulative Distribution Functions
    ax5 = fig.add_subplot(2, 3, 5)
    for name, data in distributions.items():
        sorted_data = np.sort(data)
        cumulative = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
        ax5.plot(sorted_data, cumulative, label=name, linewidth=2)
    
    ax5.set_xlabel('Value', fontsize=10)
    ax5.set_ylabel('Cumulative Probability', fontsize=10)
    ax5.set_title('Cumulative Distribution Functions', fontsize=12, fontweight='bold')
    ax5.legend()
    ax5.grid(True, alpha=0.3)
    
    # Plot 6: Statistical summary
    ax6 = fig.add_subplot(2, 3, 6)
    ax6.axis('off')
    
    summary_text = "Statistical Summary\n" + "="*40 + "\n\n"
    for name, data in distributions.items():
        summary_text += f"{name} Distribution:\n"
        summary_text += f"  Mean: {np.mean(data):8.3f}\n"
        summary_text += f"  Std:  {np.std(data):8.3f}\n"
        summary_text += f"  Min:  {np.min(data):8.3f}\n"
        summary_text += f"  Max:  {np.max(data):8.3f}\n"
        summary_text += f"  Median: {np.median(data):6.3f}\n\n"
    
    ax6.text(0.1, 0.9, summary_text, fontsize=10, family='monospace',
             verticalalignment='top', bbox=dict(boxstyle='round', 
             facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    return fig

def main():
    """Main function to generate and save statistical plots"""
    print("Generating statistical distributions visualization...")
    
    fig = create_statistical_plots()
    
    # Save with high resolution
    output_file = 'statistical_distributions.png'
    fig.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"✓ Plot saved as: {output_file}")
    
    print("\nIncluded distributions:")
    print("  - Normal (Gaussian)")
    print("  - Uniform")
    print("  - Exponential")
    print("  - Chi-Square")
    print("\nVisualization types:")
    print("  - Histograms")
    print("  - Probability Density Functions")
    print("  - Box Plots")
    print("  - Q-Q Plot")
    print("  - Cumulative Distribution Functions")
    print("  - Statistical Summary")

if __name__ == "__main__":
    main()
