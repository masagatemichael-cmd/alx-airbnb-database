# Database Normalization Documentation

## Normalization Process for AirBnB Database

### First Normal Form (1NF)
- **Eliminated repeating groups**: Each table contains only atomic values
- **Primary keys defined**: Each table has a primary key (UUID)
- **All columns contain single values**: No multi-valued attributes

### Second Normal Form (2NF)
- **All tables are in 1NF**
- **No partial dependencies**: All non-key attributes fully depend on the entire primary key
- **Examples**:
  - In Booking table: start_date, end_date, total_price all depend on booking_id
  - In Property table: name, description, location all depend on property_id

### Third Normal Form (3NF)
- **All tables are in 2NF**
- **No transitive dependencies**: Non-key attributes don't depend on other non-key attributes
- **Eliminated redundant data**:
  - User role is stored directly in User table (no separate role table needed as it's a simple enum)
  - Payment method is stored directly in Payment table
  - Booking status is stored directly in Booking table

### Normalization Decisions

#### Denormalized Elements (Intentional):
1. **User role as ENUM**: Small fixed set of values, no separate table needed
2. **Booking status as ENUM**: Limited status types, frequent queries
3. **Payment method as ENUM**: Fixed payment options, simple data

#### Normalized Elements:
1. **Separate tables for each entity**: Users, Properties, Bookings, Payments, Reviews, Messages
2. **Foreign key relationships**: Proper referential integrity
3. **No redundant data**: Each piece of information stored only once

### Indexing Strategy
- Primary keys automatically indexed
- Additional indexes on:
  - User.email (for login and lookups)
  - Property.location (for search)
  - Booking.property_id and user_id (for relationship queries)
  - Review.property_id (for property reviews)

### Data Integrity
- **NOT NULL constraints** on required fields
- **CHECK constraints** on rating values (1-5)
- **UNIQUE constraints** on email
- **FOREIGN KEY constraints** on all relationships
- **ENUM constraints** on status, role, and payment_method fields

The database design achieves 3NF while maintaining performance through strategic indexing and minimal intentional denormalization for frequently accessed simple data types.