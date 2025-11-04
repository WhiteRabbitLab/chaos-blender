#!/bin/bash

# Chaos Blender - Docker Quick Start Script
# This script starts the PostgreSQL database using Docker

set -e

echo "🎮 Chaos Blender - Docker Setup"
echo "================================"
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker Desktop first:"
    echo "   https://www.docker.com/products/docker-desktop"
    exit 1
fi

# Check if Docker is running
if ! docker info &> /dev/null; then
    echo "❌ Docker is not running. Please start Docker Desktop."
    exit 1
fi

echo "✅ Docker is installed and running"
echo ""

# Start PostgreSQL
echo "🚀 Starting PostgreSQL database..."
docker-compose -f docker-compose.db-only.yml up -d

echo ""
echo "⏳ Waiting for database to be ready..."
sleep 3

# Check if database is ready
if docker-compose -f docker-compose.db-only.yml exec -T postgres pg_isready -U chaos_user > /dev/null 2>&1; then
    echo "✅ Database is ready!"
else
    echo "⚠️  Database is starting up. It may take a few more seconds."
fi

echo ""
echo "📊 Database Information:"
echo "   Host: localhost"
echo "   Port: 5432"
echo "   Database: chaos_blender"
echo "   Username: chaos_user"
echo "   Password: chaos_password"
echo ""
echo "📝 Connection String:"
echo "   postgresql://chaos_user:chaos_password@localhost:5432/chaos_blender"
echo ""
echo "✨ Next steps:"
echo "   1. Set up the backend:"
echo "      cd server"
echo "      python -m venv venv"
echo "      source venv/bin/activate"
echo "      pip install -r requirements.txt"
echo "      cp .env.example .env"
echo "      cd src && python init_data.py"
echo ""
echo "   2. Set up the frontend:"
echo "      cd client"
echo "      npm install"
echo ""
echo "   3. Start the servers:"
echo "      Terminal 1: cd server/src && python main.py"
echo "      Terminal 2: cd client && npm start"
echo ""
echo "🛑 To stop the database:"
echo "   docker-compose -f docker-compose.db-only.yml down"
echo ""
echo "Happy blending! 🎮"
