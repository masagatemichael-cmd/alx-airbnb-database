# Database Seed Data

## Overview
This directory contains SQL scripts for populating the AirBnB database with sample data for testing and development.

## Files
- `seed.sql` - Sample data insertion script

## Usage

### Prerequisites
- Database schema must be created first (run schema.sql)
- PostgreSQL database with UUID extension

### Installation
1. Ensure schema is created
2. Run the seed script:
```sql
\i seed.sql