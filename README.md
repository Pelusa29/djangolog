<p align="center">
    <img width="350" src="IMG/gitCracken.png">
</p>
<div align="center">
<img alt="Static Badge" src="https://img.shields.io/badge/Reactjs-v18.3.1-blue?style=flat-square&logo=React&logoColor=blue&color=%23fffffff">

<img alt="Static Badge" src="https://img.shields.io/badge/Docker-v?style=plastic&logo=Docker&logoColor=blue&color=%23ffffff">
<img alt="Static Badge" src="https://img.shields.io/badge/Github-black?style=flat-square&logo=Github&logoColor=blue&color=%23dddd">
</div>

# Task system

Este repositorio contiene el código para una aplicación de gestión de libros desarrollada con React/Next.js. La aplicación incluye funcionalidades de autenticación, operaciones CRUD, manejo de archivos, estado global, y más.

## Tabla de Contenidos

- [Task system](#task-system)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Configuración Inicial](#configuración-inicial)
  - [Diseño de la Interfaz de Usuario](#diseño-de-la-interfaz-de-usuario)
  - [Autenticación](#autenticación)
  - [Operaciones CRUD](#operaciones-crud)
  - [Manejo de Archivos](#manejo-de-archivos)
  - [Estado Global](#estado-global)
  - [Seguridad](#seguridad)
  - [Instalación y Configuración (Front End)](#instalación-y-configuración-front-end)
  - [Instalación y Configuración (Back End)](#instalación-y-configuración-back-end)


## Configuración Inicial

- Front End: React Js con la librería Tailwind CSS aplicando un package llamado Flowbite React js.
- Para el Back end se usó Node js usando el Framework Express.js
- Para la Base de datos se usó Mongo DB.

## Diseño de la Interfaz de Usuario

- Se genero una pequeña interfaz base para visualizar el contenido usando algunos componenetes de Tailwind y Flowbite.
- Se implementaron componentes reutilizables para listar los libros.

## Autenticación

- Autenticación basada en JWT Server Side y manejo de sessiones con cookie-parse y cors.

## Operaciones CRUD

- Se implementó una vista para listar y Buscar.

## Manejo de Archivos

- Se implemento Cloudinary para el manejo de Archivos por medio de Filestack.

## Estado Global

- Se imlpemento un estdo Global  (Context API) para el manejo de las sesiones y accesos asi como para mantener la información de búsqueda con useState.


## Seguridad


- Se implemento JWT para las peticiones del FrontEnd hacia el backend usando Axios y en el Back end se usó middlewares de verificación de datos.
 
----------------------------------------------------------------

## Instalación y Configuración (Front End)
1 .- Clonar el proyecto: https://github.com/Pelusa29/reactjs-contextapi
2 .- Acceder al folder client
3 .- Ejecutar npm i
4 .- Ejecutar npm run dev


## Instalación y Configuración (Back End)

1. Clonar el repositorio y navegar al directorio del backend:
   ```bash
   `Dockerfile` para el Backend.

   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_DIRECTORIO_BACKEND>
   docker-compose up --build



