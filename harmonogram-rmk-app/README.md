# Harmonogram RMK App

## Overview
The Harmonogram RMK App is a web application designed to manage and display RMK (Rejestr Miesięcznych Kont) entries. It allows users to add accounts with descriptions, view schedules, and generate reports based on RMK data.

## Features
- **Account Management**: Add accounts with detailed descriptions.
- **Schedule Display**: View schedules of RMK entries categorized by month and category.
- **Reporting**: Generate reports that summarize RMK data by month, category, or custom periods.

## Project Structure
```
harmonogram-rmk-app
├── src
│   ├── main.ts                  # Entry point of the application
│   ├── models
│   │   ├── account.ts           # Defines the Account model
│   │   ├── rmk.ts               # Defines the RMK model
│   │   └── index.ts             # Exports models for use in the application
│   ├── controllers
│   │   ├── dictionaryController.ts # Handles dictionary-related requests
│   │   ├── harmonogramController.ts # Manages schedule display and RMK aggregation
│   │   └── reportsController.ts  # Generates reports based on RMK data
│   ├── services
│   │   ├── dictionaryService.ts  # Business logic for managing dictionary entries
│   │   ├── harmonogramService.ts  # Logic for generating schedules
│   │   └── reportsService.ts      # Logic for generating reports
│   ├── routes
│   │   └── index.ts              # Sets up application routes
│   ├── views
│   │   ├── tabs
│   │   │   ├── harmonogram.tsx    # UI component for displaying schedules
│   │   │   └── raporty.tsx        # UI component for displaying reports
│   │   └── components
│   │       └── rmk-summary.tsx    # Reusable UI component for RMK summaries
│   └── db
│       ├── migrations
│       │   └── add-account-description.ts # Migration script for adding description field
│       └── seed.ts               # Seed data for initial database population
├── tests
│   ├── dictionary.test.ts        # Unit tests for dictionary functionality
│   └── reports.test.ts           # Unit tests for reports functionality
├── package.json                  # npm configuration file
├── tsconfig.json                 # TypeScript configuration file
└── README.md                     # Documentation for the project
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd harmonogram-rmk-app
   ```
3. Install dependencies:
   ```
   npm install
   ```

## Usage
To start the application, run:
```
npm start
```
Visit `http://localhost:3000` in your browser to access the application.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.