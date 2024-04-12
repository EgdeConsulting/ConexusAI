# syntax=docker/dockerfile:1
# Backend - start


# Velg et Python basebilde som matcher versjonen du bruker
FROM python:3.12-slim

# Sett miljøvariabler for Python til å kjøre i en Docker container
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Sett arbeidskatalogen til /app i containeren
WORKDIR /app

# Installer eventuelle systemavhengigheter her
# F.eks.: RUN apt-get update && apt-get install -y <pakkenavn>

# Kopier requirements.txt og installer Python avhengigheter
COPY ./backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopier resten av applikasjonen til arbeidskatalogen
COPY ./backend .

# Eksponer porten applikasjonen lytter på
EXPOSE 5000

# Definer kommandoen for å kjøre applikasjonen
# For Flask's innebygde server (for utvikling)
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

# For produksjon med Gunicorn
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
# Backend - end

# # Frontend - start
# FROM node:18-alpine AS builder
# WORKDIR /frontend
# COPY /frontend/package*.json .
# RUN npm install
# COPY /frontend .
# RUN npm run build
# RUN npm prune --production

# FROM node:18-alpine
# WORKDIR /app
# COPY --from=builder /frontend/build build/
# COPY --from=builder /frontend/node_modules node_modules/
# COPY /frontend/package.json .
# # Frontend - end


# EXPOSE 3000
# # ENV NODE_ENV=production
# CMD [ "node", "build" ]
