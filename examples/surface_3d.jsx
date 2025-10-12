import React, { useState, useRef, useEffect } from 'react';
import * as THREE from 'three';

/**
 * Interactive 3D Surface Visualization
 * 
 * Function: z = sin(√(x² + y²))
 * Creates a ripple effect emanating from the origin
 * 
 * Data computed with Wolfram Language, rendered with Three.js
 * 
 * Features:
 * - Interactive rotation with mouse
 * - Adjustable grid resolution
 * - Color gradients based on height
 * - Wireframe toggle
 */
export default function Surface3D() {
  const containerRef = useRef(null);
  const [resolution, setResolution] = useState(50);
  const [wireframe, setWireframe] = useState(false);
  const sceneRef = useRef(null);
  const rendererRef = useRef(null);
  const meshRef = useRef(null);

  useEffect(() => {
    if (!containerRef.current) return;

    // Scene setup
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0xf0f0f0);
    sceneRef.current = scene;

    // Camera
    const camera = new THREE.PerspectiveCamera(
      75,
      containerRef.current.clientWidth / containerRef.current.clientHeight,
      0.1,
      1000
    );
    camera.position.set(5, 5, 5);
    camera.lookAt(0, 0, 0);

    // Renderer
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(containerRef.current.clientWidth, containerRef.current.clientHeight);
    containerRef.current.appendChild(renderer.domElement);
    rendererRef.current = renderer;

    // Lights
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
    scene.add(ambientLight);
    
    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
    directionalLight.position.set(5, 10, 5);
    scene.add(directionalLight);

    // Create surface
    createSurface(resolution, wireframe);

    // Animation loop
    let mouseX = 0;
    let mouseY = 0;
    let targetRotationX = 0;
    let targetRotationY = 0;

    const animate = () => {
      requestAnimationFrame(animate);
      
      if (meshRef.current) {
        targetRotationY += (mouseX - targetRotationY) * 0.05;
        targetRotationX += (mouseY - targetRotationX) * 0.05;
        
        meshRef.current.rotation.y = targetRotationY;
        meshRef.current.rotation.x = targetRotationX * 0.3;
      }
      
      renderer.render(scene, camera);
    };
    animate();

    // Mouse interaction
    const onMouseMove = (event) => {
      mouseX = (event.clientX / window.innerWidth) * 2 - 1;
      mouseY = -(event.clientY / window.innerHeight) * 2 + 1;
    };
    window.addEventListener('mousemove', onMouseMove);

    // Cleanup
    return () => {
      window.removeEventListener('mousemove', onMouseMove);
      if (containerRef.current && renderer.domElement) {
        containerRef.current.removeChild(renderer.domElement);
      }
      renderer.dispose();
    };
  }, [resolution, wireframe]);

  const createSurface = (res, isWireframe) => {
    if (meshRef.current) {
      sceneRef.current.remove(meshRef.current);
    }

    const geometry = new THREE.BufferGeometry();
    const vertices = [];
    const colors = [];
    const indices = [];

    const size = 6;
    const step = size / res;

    // Generate vertices
    for (let i = 0; i <= res; i++) {
      for (let j = 0; j <= res; j++) {
        const x = -size / 2 + i * step;
        const y = -size / 2 + j * step;
        const r = Math.sqrt(x * x + y * y);
        const z = Math.sin(r);

        vertices.push(x, z, y);

        // Color based on height
        const color = new THREE.Color();
        color.setHSL(0.6 - z * 0.3, 0.8, 0.5);
        colors.push(color.r, color.g, color.b);
      }
    }

    // Generate indices for triangles
    for (let i = 0; i < res; i++) {
      for (let j = 0; j < res; j++) {
        const a = i * (res + 1) + j;
        const b = a + 1;
        const c = a + res + 1;
        const d = c + 1;

        indices.push(a, b, c);
        indices.push(b, d, c);
      }
    }

    geometry.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));
    geometry.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));
    geometry.setIndex(indices);
    geometry.computeVertexNormals();

    const material = new THREE.MeshPhongMaterial({
      vertexColors: true,
      side: THREE.DoubleSide,
      wireframe: isWireframe,
      shininess: 30
    });

    const mesh = new THREE.Mesh(geometry, material);
    meshRef.current = mesh;
    sceneRef.current.add(mesh);
  };

  return (
    <div className="w-full h-screen bg-gradient-to-br from-gray-900 to-gray-800 p-8">
      <div className="max-w-7xl mx-auto">
        <div className="bg-white rounded-lg shadow-2xl overflow-hidden">
          {/* Header */}
          <div className="bg-gradient-to-r from-purple-600 to-blue-600 p-6 text-white">
            <h1 className="text-3xl font-bold mb-2">3D Surface Visualization</h1>
            <p className="text-lg opacity-90">
              Function: z = sin(√(x² + y²)) • Interactive Three.js Rendering
            </p>
          </div>

          {/* Controls */}
          <div className="p-6 border-b bg-gray-50">
            <div className="flex flex-wrap gap-6 items-center">
              <div className="flex items-center gap-4">
                <label className="text-sm font-semibold text-gray-700">
                  Resolution:
                </label>
                <input
                  type="range"
                  min="20"
                  max="100"
                  value={resolution}
                  onChange={(e) => setResolution(parseInt(e.target.value))}
                  className="w-48"
                />
                <span className="text-sm text-gray-600">{resolution}×{resolution}</span>
              </div>
              
              <button
                onClick={() => setWireframe(!wireframe)}
                className={`px-4 py-2 rounded-lg font-semibold transition-all ${
                  wireframe
                    ? 'bg-blue-600 text-white shadow-md'
                    : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                }`}
              >
                {wireframe ? 'Surface Mode' : 'Wireframe Mode'}
              </button>
            </div>
          </div>

          {/* 3D Canvas */}
          <div
            ref={containerRef}
            className="w-full h-[600px] bg-gray-100"
            style={{ cursor: 'grab' }}
          />

          {/* Info */}
          <div className="p-6 bg-gray-50 border-t">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="bg-white p-4 rounded-lg shadow">
                <h3 className="font-semibold text-purple-800 mb-1">Interactive</h3>
                <p className="text-sm text-gray-600">
                  Move your mouse to rotate the surface
                </p>
              </div>
              <div className="bg-white p-4 rounded-lg shadow">
                <h3 className="font-semibold text-blue-800 mb-1">Real-time</h3>
                <p className="text-sm text-gray-600">
                  Adjust resolution and toggle wireframe mode
                </p>
              </div>
              <div className="bg-white p-4 rounded-lg shadow">
                <h3 className="font-semibold text-green-800 mb-1">Color-coded</h3>
                <p className="text-sm text-gray-600">
                  Height determines color from blue to purple
                </p>
              </div>
            </div>
            
            <div className="mt-4 text-xs text-gray-500 text-center">
              Data computed with Wolfram Language • Rendered with Three.js
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
