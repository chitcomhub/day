# Use a Node.js image
FROM node:20

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json (or yarn.lock)
COPY package*.json ./
# COPY yarn.lock ./

# Install dependencies
RUN npm install

# Copy the rest of the codebase into the app directory
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Serve the app using Vite's preview command, which serves the production build
# CMD ["npm", "run", "preview", "--", "--host", "--port", "3000"]
CMD ["npm", "run", "dev"]
