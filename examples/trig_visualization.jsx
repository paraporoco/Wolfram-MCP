import React, { useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

// Data generated from Wolfram Language using:
// Table[{x, Sin[x], Cos[x], Sin[x]*Cos[x]}, {x, 0, 2*Pi, 0.2}]
const wolframData = [
  {x: 0.0, sin: 0.0, cos: 1.0, product: 0.0},
  {x: 0.2, sin: 0.199, cos: 0.980, product: 0.195},
  {x: 0.4, sin: 0.389, cos: 0.921, product: 0.359},
  {x: 0.6, sin: 0.565, cos: 0.825, product: 0.466},
  {x: 0.8, sin: 0.717, cos: 0.697, product: 0.500},
  {x: 1.0, sin: 0.841, cos: 0.540, product: 0.455},
  {x: 1.2, sin: 0.932, cos: 0.362, product: 0.338},
  {x: 1.4, sin: 0.985, cos: 0.170, product: 0.167},
  {x: 1.6, sin: 1.000, cos: -0.029, product: -0.029},
  {x: 1.8, sin: 0.974, cos: -0.227, product: -0.221},
  {x: 2.0, sin: 0.909, cos: -0.416, product: -0.378},
  {x: 2.2, sin: 0.808, cos: -0.589, product: -0.476},
  {x: 2.4, sin: 0.675, cos: -0.737, product: -0.498},
  {x: 2.6, sin: 0.516, cos: -0.857, product: -0.442},
  {x: 2.8, sin: 0.335, cos: -0.942, product: -0.316},
  {x: 3.0, sin: 0.141, cos: -0.990, product: -0.140},
  {x: 3.2, sin: -0.058, cos: -0.998, product: 0.058},
  {x: 3.4, sin: -0.256, cos: -0.967, product: 0.247},
  {x: 3.6, sin: -0.443, cos: -0.897, product: 0.397},
  {x: 3.8, sin: -0.612, cos: -0.791, product: 0.484},
  {x: 4.0, sin: -0.757, cos: -0.654, product: 0.495},
  {x: 4.2, sin: -0.872, cos: -0.490, product: 0.427},
  {x: 4.4, sin: -0.952, cos: -0.307, product: 0.292},
  {x: 4.6, sin: -0.994, cos: -0.112, product: 0.111},
  {x: 4.8, sin: -0.996, cos: 0.087, product: -0.087},
  {x: 5.0, sin: -0.959, cos: 0.284, product: -0.272},
  {x: 5.2, sin: -0.883, cos: 0.469, product: -0.414},
  {x: 5.4, sin: -0.773, cos: 0.635, product: -0.490},
  {x: 5.6, sin: -0.631, cos: 0.776, product: -0.490},
  {x: 5.8, sin: -0.465, cos: 0.886, product: -0.411},
  {x: 6.0, sin: -0.279, cos: 0.960, product: -0.268},
  {x: 6.2, sin: -0.083, cos: 0.997, product: -0.083}
];

/**
 * Interactive Trigonometric Functions Visualization
 * 
 * This component demonstrates the Wolfram MCP → React workflow:
 * 1. Compute data with Wolfram Language
 * 2. Format data for JavaScript
 * 3. Create interactive visualization with Recharts
 * 
 * Features:
 * - Toggle visibility of different functions
 * - Interactive tooltips
 * - Responsive design
 * - Smooth animations
 */
export default function TrigVisualization() {
  const [visibleLines, setVisibleLines] = useState({
    sin: true,
    cos: true,
    product: true
  });

  const toggleLine = (line) => {
    setVisibleLines(prev => ({...prev, [line]: !prev[line]}));
  };

  return (
    <div className="w-full h-screen bg-gradient-to-br from-slate-900 to-slate-800 p-8">
      <div className="max-w-6xl mx-auto">
        <div className="bg-white rounded-lg shadow-2xl p-6">
          <h1 className="text-3xl font-bold text-slate-800 mb-2">
            Trigonometric Functions Visualization
          </h1>
          <p className="text-slate-600 mb-6">
            Data computed using Wolfram Language • Interactive chart powered by Recharts
          </p>
          
          {/* Toggle Controls */}
          <div className="flex gap-4 mb-6">
            <button
              onClick={() => toggleLine('sin')}
              className={`px-4 py-2 rounded-lg font-semibold transition-all ${
                visibleLines.sin 
                  ? 'bg-blue-500 text-white shadow-md' 
                  : 'bg-gray-200 text-gray-500'
              }`}
            >
              Sin(x)
            </button>
            <button
              onClick={() => toggleLine('cos')}
              className={`px-4 py-2 rounded-lg font-semibold transition-all ${
                visibleLines.cos 
                  ? 'bg-green-500 text-white shadow-md' 
                  : 'bg-gray-200 text-gray-500'
              }`}
            >
              Cos(x)
            </button>
            <button
              onClick={() => toggleLine('product')}
              className={`px-4 py-2 rounded-lg font-semibold transition-all ${
                visibleLines.product 
                  ? 'bg-purple-500 text-white shadow-md' 
                  : 'bg-gray-200 text-gray-500'
              }`}
            >
              Sin(x)·Cos(x)
            </button>
          </div>

          {/* Chart */}
          <ResponsiveContainer width="100%" height={400}>
            <LineChart data={wolframData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
              <XAxis 
                dataKey="x" 
                label={{ value: 'x (radians)', position: 'insideBottom', offset: -5 }}
                stroke="#475569"
              />
              <YAxis 
                label={{ value: 'y', angle: -90, position: 'insideLeft' }}
                stroke="#475569"
              />
              <Tooltip 
                contentStyle={{ 
                  backgroundColor: 'rgba(255, 255, 255, 0.95)', 
                  border: '1px solid #cbd5e1',
                  borderRadius: '8px'
                }}
                formatter={(value) => value.toFixed(3)}
              />
              <Legend />
              
              {visibleLines.sin && (
                <Line 
                  type="monotone" 
                  dataKey="sin" 
                  stroke="#3b82f6" 
                  strokeWidth={2}
                  dot={false}
                  name="Sin(x)"
                  animationDuration={1000}
                />
              )}
              
              {visibleLines.cos && (
                <Line 
                  type="monotone" 
                  dataKey="cos" 
                  stroke="#10b981" 
                  strokeWidth={2}
                  dot={false}
                  name="Cos(x)"
                  animationDuration={1000}
                />
              )}
              
              {visibleLines.product && (
                <Line 
                  type="monotone" 
                  dataKey="product" 
                  stroke="#a855f7" 
                  strokeWidth={2}
                  dot={false}
                  name="Sin(x)·Cos(x)"
                  animationDuration={1000}
                />
              )}
            </LineChart>
          </ResponsiveContainer>

          {/* Info Panel */}
          <div className="mt-6 grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="bg-blue-50 p-4 rounded-lg border border-blue-200">
              <h3 className="font-semibold text-blue-800 mb-1">Sin(x)</h3>
              <p className="text-sm text-blue-600">Classic sine wave oscillating between -1 and 1</p>
            </div>
            <div className="bg-green-50 p-4 rounded-lg border border-green-200">
              <h3 className="font-semibold text-green-800 mb-1">Cos(x)</h3>
              <p className="text-sm text-green-600">Cosine wave, phase-shifted 90° from sine</p>
            </div>
            <div className="bg-purple-50 p-4 rounded-lg border border-purple-200">
              <h3 className="font-semibold text-purple-800 mb-1">Sin(x)·Cos(x)</h3>
              <p className="text-sm text-purple-600">Product equals ½·sin(2x), double frequency</p>
            </div>
          </div>

          <div className="mt-4 text-xs text-gray-500 text-center">
            32 data points computed from x = 0 to 2π (≈ 6.28 radians)
          </div>
        </div>
      </div>
    </div>
  );
}
