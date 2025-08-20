"""
Monkey Registry App - Python Skeleton

This is a starting point for your Monkey Registry application.
Replace the TODO comments with your actual implementation.
"""

import uuid
from datetime import datetime
from typing import Optional, List, Dict, Any
from enum import Enum

# TODO: Import required dependencies
# import boto3
# from boto3.dynamodb.conditions import Key, Attr

class Species(Enum):
    """Valid monkey species"""
    CAPUCHIN = "capuchin"
    MACAQUE = "macaque"
    MARMOSET = "marmoset"
    HOWLER = "howler"

class Monkey:
    """Monkey data model"""

    def __init__(self, name: str, species: str, age_years: int,
                 favourite_fruit: str, last_checkup_at: Optional[str] = None):
        self.monkey_id = self.generate_id()
        self.name = name
        self.species = species
        self.age_years = age_years
        self.favourite_fruit = favourite_fruit
        self.last_checkup_at = last_checkup_at
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def generate_id(self) -> str:
        """Generate unique monkey ID"""
        # TODO: Implement UUID generation
        return f"monkey_{uuid.uuid4().hex[:8]}"

    def validate(self) -> bool:
        """Validate monkey data according to business rules"""
        # TODO: Implement validation rules
        # - Name required, 2-40 chars
        # - Age 0-45
        # - Species must be valid enum
        # - Marmoset age cap at 22
        # - No duplicates within same species
        return True

    def to_dict(self) -> Dict[str, Any]:
        """Convert monkey to dictionary for storage"""
        return {
            'monkey_id': self.monkey_id,
            'name': self.name,
            'species': self.species,
            'age_years': self.age_years,
            'favourite_fruit': self.favourite_fruit,
            'last_checkup_at': self.last_checkup_at,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

class MonkeyRegistry:
    """Main registry class for managing monkeys"""

    def __init__(self):
        # TODO: Initialize database connection
        # self.dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
        # self.table = self.dynamodb.Table('monkey-registry')
        self.monkeys = {}  # TODO: Replace with actual database

    async def create_monkey(self, monkey_data: Dict[str, Any]) -> Monkey:
        """Create a new monkey"""
        # TODO: Implement create operation
        # - Validate monkey data
        # - Check for duplicates within species
        # - Save to database
        # - Return created monkey
        raise NotImplementedError("Create operation not implemented")

    async def get_monkey(self, monkey_id: str) -> Optional[Monkey]:
        """Retrieve monkey by ID"""
        # TODO: Implement read operation
        # - Retrieve monkey by ID from database
        # - Return monkey or None if not found
        raise NotImplementedError("Read operation not implemented")

    async def update_monkey(self, monkey_id: str, updates: Dict[str, Any]) -> Optional[Monkey]:
        """Update existing monkey"""
        # TODO: Implement update operation
        # - Validate updates
        # - Update in database
        # - Return updated monkey
        raise NotImplementedError("Update operation not implemented")

    async def delete_monkey(self, monkey_id: str) -> bool:
        """Delete monkey by ID"""
        # TODO: Implement delete operation
        # - Remove monkey from database
        # - Return success status
        raise NotImplementedError("Delete operation not implemented")

    async def list_monkeys(self, filters: Optional[Dict[str, Any]] = None) -> List[Monkey]:
        """List monkeys with optional filtering"""
        # TODO: Implement list operation
        # - Support filtering by species, name
        # - Implement pagination
        # - Return filtered results
        raise NotImplementedError("List operation not implemented")

    async def search_monkeys(self, query: str) -> List[Monkey]:
        """Search monkeys by name or species"""
        # TODO: Implement search operation
        # - Search by name or species
        # - Return matching results
        raise NotImplementedError("Search operation not implemented")

class MonkeyRegistryCLI:
    """Command-line interface for the monkey registry"""

    def __init__(self):
        self.registry = MonkeyRegistry()

    async def start(self):
        """Start the CLI interface"""
        # TODO: Implement CLI menu
        print("🐒 Monkey Registry CLI")
        print("Commands: create, read, update, delete, list, search, quit")

        # TODO: Add interactive CLI logic
        # - Read user input
        # - Parse commands
        # - Execute operations
        # - Display results

# TODO: Add your AI prompts and process documentation here
AI_PROMPTS = {
    # TODO: Document your AI prompts
    # Example:
    # "project_bootstrap": "I need to build a Monkey Registry app with CRUD operations...",
    # "implement_function": "Help me implement the create_monkey function...",
    # "testing_debugging": "Generate tests for the Monkey validation logic..."
}

# TODO: Add your process report
PROCESS_REPORT = {
    # TODO: Document your development process
    # - Initial spec
    # - AI tool usage
    # - Key decisions
    # - Blockers and solutions
}

def main():
    """Main entry point"""
    # TODO: Implement main application logic
    cli = MonkeyRegistryCLI()
    # asyncio.run(cli.start())  # Uncomment when async is implemented

if __name__ == "__main__":
    main()
