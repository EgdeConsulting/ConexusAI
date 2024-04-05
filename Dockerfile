
# Frontend - start
FROM node:18-alpine AS builder
WORKDIR /frontend
COPY /frontend/package*.json .
RUN npm install
COPY /frontend .
RUN npm run build
RUN npm prune --production

FROM node:18-alpine
WORKDIR /app
COPY --from=builder /frontend/build build/
COPY --from=builder /frontend/node_modules node_modules/
COPY /frontend/package.json .
EXPOSE 3000
# ENV NODE_ENV=production
CMD [ "node", "build" ]
# Frontend - end