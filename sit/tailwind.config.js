/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',  // Escanea todos los templates en la carpeta global
    './**/templates/**/*.html',  // Escanea templates dentro de cada app
  ],
  darkMode: 'class',  // Habilita el modo oscuro utilizando la clase "dark"
  theme: {
    extend: {
      colors: {
        primary: {
          "50": "#f9fafb",
          "100": "#f3f4f6",
          "200": "#e5e7eb",
          "300": "#d1d5db",
          "400": "#9ca3af",
          "500": "#6b7280",
          "600": "#4b5563",
          "700": "#374151",
          "800": "#1f2937",
          "900": "#111827",
        },
        secondary: {
          "50": "#f5e6ff", // Lila claro
          "100": "#e0b3ff",
          "200": "#d07aff",
          "300": "#b84dff",
          "400": "#9f1eff",
          "500": "#8c00e6", // Morado
          "600": "#7a00cc",
          "700": "#6600b3",
          "800": "#520099",
          "900": "#3f0066",
        },
      },
      fontFamily: {
        body: [
          'Inter', 
          'ui-sans-serif', 
          'system-ui', 
          '-apple-system', 
          'system-ui', 
          'Segoe UI', 
          'Roboto', 
          'Helvetica Neue', 
          'Arial', 
          'Noto Sans', 
          'sans-serif', 
          'Apple Color Emoji', 
          'Segoe UI Emoji', 
          'Segoe UI Symbol', 
          'Noto Color Emoji'
        ],
        sans: [
          'Inter', 
          'ui-sans-serif', 
          'system-ui', 
          '-apple-system', 
          'system-ui', 
          'Segoe UI', 
          'Roboto', 
          'Helvetica Neue', 
          'Arial', 
          'Noto Sans', 
          'sans-serif', 
          'Apple Color Emoji', 
          'Segoe UI Emoji', 
          'Segoe UI Symbol', 
          'Noto Color Emoji'
        ],
      },
    },
  },
  plugins: [],
};
