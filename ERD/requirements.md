# Entity-Relationship Diagram (ERD) Requirements

## Entities and Attributes

### User Entity
- **user_id** (Primary Key, UUID, Indexed)
- **first_name** (VARCHAR, NOT NULL)
- **last_name** (VARCHAR, NOT NULL)
- **email** (VARCHAR, UNIQUE, NOT NULL)
- **password_hash** (VARCHAR, NOT NULL)
- **phone_number** (VARCHAR, NULL)
- **role** (ENUM: guest, host, admin, NOT NULL)
- **created_at** (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

### Property Entity
- **property_id** (Primary Key, UUID, Indexed)
- **host_id** (Foreign Key, references User.user_id)
- **name** (VARCHAR, NOT NULL)
- **description** (TEXT, NOT NULL)
- **location** (VARCHAR, NOT NULL)
- **price_per_night** (DECIMAL, NOT NULL)
- **created_at** (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
- **updated_at** (TIMESTAMP, ON UPDATE CURRENT_TIMESTAMP)

### Booking Entity
- **booking_id** (Primary Key, UUID, Indexed)
- **property_id** (Foreign Key, references Property.property_id)
- **user_id** (Foreign Key, references User.user_id)
- **start_date** (DATE, NOT NULL)
- **end_date** (DATE, NOT NULL)
- **total_price** (DECIMAL, NOT NULL)
- **status** (ENUM: pending, confirmed, canceled, NOT NULL)
- **created_at** (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

### Payment Entity
- **payment_id** (Primary Key, UUID, Indexed)
- **booking_id** (Foreign Key, references Booking.booking_id)
- **amount** (DECIMAL, NOT NULL)
- **payment_date** (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
- **payment_method** (ENUM: credit_card, paypal, stripe, NOT NULL)

### Review Entity
- **review_id** (Primary Key, UUID, Indexed)
- **property_id** (Foreign Key, references Property.property_id)
- **user_id** (Foreign Key, references User.user_id)
- **rating** (INTEGER, CHECK: 1-5, NOT NULL)
- **comment** (TEXT, NOT NULL)
- **created_at** (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

### Message Entity
- **message_id** (Primary Key, UUID, Indexed)
- **sender_id** (Foreign Key, references User.user_id)
- **recipient_id** (Foreign Key, references User.user_id)
- **message_body** (TEXT, NOT NULL)
- **sent_at** (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

## Relationships

1. **User → Property** (One-to-Many): One user (host) can own multiple properties
2. **User → Booking** (One-to-Many): One user can have multiple bookings
3. **Property → Booking** (One-to-Many): One property can have multiple bookings
4. **Booking → Payment** (One-to-One): One booking has one payment
5. **Property → Review** (One-to-Many): One property can have multiple reviews
6. **User → Review** (One-to-Many): One user can write multiple reviews
7. **User → Message** (One-to-Many): One user can send/receive multiple messages

## Constraints

- Unique constraint on User.email
- Foreign key constraints on all relationship fields
- Rating constraint (1-5) on Review.rating
- Status constraints on Booking.status
- Role constraints on User.role
- Payment method constraints on Payment.payment_method