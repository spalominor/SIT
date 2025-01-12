/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',  // Escanea todos los templates en la carpeta global
    './**/templates/**/*.html',  // Escanea templates dentro de cada app
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

