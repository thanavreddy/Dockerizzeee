# Flask Hello App (Dockerized)

This is a simple Flask web application that returns a greeting message. The app is containerized using Docker and can be run locally without installing Python or Flask on your system.

---

##  Features

- Built with Python Flask
- Dockerized for easy setup and deployment
- Auto-reloads with `debug=True`

---

##  Project Structure

.
├── app.py # Main Flask app
├── Dockerfile # Docker configuration file
└── README.md # You're here!



##  Run with Docker

###  Step 1: Make sure Docker is installed

Install Docker from [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

> Or use GitHub Codespaces / Gitpod if you don't want to install Docker locally.

---

### Step 2: Build the Docker image
docker build -t flask-cosc-app .

### Step 3: Run the container
docker run -p 5000:5000 flask-cosc-app
###  Step 4: Open in browser
Go to:
http://localhost:5000
You should see:
Hello from COSC!
