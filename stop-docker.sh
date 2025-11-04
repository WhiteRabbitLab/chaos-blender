#!/bin/bash

# Chaos Blender - Stop Docker Services
# This script stops the PostgreSQL database and optionally removes volumes

set -e

echo "🛑 Stopping Chaos Blender Docker Services"
echo "=========================================="
echo ""

# Check which compose file to use
if [ "$1" == "--full" ]; then
    COMPOSE_FILE="docker-compose.yml"
    echo "Stopping full stack (database + backend + frontend)..."
elif [ "$1" == "--remove-data" ]; then
    COMPOSE_FILE="docker-compose.db-only.yml"
    echo "Stopping database and removing data volumes..."
    docker-compose -f $COMPOSE_FILE down -v
    echo "✅ Database stopped and data removed"
    exit 0
else
    COMPOSE_FILE="docker-compose.db-only.yml"
    echo "Stopping database..."
fi

# Stop services
docker-compose -f $COMPOSE_FILE down

echo "✅ Services stopped"
echo ""
echo "💾 Database data has been preserved"
echo ""
echo "🔄 To start again:"
echo "   ./start-docker.sh"
echo ""
echo "🗑️  To remove data volumes:"
echo "   ./stop-docker.sh --remove-data"
