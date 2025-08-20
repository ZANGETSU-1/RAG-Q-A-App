/**
 * Monkey Registry App - JavaScript Skeleton
 *
 * This is a starting point for your Monkey Registry application.
 * Replace the TODO comments with your actual implementation.
 */

// TODO: Import required dependencies
// const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
// const { DynamoDBDocumentClient } = require('@aws-sdk/lib-dynamodb');

// TODO: Configure AWS DynamoDB client
// const client = new DynamoDBClient({ region: 'eu-west-1' });
// const docClient = DynamoDBDocumentClient.from(client);

// Monkey data model
class Monkey {
  constructor(name, species, ageYears, favouriteFruit, lastCheckupAt = null) {
    this.monkey_id = this.generateId();
    this.name = name;
    this.species = species;
    this.age_years = ageYears;
    this.favourite_fruit = favouriteFruit;
    this.last_checkup_at = lastCheckupAt;
    this.created_at = new Date().toISOString();
    this.updated_at = new Date().toISOString();
  }

  generateId() {
    // TODO: Implement UUID generation
    return (
      "monkey_" + Date.now() + "_" + Math.random().toString(36).substr(2, 9)
    );
  }

  validate() {
    // TODO: Implement validation rules
    // - Name required, 2-40 chars
    // - Age 0-45
    // - Species must be valid enum
    // - Marmoset age cap at 22
    return true;
  }
}

// Valid species enum
const VALID_SPECIES = ["capuchin", "macaque", "marmoset", "howler"];

// Monkey Registry class
class MonkeyRegistry {
  constructor() {
    this.monkeys = new Map(); // TODO: Replace with actual database
  }

  // TODO: Implement CRUD operations

  async createMonkey(monkeyData) {
    // TODO: Implement create operation
    // - Validate monkey data
    // - Check for duplicates within species
    // - Save to database
    // - Return created monkey
    throw new Error("Create operation not implemented");
  }

  async getMonkey(monkeyId) {
    // TODO: Implement read operation
    // - Retrieve monkey by ID from database
    // - Return monkey or null if not found
    throw new Error("Read operation not implemented");
  }

  async updateMonkey(monkeyId, updates) {
    // TODO: Implement update operation
    // - Validate updates
    // - Update in database
    // - Return updated monkey
    throw new Error("Update operation not implemented");
  }

  async deleteMonkey(monkeyId) {
    // TODO: Implement delete operation
    // - Remove monkey from database
    // - Return success status
    throw new Error("Delete operation not implemented");
  }

  async listMonkeys(filters = {}) {
    // TODO: Implement list operation
    // - Support filtering by species, name
    // - Implement pagination
    // - Return filtered results
    throw new Error("List operation not implemented");
  }

  async searchMonkeys(query) {
    // TODO: Implement search operation
    // - Search by name or species
    // - Return matching results
    throw new Error("Search operation not implemented");
  }
}

// TODO: Implement CLI interface or web server
class MonkeyRegistryCLI {
  constructor() {
    this.registry = new MonkeyRegistry();
  }

  async start() {
    // TODO: Implement CLI menu
    console.log("🐒 Monkey Registry CLI");
    console.log("Commands: create, read, update, delete, list, search, quit");

    // TODO: Add interactive CLI logic
    // - Read user input
    // - Parse commands
    // - Execute operations
    // - Display results
  }
}

// TODO: Add your AI prompts and process documentation here
const AI_PROMPTS = {
  // TODO: Document your AI prompts
  // Example:
  // "project_bootstrap": "I need to build a Monkey Registry app with CRUD operations...",
  // "implement_function": "Help me implement the createMonkey function...",
  // "testing_debugging": "Generate tests for the Monkey validation logic..."
};

// TODO: Add your process report
const PROCESS_REPORT = {
  // TODO: Document your development process
  // - Initial spec
  // - AI tool usage
  // - Key decisions
  // - Blockers and solutions
};

// Export for use in other files
module.exports = {
  Monkey,
  MonkeyRegistry,
  MonkeyRegistryCLI,
  VALID_SPECIES,
  AI_PROMPTS,
  PROCESS_REPORT,
};

// Start CLI if running directly
if (require.main === module) {
  const cli = new MonkeyRegistryCLI();
  cli.start().catch(console.error);
}
